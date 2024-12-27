from pydantic import BaseModel

class DataPoint(BaseModel):
    Precio: float
    Marketing: float
    Descuento: float
    Ventas: float


class DataInput(BaseModel):
    data: list[DataPoint]
