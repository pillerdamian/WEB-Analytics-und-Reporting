import pandas as pd
from pathlib import Path
from typing import Union

def load_sales_file(path: Union[str, Path]) -> pd.DataFrame:
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"Datei nicht gefunden: {path}")

    suffix = path.suffix.lower()

    if suffix == ".csv":
        df = pd.read_csv(path)
    elif suffix in [".xlsx", ".xls"]:
        # Engine explizit angeben
        df = pd.read_excel(path, engine="openpyxl")
    else:
        raise ValueError(f"Nicht unterstütztes Dateiformat: {suffix}")

    if df.empty:
        raise ValueError("Datei enthält keine Daten")

    return df