import json
from ..models.RedisEvent import RedisEvent
from ..redis.redis import redis_client
from ..logging_config import logger

class EventRegister:
    def __init__(self, stream_name: str):
        self.stream_name = stream_name

    def register_event(self, event: RedisEvent):
        try:
            event_dict = event.model_dump()
            event_dict['data'] = json.dumps(event_dict['data'])
            redis_client.xadd(self.stream_name, event_dict)
            logger.info(f"Event registered in stream {self.stream_name}: {event_dict}")
        except Exception as e:
            logger.error(f"Failed to register event in stream {self.stream_name}: {e}")

# Example usage:
# event = RedisEvent(level="info", type="update", data={"key": "value"})
# event_register = EventRegister(stream_name="my_stream")
# event_register.register_event(event)
