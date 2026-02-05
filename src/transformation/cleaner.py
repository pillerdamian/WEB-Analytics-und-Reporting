import pandas as pd

# Pflichtspalten für die Pipeline
REQUIRED_COLUMNS = {
    "date",
    "customer_id",
    "revenue",
    "converted",
}

# Mapping für alternative Spaltennamen (z. B. Excel/Deutsch/CRM-Exports)
COLUMN_MAPPING = {
    "datum": "date",
    "date": "date",

    "kunde": "customer_id",
    "kunden_id": "customer_id",
    "customer": "customer_id",
    "customer_id": "customer_id",

    "umsatz": "revenue",
    "revenue": "revenue",
    "sales": "revenue",

    "conversion": "converted",
    "converted": "converted",
    "gekauft": "converted",
}


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    # Spaltennamen normalisieren (lowercase, trim, underscores)
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # Mapping anwenden
    new_columns = {}
    for col in df.columns:
        if col in COLUMN_MAPPING:
            new_columns[col] = COLUMN_MAPPING[col]
        else:
            new_columns[col] = col  # unbekannte Spalten bleiben erhalten

    df = df.rename(columns=new_columns)
    return df


def validate_required_columns(df: pd.DataFrame):
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(
            f"Pflichtspalten fehlen in der Datei: {', '.join(sorted(missing))}"
        )


def clean_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    - Normalisiert und mappt Spaltennamen
    - Prüft, ob alle Pflichtspalten vorhanden sind
    - Konvertiert Datentypen
    - Entfernt ungültige Zeilen
    """

    # 1. Spalten normalisieren + mappen
    df = normalize_columns(df)

    # 2. Pflichtspalten prüfen
    validate_required_columns(df)

    # 3. Datentypen konvertieren
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce")
    df["customer_id"] = pd.to_numeric(df["customer_id"], errors="coerce")
    df["converted"] = pd.to_numeric(df["converted"], errors="coerce")

    # 4. Ungültige Zeilen entfernen
    df = df.dropna(subset=["date", "revenue", "customer_id", "converted"])

    return df