import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().with_name("journal_data.json")


def load_entries() -> list:
    """
    Lädt alle vorhandenen Journal-Einträge aus der JSON-Datei.
    Wenn die Datei noch nicht existiert, wird eine leere Liste zurückgegeben.
    """
    if not DATA_FILE.exists():
        return []

    return json.loads(DATA_FILE.read_text(encoding="utf-8"))


def save_entries(entries: list) -> None:
    """
    Speichert alle Journal-Einträge in der JSON-Datei.
    """
    temporary_file = DATA_FILE.with_suffix(DATA_FILE.suffix + ".tmp")
    temporary_file.write_text(
        json.dumps(entries, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    temporary_file.replace(DATA_FILE)


def upsert_entry(entries: list, new_entry: dict) -> list:
    """
    Fügt einen neuen Eintrag hinzu oder ersetzt einen vorhandenen Eintrag
    mit demselben Datum.
    """
    entry_map = {entry["Datum"]: entry for entry in entries}
    entry_map[new_entry["Datum"]] = new_entry

    return sorted(entry_map.values(), key=lambda x: x["Datum"])
