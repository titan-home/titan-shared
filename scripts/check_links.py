"""Check that every relative link in the Markdown files points to a file and heading that exist."""

import re
import sys
from pathlib import Path

# NOTE: matches one line at a time, so a link whose text wraps onto the next
# line is not checked; join each paragraph into one line when that happens.
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
HEADING = re.compile(r"^#{1,6}\s+(.*?)\s*#*\s*$")
SKIPPED_DIRECTORIES = {"shared", "node_modules"}


def lines_outside_code(text: str) -> list[str]:
    """Return the lines that are not inside fenced code blocks, with inline code removed."""
    lines, fenced = [], False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            fenced = not fenced
        elif not fenced:
            lines.append(re.sub(r"`[^`]*`", "", line))
    return lines


def anchor(heading: str) -> str:
    """Turn a heading into its anchor the way GitHub does."""
    heading = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", heading)
    return re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")


def anchors(path: Path) -> set[str]:
    """Return every heading anchor of a Markdown file, numbering repeats as GitHub does."""
    found: set[str] = set()
    for line in lines_outside_code(path.read_text(encoding="utf-8")):
        match = HEADING.match(line)
        if match:
            base = name = anchor(match.group(1))
            number = 0
            while name in found:
                number += 1
                name = f"{base}-{number}"
            found.add(name)
    return found


def broken_links(path: Path) -> list[str]:
    """Return the relative links in one Markdown file whose file or heading does not exist."""
    broken = []
    for line in lines_outside_code(path.read_text(encoding="utf-8")):
        for target in LINK.findall(line):
            if re.match(r"^[a-z][a-z0-9+.-]*:", target):
                continue  # http, mailto, titan:// and other absolute links
            file_part, _, fragment = target.partition("#")
            linked = (path.parent / file_part).resolve() if file_part else path
            if not linked.exists():
                broken.append(target)
            elif fragment and linked.suffix == ".md" and fragment not in anchors(linked):
                broken.append(target)
    return broken


def markdown_files(root: Path) -> list[Path]:
    """Return the Markdown files under root, skipping hidden folders and the shared submodule."""
    return sorted(
        path
        for path in root.rglob("*.md")
        if not any(
            part.startswith(".") or part in SKIPPED_DIRECTORIES
            for part in path.relative_to(root).parts[:-1]
        )
    )


def main() -> int:
    """Print every broken link under the folder given as the argument and fail if there is one."""
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    failed = False
    for path in markdown_files(root):
        for target in broken_links(path):
            print(f"{path.relative_to(root)}: broken link {target}")
            failed = True
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
