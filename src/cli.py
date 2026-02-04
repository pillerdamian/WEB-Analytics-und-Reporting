import argparse
from ingestion.csv_loader import load_csv
from transformation.cleaner import clean_data
from analytics.kpis import calculate_kpis

def run_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("command")
    args = parser.parse_args()

    if args.command == "ingest":
        load_csv()
    elif args.command == "kpi":
        calculate_kpis()
