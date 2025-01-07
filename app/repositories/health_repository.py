from datetime import datetime
from app.core.firebase import firebase

class HealthRepository:
    @staticmethod
    async def create_item(name: str):
        test_item = {
            "name": name,
            "created_at": datetime.utcnow()
        }
        doc_ref = firebase.db.collection('test_collection').document()
        doc_ref.set(test_item)
        test_item["id"] = doc_ref.id
        return test_item

    @staticmethod
    async def get_all_items():
        items = []
        docs = firebase.db.collection('test_collection').stream()
        for doc in docs:
            item = doc.to_dict()
            item["id"] = doc.id
            items.append(item)
        return items

