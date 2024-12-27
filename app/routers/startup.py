from fastapi import APIRouter, HTTPException
from app.services.regression_service import RegressionService
from app.helpers.Datamanage import load_training_data

startupRouter = APIRouter()
RegressionService = RegressionService()

@startupRouter.on_event("startup")
async def startup_event():
    """Carga los datos de entrenamiento y entrena el modelo al iniciar el servidor."""
    training_data = load_training_data()
    if not training_data.empty:
        RegressionService.train(training_data)