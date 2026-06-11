from __future__ import annotations

import shutil
from pathlib import Path

from PIL import Image


CELL_W = 192
CELL_H = 208
COLS = 8
ROWS = 9
SCALE = 0.60
TOP_PADDING = 12


def shrink_cells(src: Path, dst: Path) -> None:
    image = Image.open(src).convert("RGBA")
    out = Image.new("RGBA", image.size, (0, 0, 0, 0))

    for row in range(ROWS):
        for col in range(COLS):
            left = col * CELL_W
            top = row * CELL_H
            cell = image.crop((left, top, left + CELL_W, top + CELL_H))
            bbox = cell.getbbox()
            if bbox is None:
                continue

            sprite = cell.crop(bbox)
            new_w = max(1, round(sprite.width * SCALE))
            new_h = max(1, round(sprite.height * SCALE))
            sprite = sprite.resize((new_w, new_h), Image.Resampling.LANCZOS)

            x = left + (CELL_W - new_w) // 2
            y = top + TOP_PADDING
            out.alpha_composite(sprite, (x, y))

    dst.parent.mkdir(parents=True, exist_ok=True)
    out.save(dst, "WEBP", lossless=True)


def main() -> None:
    run_dir = Path(r"C:\Users\user2\Desktop\Dev\hatch-pet-runs\pengdori")
    final_sheet = run_dir / "final" / "spritesheet.webp"
    installed_sheet = Path(r"C:\Users\user2\.codex\pets\pengdori\spritesheet.webp")
    backup = run_dir / "final" / "spritesheet.large-backup.webp"

    if not backup.exists():
        shutil.copy2(final_sheet, backup)

    tmp = run_dir / "final" / "spritesheet.shrunk.webp"
    shrink_cells(backup, tmp)
    shutil.copy2(tmp, final_sheet)
    shutil.copy2(tmp, installed_sheet)


if __name__ == "__main__":
    main()
