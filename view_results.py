from fastapi import APIRouter
from db import results_collection
from bson import ObjectId

router = APIRouter()

@router.get("/admin/all-results")
async def get_all_results():
    results = list(results_collection.find({}, {"chat_history": 0}))
    for r in results:
        r["_id"] = str(r["_id"])
    return results

@router.get("/admin/result/{id}")
async def get_single_result(id: str):
    result = results_collection.find_one({"_id": ObjectId(id)})
    result["_id"] = str(result["_id"])
    return result
