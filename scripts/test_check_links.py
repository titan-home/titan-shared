"""Tests for check_links.py."""

import tempfile
import unittest
from pathlib import Path

from check_links import anchor, broken_links


class CheckLinksTest(unittest.TestCase):
    def test_anchor_matches_github(self) -> None:
        self.assertEqual(anchor("1. Node and platform"), "1-node-and-platform")
        self.assertEqual(anchor("The owner's role [v1]"), "the-owners-role-v1")
        self.assertEqual(anchor("Plugin trust (#9)"), "plugin-trust-9")

    def test_finds_missing_files_and_headings(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "other.md").write_text("# Title\n\n## Title\n")
            page = root / "page.md"
            page.write_text(
                "# Top\n"
                "[ok](other.md#title-1) [ok](#top) [ok](https://example.com/x.md)\n"
                "[bad](missing.md) [bad](other.md#title-2) [bad](#nowhere)\n"
                "`[skipped](inline.md)`\n"
                "```\n[skipped](fenced.md)\n```\n"
            )
            self.assertEqual(
                broken_links(page), ["missing.md", "other.md#title-2", "#nowhere"]
            )


if __name__ == "__main__":
    unittest.main()
