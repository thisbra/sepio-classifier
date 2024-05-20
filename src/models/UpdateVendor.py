# src/models/UpdateVendor.py
from pydantic import BaseModel

class UpdateVendor(BaseModel):
    vendor: str
