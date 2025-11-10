# Codebase Genius — Minimal Python + Jac Integration

This is a compact, demo-grade implementation of **Codebase Genius**.
It clones a public GitHub repo, performs simple static analysis on Python files (AST),
generates a Markdown document listing classes/functions and a naive call graph,
and exposes a one-page Streamlit UI for interactive use. A minimal Jac walker is included to show integration.

## Project files
- `backend.py` — main Python pipeline (clone, analyze, render markdown).
- `utils.py` — safe directory removal helper for Windows.
- `helpers/runtime.py` — small bridge so Jac can call the Python pipeline.
- `jac/main.jac` — minimal Jac walker that calls the Python bridge.
- `streamlit_app.py` — Streamlit frontend.
- `requirements.txt` — Python dependencies.
- `outputs/` — generated docs are saved here at runtime.

## Setup (Windows / macOS / Linux)
1. Create & activate a virtual environment (recommended):
   ```bash
   python -m venv .venv
   # Windows PowerShell
   .\.venv\Scripts\Activate.ps1
   # macOS / Linux
   source .venv/bin/activate
