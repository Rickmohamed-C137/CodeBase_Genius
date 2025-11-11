# utils.py
import os

# Print messages
def msg(text):
    print(text)

# Read file content (auto-detect encoding)
def read_file(file_path):
    encodings_to_try = ["utf-8", "utf-16", "utf-8-sig", "latin-1"]
    for enc in encodings_to_try:
        try:
            with open(file_path, "r", encoding=enc) as f:
                return f.read()
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError(f"Unable to decode file {file_path} with standard encodings.")

# List files with a given extension
def list_files(dir_path, ext=""):
    return [f for f in os.listdir(dir_path) if f.endswith(ext)]

# Write Markdown output
def write_markdown(file_path, content):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

# Generate Mermaid node
def generate_mermaid_node(filename):
    name = os.path.splitext(filename)[0]
    return f'{name}["{name}"]'

# Generate Mermaid edges (for demo, connect all nodes linearly)
def generate_mermaid_edge(filename):
    name = os.path.splitext(filename)[0]
    return f'{name} --> {name}_next'

# Safe execution wrapper
def safe_execute(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        print(f"[ERROR] Exception during execution: {e}")
        return None
