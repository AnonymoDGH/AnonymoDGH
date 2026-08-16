#!/usr/bin/env python3
"""Generate profile README SVG assets from live GitHub data.

Stdlib only. Produces (in <repo>/assets):
  stats.svg        - glass stats card
  langs.svg        - language bars card
  snake.svg        - animated contribution snake (dark)
  snake-light.svg  - animated contribution snake (light)

Runs locally or in GitHub Actions (see .github/workflows/generate.yml).
"""
import json
import math
import re
import urllib.request
from datetime import date
from pathlib import Path

USER = "AnonymoDGH"
UA = {"User-Agent": f"{USER}-profile-readme-generator"}
ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
LANG_COLORS = {
    "Python": "#3572A5", "TypeScript": "#3178c6", "JavaScript": "#f1e05a",
    "HTML": "#e34c26", "C++": "#f34b7d", "C": "#8a8a8a", "Java": "#b07219",
    "Lua": "#4a67d6", "C#": "#178600", "Smarty": "#f0c040",
    "Shell": "#89e051", "CSS": "#9a5feb", "Go": "#00ADD8", "Rust": "#dea584",
}
FONT = "'JetBrains Mono', 'Cascadia Code', 'Segoe UI', monospace"


def http_get(url, headers=None, as_json=False):
    h = dict(UA)
    if headers:
        h.update(headers)
    req = urllib.request.Request(url, headers=h)
    with urllib.request.urlopen(req, timeout=60) as resp:
        raw = resp.read().decode("utf-8", "replace")
    return json.loads(raw) if as_json else raw


# ---------------------------------------------------------------- data

def fetch_contributions():
    """Scrape the public contributions calendar (no auth needed)."""
    html = http_get(f"https://github.com/users/{USER}/contributions")
    cells = {}
    pat = (r'data-date="(\d{4}-\d{2}-\d{2})" '
           r'id="contribution-day-component-(\d+)-(\d+)" data-level="(\d)"')
    for d, row, col, lvl in re.findall(pat, html):
        cells[(int(row), int(col))] = {"date": d, "level": int(lvl), "count": 0}
    tip_pat = (r'<tool-tip[^>]*for="contribution-day-component-(\d+)-(\d+)"'
               r'[^>]*>([^<]*)</tool-tip>')
    for row, col, tip in re.findall(tip_pat, html):
        m = re.match(r"(\d+) contributions? on", tip.strip())
        key = (int(row), int(col))
        if key in cells:
            cells[key]["count"] = int(m.group(1)) if m else 0
    return cells


def fetch_user():
    return http_get(f"https://api.github.com/users/{USER}", as_json=True)


def fetch_repos():
    repos, page = [], 1
    while True:
        batch = http_get(
            f"https://api.github.com/users/{USER}/repos?per_page=100&page={page}",
            as_json=True)
        repos.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    return repos


def fetch_commits():
    try:
        data = http_get(
            f"https://api.github.com/search/commits?q=author:{USER}",
            headers={"Accept": "application/vnd.github+json"}, as_json=True)
        return int(data.get("total_count", 0))
    except Exception:
        return 0


# ---------------------------------------------------------------- svg

def svg_open(w, h):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" font-family="{FONT}">')


def build_stats(user, repos, commits):
    own = [r for r in repos if not r.get("fork")]
    stars = sum(r.get("stargazers_count", 0) for r in own)
    tiles = [
        ("COMMITS", f"{commits:,}"),
        ("STARS", f"{stars:,}"),
        ("REPOS", f"{len(repos):,}"),
        ("FOLLOWERS", f"{user.get('followers', 0):,}"),
        ("PYPI PKGS", "7"),
        ("NPM PKGS", "1"),
    ]
    W, H = 520, 292
    out = [svg_open(W, H)]
    out.append(f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="16" '
               f'fill="#16161e" stroke="#7aa2f7" stroke-opacity="0.25"/>')
    out.append(f'<rect x="1" y="1" width="{W-2}" height="4" rx="2" '
               f'fill="#7aa2f7" fill-opacity="0.6"/>')
    out.append(f'<text x="26" y="42" font-size="20" font-weight="700" '
               f'fill="#7aa2f7">{USER}</text>')
    out.append('<text x="26" y="62" font-size="11" fill="#565f89">'
               'github stats · generated with python stdlib</text>')
    for i, (label, value) in enumerate(tiles):
        col, row = i % 3, i // 3
        x = 26 + col * 158
        y = 82 + row * 96
        out.append(f'<rect x="{x}" y="{y}" width="146" height="84" rx="12" '
                   f'fill="#7aa2f7" fill-opacity="0.06" stroke="#7aa2f7" '
                   f'stroke-opacity="0.12"/>')
        out.append(f'<text x="{x+73}" y="{y+40}" font-size="24" font-weight="700" '
                   f'fill="#e6e9f5" text-anchor="middle">{value}</text>')
        out.append(f'<text x="{x+73}" y="{y+62}" font-size="10" fill="#565f89" '
                   f'text-anchor="middle" letter-spacing="1.5">{label}</text>')
    out.append('</svg>')
    return "\n".join(out)


