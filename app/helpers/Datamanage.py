import json
import pandas as pd
from pathlib import Path

DATA_FILE = "training_data.json"

def load_training_data() -> pd.DataFrame:
    """Carga los datos de entrenamiento desde un archivo JSON."""
    if not Path(DATA_FILE).exists() or Path(DATA_FILE).stat().st_size == 0:
        return pd.DataFrame()
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
    return pd.DataFrame(data)

def save_training_data(new_data: pd.DataFrame):
    """Guarda datos nuevos en el archivo JSON sin duplicados."""
    existing_data = load_training_data()
    combined_data = pd.concat([existing_data, new_data]).drop_duplicates()
    combined_data.to_json(DATA_FILE, orient="records", indent=4)

def validate_columns(data: pd.DataFrame, required_columns: set):
    """Valida que un DataFrame tenga las columnas requeridas."""
    missing_columns = required_columns - set(data.columns)
    if missing_columns:
        raise ValueError(f"Faltan las siguientes columnas requeridas: {', '.join(missing_columns)}")
