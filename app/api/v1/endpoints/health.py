from fastapi import APIRouter
from app.repositories.health_repository import HealthRepository
from pydantic import BaseModel

router = APIRouter()

class HealthItem(BaseModel):
    name: str

@router.get("/health")
async def health_check():
    return {"status": "ok"}

@router.post("/health_db")
async def create_db_row(item: HealthItem):
    return await HealthRepository.create_item(item.name)

@router.get("/health_db")
async def read_db_rows():
    return await HealthRepository.get_all_items()       

