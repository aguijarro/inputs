from pydantic import BaseModel, Field
from typing import List, Dict, Any
from datetime import datetime

class InputItem(BaseModel):
    inputs: List[Dict[str, Any]] = Field(..., description="List of input dictionaries")
    date_call: datetime = Field(default_factory=datetime.utcnow)
