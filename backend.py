# backend.py
import os
import uuid
import json
import shutil
import logging
from pathlib import Path
from typing import Dict, Any
from git import Repo, GitCommandError
from jinja2 import Template
import ast

# Setup basic logging
logging.basicConfig(level=logging.INFO)

TMP_ROOT = "tmp"       # where repositories are cloned
OUT_ROOT = "outputs"   # where generated docs are saved

# Markdown template for the final documentation
MD_TEMPLATE = """# {{ repo_name }}

## Overview

{{ readme_summary }}

## Files Scanned
{{ file_tree }}

## API Reference (Classes & Functions)

{% for f in items %}
### {{ f.path }}

{% if f.classes %}
**Classes**
{% for c in f.classes %}
- `{{ c.name }}` — {{ c.doc or "No docstring." }}
{% endfor %}
{% endif %}

{% if f.functions %}
**Functions**
{% for fn in f.functions %}
- `{{ fn.name }}()` — {{ fn.doc or "No docstring." }}
{% endfor %}
{% endif %}

{% endfor %}

## Call Graph (Mermaid Diagram)

```mermaid
graph TD
{% for e in edges %}
  "{{ e.src }}" --> "{{ e.dst }}"
{% endfor %}
"""

def safe_rmtree(path: str):
    """Remove a directory tree safely, handling read-only files (Windows)."""
    if os.path.exists(path):
        def onerror(func, path, exc_info):
            try:
                os.chmod(path, 0o777)
                func(path)
            except Exception as e:
                logging.warning(f"Failed to remove {path}: {e}")
        shutil.rmtree(path, onerror=onerror)

def _ensure_dirs():
    Path(TMP_ROOT).mkdir(parents=True, exist_ok=True)
    Path(OUT_ROOT).mkdir(parents=True, exist_ok=True)

def clone_repo(repo_url: str) -> Dict[str, Any]:
    """Shallow-clone the repo into a unique tmp directory and remove .git."""
    _ensure_dirs()
    job_id = f"job{uuid.uuid4().hex[:8]}"
    target = os.path.join(TMP_ROOT, job_id)
    safe_rmtree(target)
    os.makedirs(target, exist_ok=True)
    try:
        Repo.clone_from(repo_url, target, depth=1)
        gitdir = os.path.join(target, ".git")
        safe_rmtree(gitdir)
        return {"ok": True, "job_id": job_id, "path": target}
    except GitCommandError as e:
        safe_rmtree(target)
        return {"ok": False, "error": str(e)}
    except Exception as e:
        safe_rmtree(target)
        return {"ok": False, "error": str(e)}

def _read_readme(repo_path: str) -> str:
    """Return the first chunk of README text (if any) or a default message."""
    for name in ("README.md", "README.MD", "readme.md", "README.txt"):
        p = os.path.join(repo_path, name)
        if os.path.exists(p):
            try:
                with open(p, "r", encoding="utf-8") as fh:
                    text = fh.read(2000)
                    text = text.replace("\r\n", " ").replace("\n", " ")
                return text.strip()
            except Exception:
                continue
    return "No README found."

def _build_file_tree(repo_path: str) -> list:
    """Build a simple list of files under the repository (relative paths and sizes)."""
    out = []
    ignore_dirs = {".git", "pycache", "node_modules", "venv", ".venv"}
    for root, dirs, files in os.walk(repo_path):
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        for fname in sorted(files):
            full = os.path.join(root, fname)
            rel = os.path.relpath(full, repo_path)
            try:
                size = os.path.getsize(full)
            except OSError:
                size = 0
            out.append({"path": rel, "size": size})
    return out

def analyze_python(repo_path: str) -> Dict[str, Any]:
    """Parse python files under repo_path and extract top-level classes, functions, and a naive call graph."""
    items = []
    edges = []
    func_index: Dict[str, list] = {}

    # Collect Python files
    py_files = []
    for root, dirs, files in os.walk(repo_path):
        dirs[:] = [d for d in dirs if d not in {".git", "__pycache__", "venv", ".venv"}]
        for f in files:
            if f.endswith(".py"):
                py_files.append(os.path.join(root, f))

    # First pass: record classes and functions
    for path in py_files:
        rel = os.path.relpath(path, repo_path)
        try:
            with open(path, "r", encoding="utf-8") as fh:
                src = fh.read()
            tree = ast.parse(src)
        except Exception:
            continue

        file_entry = {"path": rel, "classes": [], "functions": []}
        for node in tree.body:
            if isinstance(node, ast.ClassDef):
                doc = ast.get_docstring(node) or ""
                file_entry["classes"].append({"name": node.name, "doc": doc})
            elif isinstance(node, ast.FunctionDef):
                doc = ast.get_docstring(node) or ""
                file_entry["functions"].append({"name": node.name, "doc": doc})
                unique = f"{rel}::{node.name}"
                func_index.setdefault(node.name, []).append(unique)
        items.append(file_entry)

    # Second pass: detect simple function calls
    for path in py_files:
        rel = os.path.relpath(path, repo_path)
        try:
            with open(path, "r", encoding="utf-8") as fh:
                src = fh.read()
            tree = ast.parse(src)
        except Exception:
            continue

        defined = [n["name"] for n in next((it for it in items if it["path"] == rel), {"functions": []})["functions"]]
        called: list = []

        class CallVisitor(ast.NodeVisitor):
            def visit_Call(self, node):
                fn = node.func
                if isinstance(fn, ast.Name):
                    called.append(fn.id)
                elif isinstance(fn, ast.Attribute):
                    called.append(fn.attr)
                self.generic_visit(node)

        CallVisitor().visit(tree)

        for caller in defined:
            caller_ids = func_index.get(caller, [])
            for callee_name in called:
                callee_ids = func_index.get(callee_name, [])
                for c in caller_ids:
                    for d in callee_ids:
                        edges.append({"src": c, "dst": d})

    return {"items": items, "edges": edges}

def _render_markdown(repo_name: str, readme_summary: str, file_tree: list, analysis: dict) -> str:
    tpl = Template(MD_TEMPLATE)
    md = tpl.render(
        repo_name=repo_name,
        readme_summary=readme_summary,
        file_tree=json.dumps(file_tree, indent=2),
        items=analysis.get("items", []),
        edges=analysis.get("edges", []),
    )
    return md

def generate_docs_for_repo(repo_url: str) -> Dict[str, Any]:
    """Full pipeline: clone -> analyze -> render -> save."""
    _ensure_dirs()
    clone_res = clone_repo(repo_url)
    if not clone_res.get("ok"):
        return {"ok": False, "error": clone_res.get("error")}

    job_id = clone_res["job_id"]
    path = clone_res["path"]

    readme = _read_readme(path)
    ft = _build_file_tree(path)
    analysis = analyze_python(path)

    repo_name = repo_url.rstrip("/").split("/")[-1] or job_id
    md = _render_markdown(repo_name, readme, ft, analysis)

    out_path = os.path.join(OUT_ROOT, f"{job_id}_docs.md")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(md)

    return {"ok": True, "job_id": job_id, "doc_path": out_path}