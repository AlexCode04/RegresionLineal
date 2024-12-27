import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os

class RegressionService:
    def __init__(self, model_path="model.pkl"):
        self.model = LinearRegression()
        self.trained = False
        self.model_path = model_path
        self._load_model()

    def _load_model(self):
        """Carga el modelo entrenado desde un archivo."""
        if os.path.exists(self.model_path):
            self.model = joblib.load(self.model_path)
            self.trained = True

    def train(self, data: pd.DataFrame):
        """Entrena el modelo con un DataFrame."""
        X = data[["Precio", "Marketing", "Descuento"]]
        y = data["Ventas"]
        self.model.fit(X, y)
        self.trained = True
        joblib.dump(self.model, self.model_path)

    def predict(self, data: pd.DataFrame):
        """Realiza predicciones con el modelo entrenado."""
        if not self.trained:
            raise ValueError("El modelo no está entrenado.")
        predictions = self.model.predict(data)
        return predictions.tolist()
