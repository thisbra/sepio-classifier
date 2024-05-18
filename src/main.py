from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .firebase.firebase import db
from .routes import Classifier

app = FastAPI()

# Set CORS settings if needed
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app.include_router(Classifier.router)

@app.get("/")
def read_root():
    return {"status": "on"}
