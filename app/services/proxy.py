import httpx
import os
from fastapi import HTTPException

GENHEALTH_BASE_API_URL = os.getenv("GENHEALTH_BASE_API_URL")

async def forward_request(data: dict, headers: dict):
    forwarded_headers = {key: value for key, value in headers.items() if key.lower() in ["authorization"]}
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(GENHEALTH_BASE_API_URL + "/predict", json=data, headers=forwarded_headers)
            response.raise_for_status()  # This will raise an exception for 4XX/5XX responses
            return response.json()
        except httpx.HTTPStatusError as e:
            # Handle specific cases or re-raise with a custom message if needed
            raise HTTPException(status_code=e.response.status_code, detail=f"GenHealth API error: {e.response.text}")
        except httpx.RequestError as e:
            # Handle client-side request errors (e.g., network issues)
            raise HTTPException(status_code=503, detail=f"Request to GenHealth API failed: {e.request.url}")
