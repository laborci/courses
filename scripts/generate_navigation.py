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
    "    - navigation.tabs",
    "    - navigation.tabs.sticky",
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

courses = sorted(p for p in DOCS.iterdir() if p.is_dir() and p.name not in {"hu", "en", "int"})
for language_name, language_label, home_label, syllabus_label, week_label in [
    ("hu", "Magyar", "Kezdőlap", "Kurzusáttekintő", "hét"),
    ("en", "English", "Home", "Syllabus", "Week"),
]:
    language_home = DOCS / language_name / "index.md"
    if not language_home.is_file():
        continue
    lines += [f"  - {quoted(language_label)}:", f"      - {quoted(home_label)}: {language_name}/index.md"]
    for course in courses:
        language = course / language_name
        index = language / "index.md"
        if not index.is_file():
            continue
        lines += [f"      - {quoted(heading(index))}:", f"          - {quoted(home_label)}: {course.name}/{language_name}/index.md"]
        syllabus = language / "00-syllabus.md"
        short_titles: dict[str, str] = {}
        if syllabus.is_file():
            lines.append(f"          - {quoted(syllabus_label)}: {course.name}/{language_name}/00-syllabus.md")
            short_titles = {
                filename: label
                for label, filename in re.findall(
                    r"\[([^]]+)\]\(([0-9]{2}-[0-9]{2}-[^)]+\.md)\)",
                    syllabus.read_text(encoding="utf-8"),
                )
            }
        chapters = sorted(language.glob("[0-9][0-9]-[0-9][0-9]-*.md"))
        weeks: dict[str, list[Path]] = {}
        for chapter in chapters:
            if chapter.name[3:5] == "00":
                raise ValueError(f"Instructor presentation must not be published: {chapter}")
            weeks.setdefault(chapter.name[:2], []).append(chapter)
        for week, files in weeks.items():
            group = f"{week}. {week_label}" if language_name == "hu" else f"{week_label} {int(week)}"
            lines += [f"          - {quoted(group)}:"]
            for chapter in files:
                label = short_titles.get(chapter.name, heading(chapter))
                lines.append(f"              - {quoted(label)}: {course.name}/{language_name}/{chapter.name}")

(ROOT / "mkdocs.yml").write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"Generated language-first navigation for {len(courses)} course(s).")
