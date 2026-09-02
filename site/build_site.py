#!/usr/bin/env python3
"""Assemble the MkDocs source tree (_site_src/) from the repository content.

The repo keeps its natural layout (docs/, templates/, tools/, ...); MkDocs wants
one docs_dir. This script stages the content, preserving repo-relative paths so
every internal link keeps working, and adds the website-only landing page and CSS.

Run from the repository root:  python site/build_site.py
Then:                          mkdocs build
"""
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "_site_src"

COPY_DIRS = ["docs", "assessments", "playbooks", "templates", "tools"]
COPY_FILES = ["ABOUT.md", "CONTRIBUTING.md", "ROADMAP.md", "CHANGELOG.md", "LICENSE"]

def main():
    if SRC.exists():
        shutil.rmtree(SRC)
    SRC.mkdir()
    for d in COPY_DIRS:
        shutil.copytree(ROOT / d, SRC / d, ignore=shutil.ignore_patterns(".DS_Store"))
    for f in COPY_FILES:
        p = ROOT / f
        if p.exists():
            shutil.copy2(p, SRC / f)
    # website-only files
    shutil.copy2(ROOT / "site" / "index.md", SRC / "index.md")
    shutil.copy2(ROOT / "site" / "templates-index.md", SRC / "templates" / "index.md")
    (SRC / "assets").mkdir()
    shutil.copy2(ROOT / "site" / "extra.css", SRC / "assets" / "extra.css")
    # Self-hosted IBM Plex. Staged under assets/ so that the same relative path
    # (../assets/fonts/) resolves both on the website and when a tool in tools/
    # is opened straight from a clone of the repository.
    shutil.copytree(ROOT / "assets" / "fonts", SRC / "assets" / "fonts")
    # Custom domain: GitHub Pages (Actions source) needs a CNAME file inside the
    # published artifact on every deploy — it does not persist this on its own.
    cname = ROOT / "site" / "CNAME"
    if cname.exists():
        shutil.copy2(cname, SRC / "CNAME")
    n = sum(1 for _ in SRC.rglob("*") if _.is_file())
    print(f"staged {n} files into {SRC.relative_to(ROOT)}/")

if __name__ == "__main__":
    main()
