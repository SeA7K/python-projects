# Python Projekte

Eigene Python-Projekte im Rahmen des Lernpfads.

## Projekte

### Journal-System

Persönliches Journal-System mit Analyse und Visualisierung.

### Journal-System starten

1. Python 3.10 oder neuer installieren.
2. `pip install -r requirements.txt` ausführen.
3. `heute.txt` im Projektordner mit einem Eintrag nach diesem Muster anlegen:

```text
Datum: 2026-09-24
Zustand: klar
Erledigt: Ja
Fokus: 7
Trigger: Handy
Abweichung: zu oft aufs Handy geschaut
```

4. `python main.py` starten. `journal_data.json` wird beim Speichern automatisch
erstellt. Einträge, Tagesnotiz, Archiv und Diagramme bleiben lokal.

Dateien: `main.py` (Hauptprogramm), `analysis.py` (Auswertung), `plotting.py`
(Diagramme), `storage.py` (Datenspeicherung) und `parser.py` (Eingabeverarbeitung).

## Kommende Projekte

- Netzwerk-Scanner
- Bash-Automatisierungen
- CTF-Hilfstools
