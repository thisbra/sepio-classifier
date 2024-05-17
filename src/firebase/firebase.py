# src/firebase/firebase.py
import firebase_admin
from firebase_admin import credentials, firestore
import os
import base64
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def init_firestore():
    firebase_key_base64 = os.getenv("FIREBASE_KEY")
    if not firebase_key_base64:
        raise ValueError("The FIREBASE_KEY environment variable is not set.")
    
    firebase_key_json = base64.b64decode(firebase_key_base64).decode('utf-8')
    print(firebase_key_json)
    cred = credentials.Certificate(json.loads(firebase_key_json))
    firebase_admin.initialize_app(cred)
    return firestore.client()

db = init_firestore()