def build_langs(repos):
    own = [r for r in repos if not r.get("fork") and r.get("language")]
    weight = {}
    for r in own:
        lang = r["language"]
        weight[lang] = weight.get(lang, 0) + max(int(r.get("size") or 0), 1)
    total = sum(weight.values()) or 1
    top = sorted(weight.items(), key=lambda kv: kv[1], reverse=True)[:8]
    W, H = 520, 292
    out = [svg_open(W, H)]
    out.append(f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="16" '
               f'fill="#16161e" stroke="#7aa2f7" stroke-opacity="0.25"/>')
    out.append(f'<rect x="1" y="1" width="{W-2}" height="4" rx="2" '
               f'fill="#7aa2f7" fill-opacity="0.6"/>')
    out.append(f'<text x="26" y="42" font-size="20" font-weight="700" '
               f'fill="#7aa2f7">Languages</text>')
    out.append('<text x="26" y="62" font-size="11" fill="#565f89">'
               'weighted by repository size · own repos only</text>')
    for i, (lang, w) in enumerate(top):
        y = 84 + i * 25
        pct = w / total * 100
        color = LANG_COLORS.get(lang, "#7aa2f7")
        bar_w = max(6, round(300 * pct / 100))
        out.append(f'<text x="26" y="{y+9}" font-size="11" fill="#a9b1d6">'
                   f'{lang}</text>')
        out.append(f'<rect x="130" y="{y}" width="300" height="11" rx="5.5" '
                   f'fill="#ffffff" fill-opacity="0.05"/>')
        out.append(f'<rect x="130" y="{y}" width="{bar_w}" height="11" rx="5.5" '
                   f'fill="{color}"/>')
        out.append(f'<text x="494" y="{y+9}" font-size="10" fill="#565f89" '
                   f'text-anchor="end">{pct:.1f}%</text>')
    out.append('</svg>')
    return "\n".join(out)


def build_snake(cells, dark=True):
    if dark:
        empty = "#161b22"
        levels = ["#0e4429", "#006d32", "#26a641", "#39d353"]
        snake, head, eye = "#39d353", "#4ade80", "#0b0d14"
        text = "#565f89"
    else:
        empty = "#ebedf0"
        levels = ["#9be9a8", "#40c463", "#30a14e", "#216e39"]
        snake, head, eye = "#30a14e", "#216e39", "#ffffff"
        text = "#57606a"

    CELL, STEP = 11, 14
    X0, Y0 = 34, 22
    ncols = max(c for (_, c) in cells) + 1
    W = X0 + ncols * STEP + 8
    H = Y0 + 7 * STEP + 24

    out = [svg_open(W, H)]

    # month labels
    ordered = sorted(cells.items(), key=lambda kv: kv[1]["date"])
    prev = None
    for (_, col), c in ordered:
        m = c["date"][:7]
        if m != prev:
            label = MONTHS[int(c["date"][5:7]) - 1]
            out.append(f'<text x="{X0 + col * STEP}" y="12" font-size="9" '
                       f'fill="{text}">{label}</text>')
            prev = m

    # weekday labels
    for row, name in ((1, "Mon"), (3, "Wed"), (5, "Fri")):
        out.append(f'<text x="2" y="{Y0 + row * STEP + 9}" font-size="8" '
                   f'fill="{text}">{name}</text>')

    # cells
    for (row, col), c in sorted(cells.items()):
        fill = levels[c["level"] - 1] if c["level"] > 0 else empty
        out.append(f'<rect x="{X0 + col * STEP}" y="{Y0 + row * STEP}" '
                   f'width="{CELL}" height="{CELL}" rx="2.5" fill="{fill}"/>')

    # caption + legend
    total = sum(c["count"] for c in cells.values())
    cy = Y0 + 7 * STEP + 16
    out.append(f'<text x="2" y="{cy}" font-size="9" fill="{text}">'
               f'{total:,} contributions in the last year</text>')
    lx = W - 118
    out.append(f'<text x="{lx - 6}" y="{cy}" font-size="9" fill="{text}" '
               f'text-anchor="end">Less</text>')
    for i in range(5):
        fill = empty if i == 0 else levels[i - 1]
        out.append(f'<rect x="{lx + i * 15}" y="{cy - 9}" width="{CELL}" '
                   f'height="{CELL}" rx="2.5" fill="{fill}"/>')
    out.append(f'<text x="{lx + 5 * 15 + 6}" y="{cy}" font-size="9" '
               f'fill="{text}">More</text>')

    # snake path: column-major zigzag
    pts = []
    for col in range(ncols):
        rows = sorted(r for (r, c2) in cells if c2 == col)
        if col % 2 == 1:
            rows = rows[::-1]
        for r in rows:
            pts.append((X0 + col * STEP + CELL / 2, Y0 + r * STEP + CELL / 2))
    d = "M{:.1f} {:.1f}".format(*pts[0]) + "".join(
        " L{:.1f} {:.1f}".format(x, y) for x, y in pts[1:])
    length = sum(math.hypot(b[0] - a[0], b[1] - a[1])
                 for a, b in zip(pts, pts[1:]))
    body = 16 * STEP
    dur = max(12, round(length / 300))

    out.append(f'<path d="{d}" fill="none" stroke="{snake}" stroke-width="9" '
               f'stroke-linecap="round" stroke-linejoin="round" '
               f'stroke-dasharray="{body} {length + body:.0f}" '
               f'stroke-opacity="0.95">'
               f'<animate attributeName="stroke-dashoffset" from="{body}" '
               f'to="{body - length:.0f}" dur="{dur}s" '
               f'repeatCount="indefinite"/></path>')
    out.append(f'<g><circle r="6.5" fill="{head}"/>'
               f'<circle cx="2.4" cy="-2.7" r="1.4" fill="{eye}"/>'
               f'<circle cx="2.4" cy="2.7" r="1.4" fill="{eye}"/>'
               f'<animateMotion dur="{dur}s" repeatCount="indefinite" '
               f'rotate="auto" path="{d}"/></g>')

    out.append('</svg>')
    return "\n".join(out)



