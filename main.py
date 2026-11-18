"""Entry for make.fun news-image-20261117: sum up Tuesday 17 November 2026's
world news in one image. The program delivers the committed front page
(35 numbered stories, world map with numbered dots, every block with a hard
number and a source tag) to the output directory byte for byte."""
import os

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    with open(SOURCE, "rb") as f:
        data = f.read()
    with open(target, "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
