#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Regenerate assets/img/ from the originals in _src/img/.

Images are organised one folder per project:

    _src/img/MGDP/main.jpg  ->  assets/img/MGDP/main-{sm,md,lg}.jpg

Every still becomes three progressive JPEGs — 640w, 1100w and 1800w — which is
what picture() in build.py emits as a srcset. GIFs are re-encoded smaller if
that actually helps, and kept as GIFs.

`main` is the convention for a project's headline image: build.py uses
<dir>/main as the thumbnail on the home page.

Folders whose name starts with "_" are skipped — that is where images for
disabled projects are parked, so they cost nothing in the deployed site.

    python3 _src/optimize_images.py
"""
import os, shutil
from PIL import Image, ImageOps, ImageSequence, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True
Image.MAX_IMAGE_PIXELS = None

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC  = os.path.join(ROOT, "_src", "img")
OUT  = os.path.join(ROOT, "assets", "img")
SIZES = {"lg": 1800, "md": 1100, "sm": 640}
STILL = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tif", ".tiff"}


def sources():
    """Yield (relative_dir, filename) for every image outside a _-prefixed folder."""
    for dirpath, dirnames, filenames in os.walk(SRC):
        dirnames[:] = sorted(d for d in dirnames if not d.startswith("_"))
        rel = os.path.relpath(dirpath, SRC)
        rel = "" if rel == "." else rel
        if any(part.startswith("_") for part in rel.split(os.sep) if part):
            continue
        for fn in sorted(filenames):
            if os.path.splitext(fn)[1].lower() in STILL | {".gif"}:
                yield rel, fn


def flatten(im):
    """EXIF-rotate, and composite transparency onto white (diagrams assume it)."""
    im = ImageOps.exif_transpose(im)
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        bg = Image.new("RGB", im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[-1])
        return bg
    return im.convert("RGB")


def do_gif(src, dest):
    im = Image.open(src)
    w, h = im.size
    scale = min(1.0, 480 / w)
    best = None
    tmp = dest + ".tmp.gif"
    for step, colors in [(2, 96), (2, 64), (3, 64), (3, 48)]:
        frames, durs, acc = [], [], 0
        for i, f in enumerate(ImageSequence.Iterator(im)):
            d = f.info.get("duration", 80)
            if i % step:
                acc += d
                continue
            fr = f.convert("RGB")
            if scale < 1.0:
                fr = fr.resize((int(w * scale), int(h * scale)), Image.LANCZOS)
            frames.append(fr.convert("P", palette=Image.ADAPTIVE, colors=colors))
            durs.append(d + acc)
            acc = 0
        frames[0].save(tmp, format="GIF", save_all=True, append_images=frames[1:],
                       duration=durs, loop=0, optimize=True)
        if best is None or os.path.getsize(tmp) < best:
            best = os.path.getsize(tmp)
            shutil.copy(tmp, dest)
        if best < 1_400_000:
            break
    os.remove(tmp)
    if os.path.getsize(dest) >= os.path.getsize(src):
        shutil.copy(src, dest)


def main():
    expected = set()
    total_in = total_out = 0

    for rel, fn in sources():
        base, ext = os.path.splitext(fn)
        src = os.path.join(SRC, rel, fn)
        outdir = os.path.join(OUT, rel)
        os.makedirs(outdir, exist_ok=True)
        total_in += os.path.getsize(src)

        if ext.lower() == ".gif":
            dest = os.path.join(outdir, fn)
            do_gif(src, dest)
            made = os.path.getsize(dest)
            expected.add(os.path.relpath(dest, OUT))
        else:
            im = flatten(Image.open(src))
            made = 0
            for tag, maxw in SIZES.items():
                scale = min(1.0, maxw / im.width)
                r = im.resize((int(im.width * scale), int(im.height * scale)),
                              Image.LANCZOS) if scale < 1.0 else im
                dest = os.path.join(outdir, f"{base}-{tag}.jpg")
                r.save(dest, "JPEG", quality=84 if tag == "lg" else 82,
                       optimize=True, progressive=True, subsampling=1)
                made += os.path.getsize(dest)
                expected.add(os.path.relpath(dest, OUT))
        total_out += made
        label = os.path.join(rel, fn) if rel else fn
        print(f"  {label:<38} {os.path.getsize(src)//1024:>6}KB -> {made//1024:>6}KB")

    # drop anything in OUT with no surviving source
    for dirpath, _, filenames in os.walk(OUT, topdown=False):
        for fn in filenames:
            p = os.path.relpath(os.path.join(dirpath, fn), OUT)
            if p not in expected:
                os.remove(os.path.join(OUT, p))
                print(f"  removed orphan {p}")
        if dirpath != OUT and not os.listdir(dirpath):
            os.rmdir(dirpath)
            print(f"  removed empty {os.path.relpath(dirpath, OUT)}/")

    print(f"\nTOTAL {total_in//1024}KB -> {total_out//1024}KB")


if __name__ == "__main__":
    main()
