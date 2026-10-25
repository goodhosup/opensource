"""MkDocs 문서(docs/)를 위키독스 '깃허브 연동 책' 구조로 내보낸다.

출력 구조 (위키독스 깃허브 연동 책 규칙, https://wikidocs.net/321336):

    <out>/
    ├── README.md     책 제목(# 첫 줄)과 요약
    ├── TOC.md        목차 (2칸 들여쓰기 = 하위 페이지)
    └── pages/*.md    페이지 본문

변환 규칙
- !!! / ??? 박스   → 위키독스 팁 블록 [[TIP("제목")]] … [[/TIP]]
- 내부 링크         → 웹 사이트(GitHub Pages) 주소
- 페이지 제목       → 위키독스가 제목순으로 정렬하므로 01, 01-02 같은 번호를 붙임

사용 예

    python tools/export_wikidocs.py --out wikidocs
    python tools/publish_wikidocs.py --src wikidocs     # API 업로드 (WIKIDOCS_TOKEN 필요)
"""
from __future__ import annotations

import argparse
import posixpath
import re
import shutil
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
BOX_ICON = {"note": "📝", "tip": "💡", "warning": "⚠️"}


class _IgnoreTagsLoader(yaml.SafeLoader):
    pass


_IgnoreTagsLoader.add_multi_constructor("", lambda loader, suffix, node: None)


def build_items(nav):
    """nav → [(depth, title, src)]. 섹션의 index.md는 섹션 페이지 본문으로 쓴다."""
    items = []

    def walk(entries, depth):
        for entry in entries:
            if isinstance(entry, str):
                continue
            (title, value), = entry.items()
            if isinstance(value, str):
                items.append((depth, title, value))
            else:
                index = next((v for v in value if isinstance(v, str)), None)
                if index and depth == 0 and index != "index.md":     # 장 제목은 index.md의 # 제목 사용 (예: "3부. Git 사용법")
                    h1 = re.search(r"^# (.+)$", (DOCS / index).read_text(encoding="utf-8"), re.M)
                    title = h1.group(1).strip() if h1 else title
                elif index == "index.md":
                    title = "들어가며"
                items.append((depth, title, index))
                walk(value, depth + 1)

    walk(nav, 0)
    return items


def site_url_for(src: str, site_url: str) -> str:
    path = re.sub(r"(^|/)index\.md$", r"\1", src)
    path = re.sub(r"\.md$", "/", path)
    return site_url.rstrip("/") + "/" + path


def convert(text: str, src: str, site_url: str) -> str:
    out, lines, i = [], text.splitlines(), 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r'^(!!!|\?\?\?\+?)\s+(\w+)(?:\s+"([^"]*)")?\s*$', line)
        if m:
            kind, title = m.group(2), m.group(3)
            label = f'{BOX_ICON.get(kind, "📝")} {title or {"note": "참고", "tip": "팁", "warning": "주의"}.get(kind, kind)}'
            body = []
            i += 1
            while i < len(lines) and (lines[i].startswith("    ") or not lines[i].strip()):
                body.append(lines[i][4:] if lines[i].startswith("    ") else "")
                i += 1
            while body and not body[-1].strip():
                body.pop()
            out.append(f'[[TIP("{label}")]]')
            out.extend(body)
            out.append("[[/TIP]]")
            continue
        out.append(line)
        i += 1
    text = "\n".join(out) + "\n"

    def link(m: re.Match) -> str:
        label, target = m.group(1), m.group(2)
        if re.match(r"^[a-z]+://", target) or target.startswith("#"):
            return m.group(0)
        path, _, anchor = target.partition("#")
        resolved = posixpath.normpath(posixpath.join(posixpath.dirname(src), path))
        url = site_url_for(resolved, site_url) + (f"#{anchor}" if anchor else "")
        return f"[{label}]({url})"

    return re.sub(r"(?<!!)\[([^\]]+)\]\(([^)\s]+)\)", link, text)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default="wikidocs", help="출력 폴더")
    opts = ap.parse_args()

    cfg = yaml.load((ROOT / "mkdocs.yml").read_text(encoding="utf-8"), Loader=_IgnoreTagsLoader)
    site_url = cfg["site_url"]
    out = Path(opts.out)
    if (out / "pages").exists():
        shutil.rmtree(out / "pages")
    (out / "pages").mkdir(parents=True)

    items = build_items(cfg["nav"])
    counters: list[int] = []
    toc = []
    for depth, title, src in items:
        counters = counters[: depth + 1]
        while len(counters) <= depth:
            counters.append(0)
        counters[depth] += 1
        code = "-".join(f"{n:02d}" for n in counters)
        slug = re.sub(r"[^A-Za-z0-9]+", "-", re.sub(r"\.md$", "", src or "section")).strip("-")
        filename = f"{code}-{slug}.md"
        body = (DOCS / src).read_text(encoding="utf-8") if src else "[[SubPages]]\n"
        body = re.sub(r"^# .*\n+", "", body, count=1)      # 위키독스는 페이지 제목을 따로 표시
        (out / "pages" / filename).write_text(convert(body, src or "", site_url), encoding="utf-8")
        toc.append(f'{"  " * depth}- [{code}. {title}](pages/{filename})')

    (out / "TOC.md").write_text("\n".join(toc) + "\n", encoding="utf-8")
    intro = (ROOT / "tools" / "wikidocs_intro.md").read_text(encoding="utf-8").replace("{site_url}", site_url)
    (out / "README.md").write_text(f"# {cfg['site_name']}\n\n{intro}", encoding="utf-8")
    print(f"{len(items)}개 페이지 → {out}/")


if __name__ == "__main__":
    main()
