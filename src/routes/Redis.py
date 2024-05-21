# src/routes/Redis.py
from fastapi import APIRouter, HTTPException
from ..redis.redis import redis_client

router = APIRouter()

@router.get("/events")
async def get_events():
    try:
        # Retrieve all entries from the sepio-events stream
        events = redis_client.xrange('sepio-events', '-', '+')
        return {"status": "success", "events": events}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
