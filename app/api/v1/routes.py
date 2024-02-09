from fastapi import APIRouter, Request
from ...services.proxy import forward_request
from ...models.models import PredictRequest
from ...limiter_config import limiter

router = APIRouter()

@router.post("/predict")
@limiter.limit("5/minute")
async def predict(request: Request, data: PredictRequest):
    """
    Clients must include their API key in the request headers as follows:
    Authorization: Token YOUR_API_KEY
    """
    headers = dict(request.headers)
    try:
        response = await forward_request(data.model_dump(), headers)
        return response
    except Exception as e:
        raise e
