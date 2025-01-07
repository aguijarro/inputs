from firebase_admin import credentials, initialize_app, firestore
import os
import json
import base64
from app.core.config import settings

class Firebase:
    def __init__(self):
        self.db = None
        self.client = None

    async def connect_to_database(self):
        try:
            # Decode base64 credentials
            credentials_json = base64.b64decode(settings.FIREBASE_CREDENTIALS_BASE64)
            credentials_dict = json.loads(credentials_json)
            
            # Initialize Firebase Admin with decoded credentials
            cred = credentials.Certificate(credentials_dict)
            self.client = initialize_app(cred)
            self.db = firestore.client()
            print("Successfully connected to Firebase")
        except Exception as e:
            print(f"Error connecting to Firebase: {e}")
            raise e

    async def close_database_connection(self):
        if self.client:
            self.client.delete()

firebase = Firebase()
