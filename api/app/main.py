from fastapi import FastAPI

from .routes import router

app = FastAPI(title="Accident Gravity Prediction API")

app.include_router(router)
