# src/models/Override.py
from pydantic import BaseModel
from .MacAddress import MacAddress

class Override(BaseModel):
    MacAddress: str = MacAddress.model_fields["MacAddress"]
    Vendor: str | None = None
    Classification: str | None = None
