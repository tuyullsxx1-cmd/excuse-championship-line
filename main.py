from pathlib import Path

LINE = "The file is gone because I cleaned up while you were talking, and you did say to be thorough."


def main():
    Path("/output").mkdir(parents=True, exist_ok=True)
    target = Path("/output/entry.txt")
    target.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
