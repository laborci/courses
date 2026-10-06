#!/usr/bin/env python3
"""Generate the MkDocs navigation from published student chapters."""

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


def quoted(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def heading(path: Path) -> str:
    match = re.search(r"(?m)^# (.+)$", path.read_text(encoding="utf-8"))
    if not match:
        raise ValueError(f"Missing H1: {path}")
    return match.group(1)


lines = [
    "site_name: Tananyagok",
    "site_description: Egyetemi tananyagok heti bontásban",
    "site_url: https://laborci.github.io/courses/",
    "repo_url: https://github.com/laborci/courses",
    "use_directory_urls: true",
    "theme:",
    "  name: material",
    "  language: hu",
    "  features:",
    "    - navigation.sections",
    "    - navigation.top",
    "    - navigation.path",
    "    - search.suggest",
    "    - search.highlight",
    "  palette:",
    "    - media: '(prefers-color-scheme: light)'",
    "      scheme: default",
    "      toggle:",
    "        icon: material/brightness-7",
    "        name: Sötét mód",
    "    - media: '(prefers-color-scheme: dark)'",
    "      scheme: slate",
    "      toggle:",
    "        icon: material/brightness-4",
    "        name: Világos mód",
    "plugins:",
    "  - search",
    "markdown_extensions:",
    "  - admonition",
    "  - pymdownx.details",
    "  - pymdownx.superfences:",
    "      custom_fences:",
    "        - name: mermaid",
    "          class: mermaid",
    "          format: !!python/name:pymdownx.superfences.fence_code_format",
    "nav:",
    "  - Kezdőlap: index.md",
]

for course in sorted(p for p in DOCS.iterdir() if p.is_dir()):
    index = course / "index.md"
    if not index.is_file():
        raise ValueError(f"Missing course index: {index}")
    lines += [f"  - {quoted(heading(index))}:", f"      - Áttekintés: {course.name}/index.md"]
    for language in sorted(p for p in course.iterdir() if p.is_dir()):
        label = {"hu": "Magyar tananyag", "en": "English materials", "int": "International materials"}.get(language.name, language.name)
        lines += [f"      - {quoted(label)}:"]
        for name, label in [("index.md", "Kezdőlap"), ("00-syllabus.md", "Kurzusáttekintő")]:
            if (language / name).is_file():
                lines.append(f"          - {quoted(label)}: {course.name}/{language.name}/{name}")
        chapters = sorted(language.glob("[0-9][0-9]-[0-9][0-9]-*.md"))
        weeks: dict[str, list[Path]] = {}
        for chapter in chapters:
            if chapter.name[3:5] == "00":
                raise ValueError(f"Instructor presentation must not be published: {chapter}")
            weeks.setdefault(chapter.name[:2], []).append(chapter)
        for week, files in weeks.items():
            lines += [f"          - {quoted(week + '. hét')}:"]
            for chapter in files:
                lines.append(
                    f"              - {quoted(heading(chapter))}: "
                    f"{course.name}/{language.name}/{chapter.name}"
                )

(ROOT / "mkdocs.yml").write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"Generated navigation for {sum(1 for p in DOCS.iterdir() if p.is_dir())} course(s).")
