from pathlib import Path

from analysis import (
    average_score,
    best_day,
    most_common_trigger,
    strongest_days_of_week,
    weakest_days_of_week,
    worst_day,
)
from archive import archive_entry
from parser import parse_entry
from plotting import plot_scores, plot_triggers
from storage import load_entries, save_entries, upsert_entry


BASE_DIR = Path(__file__).resolve().parent


def main() -> None:
    raw_text = (BASE_DIR / "heute.txt").read_text(encoding="utf-8")
    entry = parse_entry(raw_text)

    entries = upsert_entry(load_entries(), entry)
    save_entries(entries)

    print("Eintrag erfolgreich gespeichert.\n")
    for saved_entry in entries:
        print("-" * 30)
        for key, value in saved_entry.items():
            print(f"{key}: {value}")

    archive_path = archive_entry(raw_text, entry["Datum"])
    print(f"\nArchiv gespeichert unter: {archive_path}")

    print("\n--- ANALYSE ---")
    print(f"Durchschnittlicher Score: {average_score(entries):.2f}")
    print(f"Häufigster Trigger: {most_common_trigger(entries)}")

    strongest = best_day(entries)
    weakest = worst_day(entries)
    if strongest:
        print(f"Stärkster Tag: {strongest['Datum']} ({strongest['Score']})")
    if weakest:
        print(f"Schwächster Tag: {weakest['Datum']} ({weakest['Score']})")

    week = (entry["ISO_Jahr"], entry["ISO_Woche"])
    strongest_week = strongest_days_of_week(entries, *week)
    weakest_week = weakest_days_of_week(entries, *week)
    print(f"\n--- WOCHE {entry['ISO_Woche']} ---")
    print("Stärkste Tage der Woche:")
    for day in strongest_week:
        print(f"- {day['Datum']} | Score: {day['Score']} | Zustand: {day['Zustand']}")
    print("Schwächste Tage der Woche:")
    for day in weakest_week:
        print(f"- {day['Datum']} | Score: {day['Score']} | Zustand: {day['Zustand']}")

    plot_scores(entries)
    plot_triggers(entries)


if __name__ == "__main__":
    main()
