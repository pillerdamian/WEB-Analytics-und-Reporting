# Local Business Intelligence Analytics Tool (Python)

## 🎯 Ziel des Projekts

Dieses Projekt ist ein **lokal ausführbares Business-Intelligence-Tool** zur automatisierten Auswertung von Unternehmens- bzw. Vertriebsdaten.  
Es ersetzt manuelle Excel-basierte Analysen durch eine **reproduzierbare, programmatische Datenpipeline**.

Der Fokus liegt auf:
- sauberer Architektur
- klarer Trennung der Verantwortlichkeiten (Ingestion, Transformation, Persistenz, Analytics, Reporting)
- Automatisierung statt manueller Auswertung
- lokaler Ausführung ohne Webserver oder externe Kosten

---

## 📥 Unterstützte Dateiformate

✅ Aktuell werden **ausschließlich CSV-Dateien (`.csv`)** unterstützt.

Die CSV-Datei muss mindestens folgende Spalten enthalten:

- `date` – Datum
- `customer_id` – Kunden-ID
- `revenue` – Umsatz
- `converted` – 0 oder 1 (Conversion-Indikator)

Andere Formate (z. B. Excel `.xlsx`) sind **bewusst nicht aktiviert**, um die Pipeline einfach, stabil und reproduzierbar zu halten.

---

## 🧠 Architektur-Überblick

Die Anwendung ist in klar getrennte Schichten aufgebaut:

```text
Ingestion (CSV Import)
   ↓
Transformation (Datenbereinigung & Normalisierung)
   ↓
Persistence (SQLite als lokale Datenbank)
   ↓
Analytics (KPI-Berechnung)
   ↓
Reporting (HTML-Report)
