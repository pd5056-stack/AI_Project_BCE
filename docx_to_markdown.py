from pathlib import Path
import re
import sys

from docx import Document
from docx.document import Document as _Document
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
from docx.table import Table
from docx.text.paragraph import Paragraph


def clean_text(text: str) -> str:
    text = text.replace("\u00a0", " ")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def iter_block_items(parent):
    if isinstance(parent, _Document):
        parent_elm = parent.element.body
    else:
        parent_elm = parent._element

    for child in parent_elm.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, parent)
        elif isinstance(child, CT_Tbl):
            yield Table(child, parent)


def paragraph_to_md(paragraph: Paragraph) -> str:
    text = clean_text(paragraph.text)
    if not text:
        return ""

    style = paragraph.style
    style_name = (style.name if style is not None else "").lower()

    if style_name.startswith("heading"):
        m = re.search(r"heading\s*(\d+)", style_name)
        level = int(m.group(1)) if m else 1
        level = max(1, min(level, 6))
        return f"{'#' * level} {text}"

    if "list bullet" in style_name:
        return f"- {text}"

    if "list number" in style_name:
        return f"1. {text}"

    return text


def table_to_md(table: Table) -> str:
    rows = []
    for row in table.rows:
        rows.append([clean_text(cell.text) for cell in row.cells])

    if not rows:
        return ""

    max_cols = max(len(r) for r in rows)
    normalized = [r + [""] * (max_cols - len(r)) for r in rows]

    header = normalized[0]
    sep = ["---"] * max_cols

    lines = [
        "| " + " | ".join(header) + " |",
        "| " + " | ".join(sep) + " |",
    ]

    for r in normalized[1:]:
        lines.append("| " + " | ".join(r) + " |")

    return "\n".join(lines)


def convert_docx_to_markdown(input_path: Path, output_path: Path):
    doc = Document(str(input_path))
    chunks = []

    for item in iter_block_items(doc):
        if isinstance(item, Paragraph):
            md = paragraph_to_md(item)
        else:
            md = table_to_md(item)

        if md:
            chunks.append(md)

    # Compress excessive empty lines while keeping section spacing readable.
    content = "\n\n".join(chunks)
    content = re.sub(r"\n{3,}", "\n\n", content).strip() + "\n"
    output_path.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python docx_to_markdown.py <input.docx> <output.md>")
        raise SystemExit(1)

    src = Path(sys.argv[1])
    dst = Path(sys.argv[2])

    if not src.exists():
        print(f"Input file not found: {src}")
        raise SystemExit(2)

    convert_docx_to_markdown(src, dst)
    print(f"Converted: {src} -> {dst}")
