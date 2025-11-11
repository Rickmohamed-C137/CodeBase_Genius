# main.jac
from pathlib import Path;
import os;
import traceback;
import time;

# load .env if present
try:
    from dotenv import load_dotenv;
    load_dotenv()
except Exception:
    pass

# import installed SDK
import google.generativeai as genai;

from utils import (
    msg,
    read_file,
    list_files,
    write_markdown,
    generate_mermaid_node,
    safe_execute,
);

# CONFIG
PROMPTS_DIR = Path("prompts")
OUTPUTS_DIR = Path("outputs")
DIAGRAM_FILE = OUTPUTS_DIR / "diagram.md"
# fallback candidates if list_models doesn't return useful items
MODEL_CANDIDATES = ["gemini-2.5-flash", "gemini-1.5", "text-bison-001"]

# AUTH
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not set in environment variables or .env file. Create a .env with GEMINI_API_KEY=... or set $env:GEMINI_API_KEY in this shell.")

# configure SDK if possible
try:
    if hasattr(genai, "configure"):
        genai.configure(api_key=GEMINI_API_KEY)
        msg("[INFO] genai.configure called.")
    elif hasattr(genai, "api_key"):
        genai.api_key = GEMINI_API_KEY
        msg("[INFO] genai.api_key set.")
    else:
        msg("[WARN] genai module found but no configure/api_key attribute detected.")
except Exception as e:
    msg(f"[WARN] genai.configure/api_key assignment raised: {e}")

msg("=== Project Starting with Gemini (v0.8.x style handler) ===")

PROMPTS_DIR.mkdir(exist_ok=True)
OUTPUTS_DIR.mkdir(exist_ok=True)

def choose_model():
    """Try genai.list_models() to pick a model id, else return candidates."""
    try:
        if hasattr(genai, "list_models"):
            try:
                mlist = genai.list_models()
                # mlist may be a list-like or dict — inspect
                if isinstance(mlist, list) and mlist:
                    # try to extract model id/name from first elements
                    first = mlist[0]
                    if isinstance(first, str):
                        return first
                    if isinstance(first, dict):
                        # common keys
                        for k in ("name", "id", "model"):
                            if k in first:
                                return first[k]
                    # fallback to string conversion
                    return str(first)
                # sometimes list_models returns an object with 'models' attribute
                if hasattr(mlist, "models") and getattr(mlist, "models"):
                    m0 = getattr(mlist, "models")[0]
                    for k in ("name", "id", "model"):
                        if isinstance(m0, dict) and k in m0:
                            return m0[k]
                        if hasattr(m0, k):
                            return getattr(m0, k)
                    return str(m0)
            except Exception as e:
                msg(f"[WARN] genai.list_models() call failed: {e}")
    except Exception:
        pass
    # fallback list
    for m in MODEL_CANDIDATES:
        return m
    return MODEL_CANDIDATES[0]

def _extract_text(resp):
    """Extract likely text from various response shapes."""
    try:
        if resp is None:
            return None
        if hasattr(resp, "text"):
            return resp.text
        if hasattr(resp, "content"):
            return resp.content if isinstance(resp.content, str) else str(resp.content)
        if hasattr(resp, "candidates"):
            c = getattr(resp, "candidates")
            if c and len(c) > 0:
                first = c[0]
                if hasattr(first, "output"):
                    return first.output
                if hasattr(first, "content"):
                    return first.content
                if isinstance(first, dict):
                    for k in ("output", "content", "text"):
                        if k in first:
                            return first[k]
        if isinstance(resp, dict):
            for k in ("text", "output", "result"):
                if k in resp:
                    v = resp[k]
                    if isinstance(v, str):
                        return v
                    if isinstance(v, list) and v:
                        first = v[0]
                        if isinstance(first, str):
                            return first
                        if isinstance(first, dict):
                            for k2 in ("output", "content", "text"):
                                if k2 in first:
                                    return first[k2]
        return str(resp)
    except Exception:
        return str(resp)

def try_generate_with_generative_model(model_id, prompt_text):
    """If genai.GenerativeModel exists, try to use it with several method names."""
    gm_cls = getattr(genai, "GenerativeModel", None)
    if not gm_cls:
        return None, "No GenerativeModel class available"
    try:
        gm = gm_cls(model_id)
    except Exception as e:
        return None, f"Constructing GenerativeModel('{model_id}') failed: {e}"
    # possible method names
    for meth in ("generate", "generate_text", "generate_content", "call"):
        if hasattr(gm, meth):
            try:
                fn = getattr(gm, meth)
                # try with common params (some methods accept prompt, some accept contents)
                try:
                    resp = fn(prompt_text)
                except TypeError:
                    resp = fn(model=model_id, prompt=prompt_text)
                text = _extract_text(resp)
                return text, None
            except Exception as e:
                # continue trying other methods
                last_err = f"GenerativeModel.{meth} raised: {e}"
                continue
    return None, f"GenerativeModel exists but no successful method call. Last error: {last_err if 'last_err' in locals() else 'none'}"

