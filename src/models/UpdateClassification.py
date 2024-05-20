# src/models/UpdateCLassification.py
from pydantic import BaseModel

class UpdateClassification(BaseModel):
    classification: str
