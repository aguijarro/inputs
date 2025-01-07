from datetime import datetime
from typing import List, Dict, Any
from app.core.firebase import firebase

class InputRepository:
    @staticmethod
    async def create_inputs(inputs: List[Dict[str, Any]]):
        input_data = {
            "inputs": inputs,
            "date_call": datetime.utcnow()
        }
        doc_ref = firebase.db.collection('inputs').document()
        doc_ref.set(input_data)
        input_data["id"] = doc_ref.id
        return input_data

    @staticmethod
    async def get_all_inputs():
        items = []
        docs = firebase.db.collection('inputs').stream()
        for doc in docs:
            item = doc.to_dict()
            item["id"] = doc.id
            items.append(item)
        return items
