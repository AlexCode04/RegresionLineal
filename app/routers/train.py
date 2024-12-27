from fastapi import APIRouter, HTTPException
from app.models.data_models import DataInput
from app.services.regression_service import RegressionService
from app.helpers.dataframe_helper import validate_columns
from app.helpers.Datamanage import save_training_data
import pandas as pd

router = APIRouter()
regression_service = RegressionService()

DATA_FILE = "training_data.json"

@router.post("/train")
async def train_model(input_data: DataInput):
    df = pd.DataFrame([item.dict() for item in input_data.data])

    # Validar las columnas requeridas
    required_columns = {"Precio", "Marketing", "Descuento", "Ventas"}
    try:
        validate_columns(df, required_columns)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    # Guardar los datos y entrenar el modelo
    save_training_data(df)
    regression_service.train(df)

    return {"message": "Modelo entrenado con éxito y datos guardados."}


