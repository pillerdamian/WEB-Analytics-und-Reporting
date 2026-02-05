import sqlite3
from pathlib import Path
import pandas as pd

DB_PATH = Path("data") / "sales.db"

class Database:
    def __init__(self, db_path: Path = DB_PATH):
        self.db_path = db_path
        self.conn = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_path)
        return self.conn

    def close(self):
        if self.conn:
            self.conn.close()

    def create_sales_table(self):
        with self.connect() as conn:
            query = """
            CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                customer_id INTEGER,
                revenue REAL,
                converted INTEGER
            ); """

            self.conn.execute(query)
            self.conn.commit()

    def insert_sales_dataframe(self, df: pd.DataFrame):
        df.to_sql("sales", self.conn, if_exists="append", index=False)