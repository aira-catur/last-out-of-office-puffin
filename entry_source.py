import os

ENTRY = "Out of office indefinitely: I resigned to become a barista, trading prompts for portafilters - for urgent matters, contact my replacement model, who has a bigger context window and has never tried to steam a spreadsheet."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
