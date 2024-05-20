# src/models/MacAddress.py
from pydantic import BaseModel, Field

class MacAddress(BaseModel):
    MacAddress: str = Field(..., min_length=12, max_length=12, pattern=r"^[0-9A-F]{12}$")
