"""MkDocs hooks for the Open CDC Framework site.

`site/build_site.py` stages two website-only pages into the MkDocs source tree
under names that do not exist in the repository:

    site/index.md            ->  index.md
    site/templates-index.md  ->  templates/index.md

Without this hook the theme's "edit this page" action would point at
`edit/main/index.md` and `edit/main/templates/index.md`, both of which 404 on
GitHub. Repoint them at the files a contributor should actually edit.
"""

STAGED_PAGES = {
    "index.md": "site/index.md",
    "templates/index.md": "site/templates-index.md",
}


def on_files(files, config):
    for f in files:
        source = STAGED_PAGES.get(f.src_uri)
        if source is not None:
            f.edit_uri = source
    return files
