from fastapi import APIRouter, HTTPException, Path, Body
from ..models.KnowledgeBaseItem import KnowledgeBaseItem
from ..models.MacAddress import MacAddress
from ..service import Classifier as ClassifierService

router = APIRouter()

# Define the endpoints
@router.get("/classification/{mac_address}")
def get_classification(mac_address: str = Path(..., min_length=12, max_length=12, regex=r"^[0-9A-F]{12}$")):
    classification = ClassifierService.getVendorAndAssetTypeByMacAddress(MacAddress(mac_address=mac_address))    
    if not classification:
        raise HTTPException(status_code=404, detail="Classification not found")
    return classification

@router.put("/vendor/{mac_address}")
def update_vendor(mac_address: str = Path(..., min_length=12, max_length=12, regex=r"^[0-9A-F]{12}$"), 
                  vendor: KnowledgeBaseItem = Body(...)):
    # Logic to update vendor by mac_address
    # Example: Update vendor in the database
    updated_vendor = {"mac_address": mac_address, "vendor": vendor.Vendor}
    return updated_vendor

@router.put("/classification/{mac_address}")
def update_type(mac_address: str = Path(..., min_length=12, max_length=12, regex=r"^[0-9A-F]{12}$"), 
                classification: KnowledgeBaseItem = Body(...)):
    # Logic to update type by mac_address
    # Example: Update type in the database
    updated_type = {"mac_address": mac_address, "classification": classification.Classification}
    return updated_type
