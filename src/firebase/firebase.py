import firebase_admin
from firebase_admin import credentials, firestore

def init_firestore():
    # Use the application default credentials
    cred = credentials.Certificate("src/firebase/serviceAccountKey.json")
    firebase_admin.initialize_app(cred)
    return firestore.client()

db = init_firestore()

print(db)