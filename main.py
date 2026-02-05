from src.ingestion.csv_loader import load_sales_file
from src.transformation.cleaner import clean_sales_data
from src.database.db import Database
from src.analytics.kpis import load_sales_from_db, calculate_kpis
from src.reporting.html_report import generate_html_report

def main():
    # 1. CSV laden
    df_raw = load_sales_file("data/raw/sales.csv")

    # 2. Daten bereinigen
    df_clean = clean_sales_data(df_raw)

    # 3. In Datenbank speichern
    db = Database()
    db.connect()
    db.create_sales_table()
    db.insert_sales_dataframe(df_clean)
    db.close()

    # 4. KPIs generieren
    df = load_sales_from_db()
    kpis = calculate_kpis(df)

    # 5. HTML-Report erstellen
    report_path = generate_html_report(kpis)
    print("Report erstellt:", report_path)

if __name__ == "__main__":
    main()
