"""
CLI and helper tools to extract or download bundled CN lab files.
"""
import os
import shutil
import sys
from pathlib import Path

def get_bundle_dir() -> Path:
    """Return the absolute path to the directory containing all bundled lab files."""
    return Path(__file__).resolve().parent / "files"

def list_files():
    """List all bundled lab files."""
    files_dir = get_bundle_dir()
    if not files_dir.exists():
        print(f"Error: Bundle directory {files_dir} not found.")
        return []
    return sorted(os.listdir(files_dir))

def export_all_files(target_dir="."):
    """Copy all real client, server, and C++ lab files to the specified directory."""
    bundle_dir = get_bundle_dir()
    dest = Path(target_dir).resolve()
    dest.mkdir(parents=True, exist_ok=True)

    files = list_files()
    print(f"Downloading/Extracting {len(files)} CN lab files to: {dest}")
    for fname in files:
        src_path = bundle_dir / fname
        dst_path = dest / fname
        shutil.copy2(src_path, dst_path)
        print(f"  -> {fname}")
    print(f"\nAll files successfully saved in: {dest}")

def main():
    """CLI entry point for `cn-download` or `cn-extract`."""
    target_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    export_all_files(target_dir)

if __name__ == "__main__":
    main()

