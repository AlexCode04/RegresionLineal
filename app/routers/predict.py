from fastapi import APIRouter, HTTPException
from app.services.regression_service import RegressionService
from app.helpers.Datamanage import validate_columns
import pandas as pd

router = APIRouter()
regression_service = RegressionService()

@router.post("/predict")
async def predict(data: dict):
    required_features = ["Precio", "Marketing", "Descuento"]
    try:
        df = pd.DataFrame(data["data"])
        validate_columns(df, set(required_features))
        predictions = regression_service.predict(df)
        return {"predictions": predictions}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


