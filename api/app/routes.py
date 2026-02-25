from fastapi import APIRouter, HTTPException

from .models import AccidentData, PredictionOutput
from .predictor import predictor

router = APIRouter()


@router.get("/health")
async def health_check():
    """Health check endpoint to verify API status and model loading."""
    return {"status": "ok", "model_loaded": True}


@router.post("/predict", response_model=PredictionOutput)
async def get_prediction(data: AccidentData):
    """Predict accident gravity from input data.

    Args:
        data (AccidentData): User input data for prediction

    Returns:
        PredictionOutput: Prediction results with gravity code, label and probabilities
    """
    try:
        # Call the predictor and return its result
        result = predictor.predict(data.dict())
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}") from e
