# liwanyue123.github.io

Personal site for **Wanyue Li** — robotics engineer. Plain static HTML/CSS/JS,
no framework and no build step required to deploy.

## Layout

```
index.html              home — hero, work, publications, experience,
                        education, honors, about, contact
work/<slug>/index.html  11 project pages (5 research + 6 earlier)
beyond/index.html       gallery: painting, 3D modelling, machine building
404.html  sitemap.xml  robots.txt  favicon.svg
assets/css/main.css     design system (tokens, layout, components)
assets/js/main.js       sticky nav, scroll reveal, scrollspy, cursor preview
assets/img/<Project>/   optimised images, one folder per project
assets/cv/              CV PDFs, linked from the nav and contact block
_src/build.py           content + page generator
_src/optimize_images.py regenerates assets/img/ from _src/img/
_src/img/<Project>/     ORIGINAL full-size images, one folder per project
```

## Editing content

All copy, project data and publications live in the data blocks at the top of
`_src/build.py`. Change them there and regenerate:

```bash
python3 _src/build.py
```

Editing the generated `.html` directly works too, but the next build overwrites it.

## Preview locally

```bash
python3 -m http.server 8899
# then open http://127.0.0.1:8899/
```

Paths are root-relative (`/assets/...`), so serve from the repo root — opening
`index.html` via `file://` will not load styles.

## Deploying

This is a GitHub Pages user site, served from the repo root. Copy the contents
of this folder over the `liwanyue123.github.io` repo and push. `.nojekyll` is
present so Jekyll does not touch the output.

## Notes

- **Images were rescued from the old site.** The 2023 site loaded every image
  from `s2.loli.net`, a third-party image host. All 33 are now stored locally in
  `_src/img/` (originals) and served from `assets/img/` as resized, progressive
  JPEGs. If you want a smaller repo you can delete `_src/img/` — but then the
  originals exist nowhere else.
- **Profile content comes from the CV** (`assets/cv/`, English version authoritative).
  Education, experience, honors, the six
  publications and the skills list all live in the data blocks at the top of
  `_src/build.py`.
- **Selected work is split into two groups**: doctoral research at ArcLab, HKU
  (2024–present) and earlier work (2018–2023).
- **The five research projects have no photography yet.** They render with a
  typographic "paper" tile in the work list and a grid-and-gradient hero on the
  detail page. To switch one to the photographic layout, add its image to
  `_src/img/`, rerun the optimiser, and set `"hero": "<asset-name>"` plus
  `"hero_pos"` on that entry in `R` — everything else adapts automatically.
- **Research copy is drawn from the published abstracts** (arXiv / IEEE Xplore /
  Wiley), not invented. Sources are linked from each project page.
- **No portrait photo.** The old site's `about/img/pic.jpg` returns a 404, so the
  About section uses a workshop photo instead. Drop a portrait into
  `_src/img/`, rerun the optimiser, and swap the name in `build_index()`.
- Videos are embedded from YouTube and Bilibili, not self-hosted.

## Images

One folder per project, mirrored from `_src/img/` into `assets/img/`:

```
_src/img/MGDP/main.jpg   ->   assets/img/MGDP/main-{sm,md,lg}.jpg
```

Conventions:

- **`main`** is the project's headline image. `build.py` uses `<dir>/main` as the
  thumbnail in the Selected work list; set `"thumb"` on a project to override.
- A project declares its folder with `"dir"`, and image references inside
  `media` / `hero` are then bare names resolved against it (`"src": "framework"`
  becomes `MGDP/framework`). A name containing `/` is used as-is.
- A project with no `hero` falls back to a typographic tile built from
  `tile` / `tile_mark`, so it still looks deliberate before artwork exists.
- Folders starting with `_` are **skipped** by the optimiser. `_src/img/_disabled/`
  holds artwork for hidden projects, so it costs nothing in the deployed site.

## Regenerating images

`_src/img/` holds every original. To re-derive the served sizes:

```bash
python3 _src/optimize_images.py
```

It writes `<name>-sm/-md/-lg.jpg` into `assets/img/` and deletes anything there
that no longer has a source. `python3 _src/build.py` likewise prunes
`work/<slug>/` directories whose project no longer exists.
