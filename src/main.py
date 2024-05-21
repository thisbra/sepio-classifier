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

@app.get("/", tags=["Status"])
def read_root():
    return {"status": "on"}

app.include_router(Classifier.router, tags=["Classifier"])
app.include_router(Redis.router, tags=["Redis"])

logger.info("Application started")

