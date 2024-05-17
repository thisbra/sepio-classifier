from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .firebase.firebase import db 

app = FastAPI()

# Set CORS settings if needed
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

@app.get("/")
def read_root():
    return {"Hello": "Deployedd"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/knowledgebase/{doc_id}")
async def get_knowledgebase_item(doc_id: str):
    try:
        doc_ref = db.collection('KnowledgeBase').document(doc_id)
        doc = doc_ref.get()
        if doc.exists:
            return doc.to_dict()
        else:
            raise HTTPException(status_code=404, detail="Document not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
