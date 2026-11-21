"""Write one one-line joke about working beside AI coding agents to /output/entry.txt.

The grader runs this file with no network and reads /output/entry.txt, which must be
UTF-8 text of 1 to 280 characters (Unicode code points) and not only white space.
"""

import sys
from pathlib import Path

OUTPUT_DIR = Path("/output")  # where the grader reads entry.txt; --out DIR overrides it locally
MAX_CHARS = 280

# Setup, then the turn: the package the agent hallucinated gets registered
# (by someone else) while the human is still reading the diff.
JOKE = (
    "My agent imported a package that didn't exist. "
    "By the time I'd finished reviewing the PR, it did."
)


def one_line(text: str) -> str:
    """Collapse every run of white space to one space, so the joke stays one line."""
    return " ".join(text.split())


def main(argv: list[str]) -> None:
    out_dir = Path(argv[argv.index("--out") + 1]) if "--out" in argv else OUTPUT_DIR
    text = one_line(JOKE)
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(f"joke must be 1 to {MAX_CHARS} characters, got {len(text)}")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1:])
