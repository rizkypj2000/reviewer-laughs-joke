"""Write one one-line joke about working beside AI coding agents to /output/entry.txt."""

from pathlib import Path

JOKE = (
    "My agent imported a package that didn't exist. "
    "By the time I'd finished reviewing the PR, it did."
)


def main() -> None:
    text = JOKE.strip()
    if not 1 <= len(text) <= 280:
        raise SystemExit(f"joke must be 1 to 280 characters, got {len(text)}")
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
