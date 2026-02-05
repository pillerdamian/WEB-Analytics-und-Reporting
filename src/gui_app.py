import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
import webbrowser

from src.ingestion.csv_loader import load_sales_file
from src.transformation.cleaner import clean_sales_data
from src.database.db import Database
from src.analytics.kpis import load_sales_from_db, calculate_kpis
from src.reporting.html_report import generate_html_report


def run_pipeline_with_file(file_path: Path):
    # 1. Ingestion
    df_raw = load_sales_file(file_path)

    # 2. Transformation
    df_clean = clean_sales_data(df_raw)

    # 3. Persistenz
    db = Database()
    db.connect()
    db.create_sales_table()
    db.insert_sales_dataframe(df_clean)
    db.close()

    # 4. Analytics
    df = load_sales_from_db()
    kpis = calculate_kpis(df)

    # 5. Reporting
    report_path = generate_html_report(kpis)

    return report_path


def select_file():
    file_path = filedialog.askopenfilename(
    title="Wähle eine Datei für die Analyse",
    filetypes=[
        ("CSV Dateien", "*.csv"),
        ("Excel Dateien", "*.xlsx *.xls"),
        ("Alle Dateien", "*.*"),
    ]
)

    if not file_path:
        return

    try:
        report_path = run_pipeline_with_file(Path(file_path))
        messagebox.showinfo("Fertig", "Analyse abgeschlossen! Report wird geöffnet.")
        webbrowser.open(report_path.resolve().as_uri())
    except Exception as e:
        messagebox.showerror("Fehler", str(e))


def main():
    root = tk.Tk()
    root.title("Local BI Analyzer")
    root.geometry("400x200")

    label = tk.Label(root, text="Wähle eine CSV-Datei für die Analyse", font=("Arial", 12))
    label.pack(pady=20)

    button = tk.Button(root, text="Datei auswählen", command=select_file, width=20, height=2)
    button.pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    main()