# src/models/RedisEvent.py
from pydantic import BaseModel

class RedisEvent(BaseModel):
    level: str
    type: str
    data: dict