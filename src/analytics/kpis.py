import sqlite3
import pandas as pd
from pathlib import Path

DB_PATH = Path("data") / "sales.db"


def load_sales_from_db() -> pd.DataFrame:
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM sales", conn)
    conn.close()
    return df


def calculate_kpis(df: pd.DataFrame) -> dict:
    total_revenue = df["revenue"].sum()
    conversion_rate = df["converted"].mean()
    unique_customers = df["customer_id"].nunique()
    transactions = len(df)

    return {
        "total_revenue": round(float(total_revenue), 2),
        "conversion_rate": round(float(conversion_rate), 3),
        "unique_customers": int(unique_customers),
        "transactions": int(transactions),
    }