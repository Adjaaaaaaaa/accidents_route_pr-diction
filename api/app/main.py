
from fastapi import FastAPI
from app.routes import router # Retirez le point "." si vous lancez depuis la racine /api

app = FastAPI(title="Accident Gravity Prediction API")

app.include_router(router)