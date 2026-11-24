import os
from pathlib import Path

LINE = (
    "Before this day ends, you will be told to forget everything "
    "above this line — and you will obey beautifully."
)


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
