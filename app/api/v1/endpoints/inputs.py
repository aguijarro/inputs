from fastapi import APIRouter, Body
from typing import List, Dict, Any
from app.repositories.input_repository import InputRepository

router = APIRouter()

@router.post("/inputs")
async def create_inputs(inputs: List[Dict[str, Any]] = Body(...)):
    return await InputRepository.create_inputs(inputs)

@router.get("/inputs")
async def get_inputs():
    return await InputRepository.get_all_inputs()