def try_client_models_generate(model_id, prompt_text):
    """Try client-based patterns: Client().models.generate_content or similar."""
    ClientClass = getattr(genai, "Client", None) or getattr(genai, "GenAIClient", None)
    if not ClientClass:
        return None, "No Client class on genai"
    try:
        client = ClientClass()
    except Exception as e:
        return None, f"Client() construction failed: {e}"

    models_obj = getattr(client, "models", None)
    if models_obj and hasattr(models_obj, "generate_content"):
        try:
            resp = models_obj.generate_content(model=model_id, contents=prompt_text)
            return _extract_text(resp), None
        except Exception as e:
            return None, f"client.models.generate_content failed: {e}"

    # try client.generate or client.generate_text
    for fn in ("generate_text", "generate", "generate_content"):
        if hasattr(client, fn):
            try:
                method = getattr(client, fn)
                try:
                    resp = method(model=model_id, prompt=prompt_text)
                except Exception:
                    resp = method(contents=prompt_text, model=model_id)
                return _extract_text(resp), None
            except Exception as e:
                last_e = e
                continue
    return None, f"Client-based attempts failed. Last error: {last_e if 'last_e' in locals() else 'none'}"

def fallback_attempts(model_id, prompt_text):
    """Try other shapes on the genai module directly (generate_text, text.generate, models.generate_text)."""
    # 1) genai.generate_text
    try:
        if hasattr(genai, "generate_text"):
            try:
                resp = genai.generate_text(model=model_id, prompt=prompt_text)
                return _extract_text(resp), None
            except Exception as e:
                last = f"genai.generate_text raised: {e}"
    except Exception:
        last = "genai.generate_text not available"
    # 2) genai.text.generate
    try:
        text_mod = getattr(genai, "text", None)
        if text_mod:
            for fn in ("generate", "generate_text"):
                if hasattr(text_mod, fn):
                    try:
                        fcall = getattr(text_mod, fn)
                        resp = fcall(model=model_id, prompt=prompt_text)
                        return _extract_text(resp), None
                    except Exception as e:
                        last = f"genai.text.{fn} raised: {e}"
    except Exception:
        last = "genai.text not usable"
    # 3) genai.models.generate_text
    try:
        models_mod = getattr(genai, "models", None)
        if models_mod and hasattr(models_mod, "generate_text"):
            try:
                resp = models_mod.generate_text(model=model_id, prompt=prompt_text)
                return _extract_text(resp), None
            except Exception as e:
                last = f"genai.models.generate_text raised: {e}"
    except Exception:
        last = "genai.models not usable"
    return None, f"No fallback succeeded. Last: {last}"

def generate_with_gemini(prompt_text):
    """Top-level generator: pick model, try several invocation styles until one works."""
    model_id = choose_model()
    msg(f"[INFO] Chosen model id: {model_id}")

    # 1) Try GenerativeModel path
    text, err = try_generate_with_generative_model(model_id, prompt_text)
    if text:
        return text
    msg(f"[DEBUG] GenerativeModel attempt failed: {err}")

    # 2) Try client-based
    text, err = try_client_models_generate(model_id, prompt_text)
    if text:
        return text
    msg(f"[DEBUG] Client-based attempt failed: {err}")

    # 3) Fallback direct attempts
    text, err = fallback_attempts(model_id, prompt_text)
    if text:
        return text
    msg(f"[ERROR] All attempts failed for model {model_id}: {err}")
    raise RuntimeError("All Gemini generation attempts failed: " + str(err))

def main():
    try:
        prompt_files = list_files(PROMPTS_DIR, ".txt")
    except Exception:
        prompt_files = []

    if not prompt_files:
        msg("[INFO] No prompt files found. Create prompts/*.txt and re-run.")
        return

    mermaid_lines = ["flowchart TD"]
    prev_node = None

    for pf in prompt_files:
        msg(f"[INFO] Processing prompt: {pf}")
        path = PROMPTS_DIR / pf
        prompt_text = safe_execute(read_file, path)
        if not prompt_text:
            msg(f"[WARN] Empty or unreadable prompt: {pf}")
            continue

        try:
            generated = generate_with_gemini(prompt_text)
        except Exception as e:
            msg(f"[ERROR] Generation failed for {pf}: {e}")
            debug_path = OUTPUTS_DIR / (pf + ".error.txt")
            with open(debug_path, "w", encoding="utf-8") as fh:
                fh.write("Generation error:\n")
                fh.write(str(e) + "\n\n")
                fh.write(traceback.format_exc())
            continue

        out_name = pf.replace(".txt", ".md")
        write_markdown(str(OUTPUTS_DIR / out_name), generated)
        msg(f"[INFO] Generated: {OUTPUTS_DIR / out_name}")

        node_label = pf.replace(".txt", "")
        mermaid_lines.append(generate_mermaid_node(node_label))
        if prev_node:
            mermaid_lines.append(f'    "{prev_node}" --> "{node_label}"')
        prev_node = node_label

    mermaid_text = "\n".join(mermaid_lines) + "\n"
    write_markdown(str(DIAGRAM_FILE), "```mermaid\n" + mermaid_text + "```\n")
    msg(f"[INFO] Mermaid diagram generated: {DIAGRAM_FILE}")

    msg("=== Project Finished ===")

if __name__ == "__main__":
    main()
