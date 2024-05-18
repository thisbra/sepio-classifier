from pydantic import BaseModel
from typing import Optional

class KnowledgeBaseItem(BaseModel):
    Classification: str = None
    Icon: int = None
    MacPrefix: str
    Vendor: str = None
    id: str
