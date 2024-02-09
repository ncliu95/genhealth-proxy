from pydantic import BaseModel, Field
from typing import List

class HistoryItem(BaseModel):
    code: str = Field(..., example="E11")
    system: str = Field(..., example="ICD10CM")
    display: str = Field(..., example="Type 2 diabetes mellitus")

class PredictRequest(BaseModel):
    history: List[HistoryItem] = Field(..., example=[
        {"code": "64", "system": "age", "display": "64"},
        {"code": "E11", "system": "ICD10CM", "display": "Type 2 diabetes mellitus"},
        {"code": "E11.3551", "system": "ICD10CM", "display": "Type 2 diabetes mellitus with stable proliferative diabetic retinopathy, right eye"}
    ])
    num_predictions: int = Field(..., example=1)
    generation_length: int = Field(..., example=10)
    inference_threshold: float = Field(..., example=0.95)
    inference_temperature: float = Field(..., example=0.95)
