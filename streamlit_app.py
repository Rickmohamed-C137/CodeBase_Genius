# streamlit_app.py
import streamlit as st
import os
from backend import generate_docs_for_repo

st.set_page_config(page_title="Codebase Genius (Minimal)", layout="wide")

st.title("Codebase Genius — Minimal Documentation Generator")
st.write("Enter a **public** GitHub repository URL and click Generate. This demo focuses on Python code and produces a Markdown file listing classes, functions and a naive call graph.")

repo_url = st.text_input("GitHub repo URL (e.g. https://github.com/psf/requests)", "")

col1, col2 = st.columns([2, 1])
with col1:
    if st.button("Generate documentation"):
        if not repo_url:
            st.error("Please enter a GitHub repository URL.")
        else:
            with st.spinner("Cloning repository and generating documentation..."):
                res = generate_docs_for_repo(repo_url)
            if not res.get("ok"):
                st.error(f"Failed: {res.get('error')}")
            else:
                out_path = res.get("doc_path")
                st.success(f"Documentation generated: {out_path}")
                try:
                    with open(out_path, "r", encoding="utf-8") as fh:
                        md = fh.read()
                    st.markdown(md)
                except Exception as e:
                    st.warning(f"Could not open generated file for preview: {e}")
with col2:
    st.info("Notes")
    st.write("- This demo uses a shallow clone for speed.")
    st.write("- For large repos, generation may take longer or fail due to memory limits.")
    st.write("- Generated markdown is saved under the `outputs/` folder.")
