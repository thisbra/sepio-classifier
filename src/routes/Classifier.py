from fastapi import APIRouter, HTTPException, Path, Body
from ..models.KnowledgeBaseItem import KnowledgeBaseItem
from ..models.UpdateVendor import UpdateVendor
from ..models.UpdateClassification import UpdateClassification
from ..models.Override import Override
from ..models.MacAddress import MacAddress
from ..service import Classifier as ClassifierService

router = APIRouter()

# Define the endpoints
@router.get("/classification/{mac_address}")
async def get_classification(mac_address: str = Path(..., min_length=12, max_length=12, regex=r"^[0-9A-F]{12}$")):
    classification = ClassifierService.getVendorAndAssetTypeByMacAddress(mac_address)
    if not classification:
        raise HTTPException(status_code=404, detail="Classification not found")
    return {"Vendor": classification["Vendor"], "Classification": classification["Classification"]}

@router.put("/vendor/{mac_address}")
async def update_vendor(mac_address: str = Path(..., min_length=12, max_length=12, regex=r"^[0-9A-F]{12}$"), 
                        vendor: UpdateVendor = Body(...)):
    override = Override(MacAddress=mac_address, Vendor=vendor.vendor)
    response = ClassifierService.addOverrideToRepository(override)
    if response:
        return response
    raise HTTPException(status_code=404, detail="Operation failed")

@router.put("/classification/{mac_address}")
async def update_type(mac_address: str = Path(..., min_length=12, max_length=12, regex=r"^[0-9A-F]{12}$"), 
                      classification: UpdateClassification = Body(...)):
    override = Override(MacAddress=mac_address, Classification=classification.classification)
    response = ClassifierService.addOverrideToRepository(override)
    if response:
        return response
    raise HTTPException(status_code=404, detail="Operation failed")
