# streamlit_app.py
import streamlit as st
from pathlib import Path
import backend  # Our backend logic for cloning and analysis
import re

# Configure the Streamlit page settings, like title and layout.
st.set_page_config(
    page_title="Codebase Genius",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Use Streamlit's session state to keep track of the last generated file.
# This way, the data persists even when the user interacts with the app.
if "doc_path" not in st.session_state:
    st.session_state.doc_path = None

# --- User Interface ---

st.title("Codebase Genius 🧬")
st.markdown("Enter a public GitHub repository URL to automatically generate its documentation.")

# The sidebar holds all the user controls.
with st.sidebar:
    st.header("Controls")
    repo_url = st.text_input(
        "GitHub Repository URL",
        placeholder="e.g., https://github.com/user/repo-name"
    )

    # This button kicks off the main process.
    if st.button("Generate Documentation", type="primary"):
        if repo_url:
            # Show a spinner to let the user know something is happening.
            with st.spinner("Cloning repo, analyzing files, and generating docs... This may take a moment."):
                # This is where we call our main analysis function from backend.py.
                result = backend.generate_docs_for_repo(repo_url)

                if result.get("ok"):
                    # If successful, save the file path to the session state.
                    st.session_state.doc_path = result.get("doc_path")
                    st.success("Documentation generated successfully!")
                else:
                    # If it fails, clear the path and show the error message.
                    st.session_state.doc_path = None
                    error_message = result.get("error", "An unknown error occurred.")
                    st.error(f"Failed to generate docs: {error_message}")
        else:
            st.warning("Please enter a GitHub repository URL.")

# --- Main Content Display ---

st.header("Generated Documentation")

# Only show the output if a document has been successfully generated.
if st.session_state.doc_path:
    doc_path = Path(st.session_state.doc_path)
    if doc_path.exists():
        # Load the content of the generated markdown file.
        markdown_content = doc_path.read_text(encoding="utf-8")

        # This block finds the "Overview" section and injects CSS to style it.
        # This regex looks for "## Overview" and grabs all text until the next header.
        pattern = r"(## Overview\n)(.*?)(?=\n## |\Z)"
        
        # This little function wraps the overview content in a div with our style.
        def style_overview_content(match):
            header = match.group(1)
            content = match.group(2)
            # You can change the font-size percentage here.
            return f'{header}<div style="font-size: 100%;">{content}</div>'

        # Use the regex to find and replace the overview section with our styled version.
        # The re.DOTALL flag helps match across multiple lines.
        styled_markdown = re.sub(pattern, style_overview_content, markdown_content, count=1, flags=re.DOTALL)
        
        # Display the final markdown. We allow HTML to render our styled div.
        st.markdown(styled_markdown, unsafe_allow_html=True)

        # Add a download button to the sidebar.
        st.sidebar.download_button(
            label="Download Documentation (.md)",
            data=markdown_content, # Let the user download the original, unstyled file.
            file_name=doc_path.name,
            mime="text/markdown"
        )
    else:
        st.info("Documentation file not found. Please generate it using the controls on the left.")
else:
    # This message shows on the initial app load.
    st.info("No documentation has been generated yet. Enter a URL in the sidebar and click 'Generate'.")