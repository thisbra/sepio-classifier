import firebase_admin
from firebase_admin import credentials, firestore
import os
import base64
import json
from dotenv import load_dotenv
from ..logging_config import logger

# Load environment variables from .env file
load_dotenv()

def init_firestore():
    firebase_key_base64 = os.getenv("FIREBASE_KEY")
    if not firebase_key_base64:
        logger.error("The FIREBASE_KEY environment variable is not set.")
        return None
    
    try:
        firebase_key_json = base64.b64decode(firebase_key_base64).decode('utf-8')
        cred = credentials.Certificate(json.loads(firebase_key_json))
        firebase_admin.initialize_app(cred)
        logger.info("Successfully connected to Firebase")
        return firestore.client()
    except Exception as e:
        logger.error(f"Failed to initialize Firebase: {e}")
        return None

db = init_firestore()
