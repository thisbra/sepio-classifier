from pydantic import BaseModel
from typing import Optional

class KnowledgeBaseItem(BaseModel):
    Classification: Optional[str] = None
    Icon: Optional[int] = None
    MacPrefix: str
    Vendor: Optional[str] = None
    id: str
