from pathlib import Path
from datetime import datetime

ARCHIVE_DIR = Path(__file__).resolve().parent / "archive"


def archive_entry(raw_text: str, entry_date: str) -> Path:
    """
    Speichert den Original-Text in den archive-Ordner.
    """

    ARCHIVE_DIR.mkdir(exist_ok=True)

    file_path = ARCHIVE_DIR / f"{entry_date}.txt"

    if file_path.exists():
        timestamp = datetime.now().strftime("%H-%M-%S-%f")
        file_path = ARCHIVE_DIR / f"{entry_date}_{timestamp}.txt"
        suffix = 1
        while file_path.exists():
            file_path = ARCHIVE_DIR / f"{entry_date}_{timestamp}_{suffix}.txt"
            suffix += 1

    file_path.write_text(raw_text.strip() + "\n", encoding="utf-8")

    return file_path
