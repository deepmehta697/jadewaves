"""Build only the isolated, unpublished pebble preview. Never regenerate the live site.

Extracts catalogue photos without supplier text/metadata. Four branded photos must
be supplied as approved clean crops in clean-inputs/; originals never go in media/.
"""
from __future__ import annotations

import json
import re
import shutil
from html import escape
from io import BytesIO
from pathlib import Path

from PIL import Image
from pypdf import PdfReader

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = Path("/Users/deepmehta/Downloads/PEBBLES STONE.pdf")


def main():
    entries = json.loads((HERE / "catalogue.json").read_text())
    reader = PdfReader(SOURCE)
    media = HERE / "media"
    media.mkdir(exist_ok=True)
    public_entries = []
    for entry in entries:
        clean = entry.get("clean_image")
        if clean:
            image = Image.open(HERE / "clean-inputs" / f"{clean}.png")
        else:
            source_image = reader.pages[entry["page"] - 1].images[entry["image"]]
            image = Image.open(BytesIO(source_image.data))
        image = image.convert("RGB")
        image.thumbnail((960, 960))
        image.info.clear()
        image.save(media / f'{entry["id"]}.webp', "WEBP", lossless=True, method=6)
        public_entries.append({
            "id": entry["id"], "name": entry["name"], "finish": entry["finish"],
            "sizes": entry["sizes"], "color": entry["color"],
            "packing": entry.get("packing", "25 kg bags"),
            "src": f'media/{entry["id"]}.webp',
            "width": image.width, "height": image.height,
        })
    first = public_entries[0]
    options = []
    finishes = ["Polished", "Natural", "Semi-polished", "Tumbled", "Coated", "Unpolished", "Finish to confirm"]
    for finish in finishes:
        options.append(f'<optgroup label="{finish}">')
        for entry in public_entries:
            if entry["finish"] == finish:
                options.append(f'<option value="{entry["id"]}">{escape(entry["name"])}</option>')
        options.append('</optgroup>')
    rows = ''.join(
        f'<tr><th scope="row">{escape(e["name"])}</th><td>{escape(e["finish"])}</td>'
        f'<td>{escape(" / ".join(e["sizes"]))}</td></tr>' for e in public_entries
    )
    template = (HERE / "page.html").read_text()
    replacements = {
        "{{OPTIONS}}": ''.join(options), "{{ROWS}}": rows,
        "{{COUNT}}": str(len(public_entries)),
        "{{DATA}}": json.dumps(public_entries, ensure_ascii=False).replace('<', '\\u003c'),
        "{{FIRST_WIDTH}}": str(first["width"]), "{{FIRST_HEIGHT}}": str(first["height"]),
    }
    for key, value in replacements.items():
        template = template.replace(key, value)
    assert not re.search(r'\{\{\w+\}\}', template)
    (HERE / "index.html").write_text(template)
    shutil.copy2(ROOT / "styles.css", HERE / "base.css")
    shutil.copy2(ROOT / "assets/jade-waves-logo-transparent.png", media / "jade-waves-logo.png")
    print(f'Preview only: {len(public_entries)} selections, {media}. No production pages changed.')


if __name__ == "__main__":
    main()
