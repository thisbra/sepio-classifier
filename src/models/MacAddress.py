from typing import Annotated
from pydantic import BaseModel
from fastapi import Query

# MacAddress is a string of 12 hexadecimals between 0-9 and A-F 
class MacAddress(BaseModel):
    mac_address: Annotated[str, Query(..., min_length=12, max_length=12)]
    
