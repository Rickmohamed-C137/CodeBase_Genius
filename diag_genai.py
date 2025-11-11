# diag_genai.py
import os
import sys
import importlib
import traceback
from pathlib import Path

def show(msg):
    print(msg)

def inspect_module(mod):
    attrs = sorted(dir(mod))
    # show a focused set of likely names
    interesting = [a for a in attrs if any(k in a.lower() for k in ("generate", "text", "models", "client", "api", "configure", "candidates", "create", "Client", "Generative"))]
    return attrs, interesting

def try_configure(mod, key):
    out = []
    try:
        if hasattr(mod, "configure"):
            try:
                mod.configure(api_key=key)
                out.append("Called mod.configure(api_key=...) successfully.")
            except Exception as e:
                out.append(f"mod.configure(...) raised: {e}")
        if hasattr(mod, "api_key"):
            try:
                mod.api_key = key
                out.append("Assigned mod.api_key = key successfully.")
            except Exception as e:
                out.append(f"Assigning mod.api_key raised: {e}")
        # nothing else to do; client-based configs are handled at call time
    except Exception as e:
        out.append(f"configure checks raised: {e}")
    return out

def safe_call_report(mod):
    results = []
    # pattern 1: mod.generate_text(...)
    try:
        if hasattr(mod, "generate_text"):
            results.append("Found mod.generate_text -- would call with (model, prompt, ...).")
        else:
            results.append("No mod.generate_text attribute.")
    except Exception as e:
        results.append(f"Error inspecting generate_text: {e}")

    # pattern 2: mod.text.generate or mod.text.generate_text
    try:
        text_mod = getattr(mod, "text", None)
        if text_mod is None:
            results.append("No mod.text submodule.")
        else:
            found = []
            for fn in ("generate", "generate_text"):
                if hasattr(text_mod, fn):
                    found.append(fn)
            results.append(f"mod.text found. functions: {found}")
    except Exception as e:
        results.append(f"Error inspecting mod.text: {e}")

    # pattern 3: mod.models.generate_text
    try:
        models_mod = getattr(mod, "models", None)
        if models_mod is None:
            results.append("No mod.models submodule.")
        else:
            results.append("mod.models found; check for generate_text attr.")
            if hasattr(models_mod, "generate_text"):
                results.append("mod.models.generate_text exists.")
            else:
                results.append("mod.models.generate_text does NOT exist.")
    except Exception as e:
        results.append(f"Error inspecting mod.models: {e}")

    # pattern 4: Client class
    for cname in ("Client", "GenAIClient", "GenerativeModel"):
        try:
            if hasattr(mod, cname):
                results.append(f"Module exposes {cname}. Could try Client-based calls.")
        except Exception as e:
            results.append(f"Error inspecting {cname}: {e}")

    return results

def main():
    show("=== Diagnostic for google.generativeai ===")
    show(f"Python: {sys.version.strip()}")
    show(f"CWD: {Path.cwd()}")
    show(f"VENV (sys.executable): {sys.executable}")
    show("")

    # print installed package version if present
    try:
        import pkgutil, importlib.metadata
        try:
            ver = importlib.metadata.version("google-generativeai")
        except Exception:
            try:
                ver = importlib.metadata.version("google-ai-generativelanguage")
            except Exception:
                ver = None
        show(f"Installed package version (guesses): {ver}")
    except Exception:
        show("Could not determine package version via importlib.metadata.")

    # try import
    try:
        mod = importlib.import_module("google.generativeai")
        show("Imported google.generativeai successfully.")
    except Exception as e:
        show("Failed to import google.generativeai:")
        show(traceback.format_exc())
        return

    # show high-level attributes
    attrs, interesting = inspect_module(mod)
    show(f"Total attributes on module: {len(attrs)}")
    show("Some interesting attributes (filtered):")
    for it in interesting[:80]:
        show("  " + it)
    show("")

    # show top-level config attempts
    key = os.getenv("GEMINI_API_KEY", None)
    show(f"GEMINI_API_KEY present in env: {bool(key)}")
    if key:
        show("Attempting to configure module (no network calls yet):")
    conf_out = try_configure(mod, key)
    for line in conf_out:
        show("  " + line)
    show("")

    # show call pattern reports
    show("Reporting which call patterns are present (no network calls will be made):")
    rep = safe_call_report(mod)
    for r in rep:
        show("  " + r)
    show("")

    show("=== End diagnostic ===")

if __name__ == "__main__":
    main()
