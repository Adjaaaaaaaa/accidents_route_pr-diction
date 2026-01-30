from fastapi import APIRouter
from .models import InputData, OutputData
from .predictor import predict

router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "ok"}

@router.post("/predict", response_model=OutputData)
async def get_prediction(data: InputData):
    prediction = predict(data)
    return OutputData(prediction=prediction)