def build_activity(cells):
    """Area chart of daily contributions over the last year."""
    ordered = sorted(cells.items(), key=lambda kv: kv[1]["date"])
    counts = [c["count"] for (_, _), c in ordered]
    dates = [c["date"] for (_, _), c in ordered]
    n = len(counts)
    if n == 0:
        return ""
    W, H = 784, 180
    pad_l, pad_r, pad_t, pad_b = 34, 12, 26, 26
    plot_w = W - pad_l - pad_r
    plot_h = H - pad_t - pad_b
    ymax = max(counts) if max(counts) > 0 else 1
    ymax = max(ymax, 4)

    def px(i):
        return pad_l + (i / max(n - 1, 1)) * plot_w

    def py(v):
        return pad_t + plot_h - (v / ymax) * plot_h

    out = [svg_open(W, H)]
    out.append(f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="16" '
               f'fill="#16161e" stroke="#7aa2f7" stroke-opacity="0.25"/>')
    out.append(f'<text x="26" y="20" font-size="13" font-weight="700" '
               f'fill="#7aa2f7">Contribution activity · last year</text>')

    # gridlines
    for g in range(5):
        v = ymax * g / 4
        y = py(v)
        out.append(f'<line x1="{pad_l}" y1="{y:.1f}" x2="{W-pad_r}" y2="{y:.1f}" '
                   f'stroke="#ffffff" stroke-opacity="0.05"/>')
        out.append(f'<text x="{pad_l-6}" y="{y+3:.1f}" font-size="8" '
                   f'fill="#565f89" text-anchor="end">{v:.0f}</text>')

    # area path
    line_pts = " ".join(f"{px(i):.1f},{py(v):.1f}" for i, v in enumerate(counts))
    area = (f"M{px(0):.1f},{py(0):.1f} " +
            " ".join(f"L{px(i):.1f},{py(v):.1f}" for i, v in enumerate(counts)) +
            f" L{px(n-1):.1f},{py(0):.1f} Z")
    out.append(f'<defs><linearGradient id="ag" x1="0" y1="0" x2="0" y2="1">'
               f'<stop offset="0%" stop-color="#7aa2f7" stop-opacity="0.35"/>'
               f'<stop offset="100%" stop-color="#7aa2f7" stop-opacity="0.02"/>'
               f'</linearGradient></defs>')
    out.append(f'<path d="{area}" fill="url(#ag)"/>')
    out.append(f'<polyline points="{line_pts}" fill="none" stroke="#7aa2f7" '
               f'stroke-width="1.5" stroke-linejoin="round"/>')

    # month labels
    prev = None
    for i, d in enumerate(dates):
        m = d[:7]
        if m != prev:
            out.append(f'<text x="{px(i):.1f}" y="{H-8}" font-size="8" '
                       f'fill="#565f89">{MONTHS[int(d[5:7])-1]}</text>')
            prev = m

    total = sum(counts)
    out.append(f'<text x="{W-pad_r}" y="20" font-size="10" fill="#565f89" '
               f'text-anchor="end">{total:,} total</text>')
    out.append('</svg>')
    return "\n".join(out)


# ---------------------------------------------------------------- main

def main():
    ASSETS.mkdir(exist_ok=True)
    print("fetching contributions calendar...")
    cells = fetch_contributions()
    print(f"  {len(cells)} cells")
    print("fetching user / repos / commits...")
    user = fetch_user()
    repos = fetch_repos()
    commits = fetch_commits()
    print(f"  repos={len(repos)} commits={commits} "
          f"followers={user.get('followers')}")

    files = {
        "stats.svg": build_stats(user, repos, commits),
        "langs.svg": build_langs(repos),
        "snake.svg": build_snake(cells, dark=True),
        "snake-light.svg": build_snake(cells, dark=False),
        "activity.svg": build_activity(cells),
    }
    for name, content in files.items():
        p = ASSETS / name
        p.write_text(content, encoding="utf-8")
        print(f"wrote assets/{name} ({len(content):,} bytes)")


if __name__ == "__main__":
    main()