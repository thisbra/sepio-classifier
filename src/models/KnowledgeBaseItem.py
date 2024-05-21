from pydantic import BaseModel

class KnowledgeBaseItem(BaseModel):
    Classification: str = None
    Icon: int = None
    MacPrefix: str
    Vendor: str = None
    id: str
