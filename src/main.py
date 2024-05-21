from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import Classifier
from .routes import Redis
from .logging_config import logger

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
app.include_router(Redis.router)

logger.info("Application started")

@app.get("/")
def read_root():
    return {"status": "on"}
