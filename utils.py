# utils.py
import os
import stat
import shutil

def _on_rm_error(func, path, exc_info):
    """
    Handler for shutil.rmtree on Windows to change file permissions then retry.
    """
    try:
        os.chmod(path, stat.S_IWRITE)
    except Exception:
        pass
    try:
        func(path)
    except Exception:
        pass

def safe_rmtree(path: str):
    """
    Remove a directory tree robustly on Windows and other OSes.
    If path does not exist, nothing happens.
    """
    if not path:
        return
    if os.path.exists(path):
        shutil.rmtree(path, onerror=_on_rm_error)
