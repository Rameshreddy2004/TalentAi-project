from fastapi import APIRouter
from db import results_collection
from datetime import datetime

router = APIRouter()

@router.post("/save-result")
async def save_result(data: dict):
    data["created_at"] = datetime.now()
    results_collection.insert_one(data)
    return {"message": "Result saved successfully!"}
