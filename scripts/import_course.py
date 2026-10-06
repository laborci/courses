#!/usr/bin/env python3
"""Import only student-facing Hungarian course Markdown into the public site."""

import argparse
import re
import subprocess
import sys
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Local hu/ directory")
    parser.add_argument("slug", help="Course URL segment")
    parser.add_argument("--title", required=True, help="Hungarian course title")
    args = parser.parse_args()

    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", args.slug):
        parser.error("slug must use lowercase letters, digits and hyphens")
    source = args.source.resolve()
    syllabus = source / "00-syllabus.md"
    if not syllabus.is_file():
        parser.error(f"missing syllabus: {syllabus}")

    destination = Path(__file__).resolve().parents[1] / "docs" / args.slug / "hu"
    destination.mkdir(parents=True, exist_ok=True)
    chapters = sorted(
        f for f in source.glob("[0-9][0-9]-[0-9][0-9]-*.md")
        if f.name[3:5] != "00"
    )
    if not chapters:
        parser.error("no student chapters found")

    syllabus_text = syllabus.read_text(encoding="utf-8")
    syllabus_text = re.sub(
        r"(?m)^\[[^\n]*oktatói prezentációja\]\([0-9]{2}-00-[^)]+\.md\)\n?",
        "",
        syllabus_text,
    )
    (destination / "00-syllabus.md").write_text(syllabus_text, encoding="utf-8")
    for chapter in chapters:
        (destination / chapter.name).write_bytes(chapter.read_bytes())

    weeks: dict[str, list[tuple[str, str]]] = {}
    for chapter in chapters:
        match = re.match(r"([0-9]{2})-[0-9]{2}-", chapter.name)
        assert match
        title_match = re.search(r"(?m)^# (.+)$", chapter.read_text(encoding="utf-8"))
        if not title_match:
            parser.error(f"missing H1: {chapter}")
        weeks.setdefault(match.group(1), []).append((title_match.group(1), chapter.name))

    index = [f"# {args.title}", "", "[A kurzus áttekintése](00-syllabus.md)", ""]
    for week, entries in weeks.items():
        index += [f"## {week}. hét", ""]
        index += [f"- [{title}]({name})" for title, name in entries]
        index += [""]
    (destination / "index.md").write_text("\n".join(index), encoding="utf-8")
    course_index = destination.parent / "index.md"
    course_index.write_text(
        f"# {args.title}\n\n[Magyar tananyag](hu/index.md)\n",
        encoding="utf-8",
    )
    subprocess.run([sys.executable, str(Path(__file__).with_name("generate_navigation.py"))], check=True)
    print(f"Imported {len(chapters)} chapters into {destination}")


if __name__ == "__main__":
    main()
