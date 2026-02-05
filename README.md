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

Die CSV-Datei muss inhaltlich folgende Informationen enthalten (Spaltennamen können gemappt werden, siehe unten):

- `date` – Datum
- `customer_id` – Kunden-ID
- `revenue` – Umsatz
- `converted` – 0 oder 1 (Conversion-Indikator)

Andere Formate (z. B. Excel `.xlsx`) sind **bewusst nicht aktiviert**, um die Pipeline einfach, stabil und reproduzierbar zu halten.

---

## 🔎 Spalten-Mapping & Validierung

### ✅ Spalten-Mapping

Die Pipeline unterstützt automatisch alternative Spaltennamen, z. B.:

- `Datum` → `date`
- `Kunde`, `Kunden_ID` → `customer_id`
- `Umsatz`, `Sales` → `revenue`
- `Gekauft`, `Conversion` → `converted`

Zusätzliche Spalten in der CSV sind **kein Problem** und werden einfach ignoriert, solange die benötigten Pflichtspalten vorhanden sind.

---

### ❌ Pflichtspalten-Prüfung

Vor der Verarbeitung wird geprüft, ob alle notwendigen Spalten vorhanden sind.  
Fehlen eine oder mehrere Pflichtspalten, bricht die Pipeline mit einer **klaren Fehlermeldung** ab.

#Readme is written by ChatGPT