"""Render PROPOSAL.md (and the two companions) to standalone HTML."""
from pathlib import Path

from markdown_it import MarkdownIt

CSS = """body{max-width:52em;margin:2em auto;padding:0 1em;font:16px/1.5 Georgia,serif;color:#111}
h1{font-size:1.6em;line-height:1.25}h2{margin-top:2em;border-bottom:1px solid #ccc}
table{border-collapse:collapse;font-size:.92em}td,th{border:1px solid #bbb;padding:.3em .6em;vertical-align:top}
code{font-family:ui-monospace,Menlo,monospace;font-size:.9em}a{color:#0645ad}"""
md = MarkdownIt("commonmark").enable("table")
for name in ("PROPOSAL", "PREREGISTRATION", "FORM_ANSWERS"):
    body = md.render(Path(f"{name}.md").read_text())
    Path(f"{name}.html").write_text(
        f"<!doctype html><meta charset='utf-8'><title>{name}</title><style>{CSS}</style>{body}")
    print("wrote", f"{name}.html")
