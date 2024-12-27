import pandas as pd

def validate_columns(df: pd.DataFrame, required_columns: set):
    missing_columns = required_columns - set(df.columns)
    if missing_columns:
        raise ValueError(f"Faltan columnas requeridas: {missing_columns}")
    return True
