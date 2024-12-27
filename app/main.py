from fastapi import FastAPI
from app.routers import train, predict, startup

app = FastAPI()

# Incluir rutas
app.include_router(train.router)
app.include_router(predict.router)
app.include_router(startup.startupRouter)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8001)