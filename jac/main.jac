# jac/main.jac
walker generate_docs_walker(repo_url: str) -> dict {
    result = py_module.helpers.runtime.run_full_pipeline(repo_url)
    if result["ok"] {
        return result
    }
    emit_error(result["error"])
}

