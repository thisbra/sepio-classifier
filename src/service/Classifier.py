from ..models.KnowledgeBaseItem import KnowledgeBaseItem
from ..repository import KnowledgeBaseItem as KnowledgeBaseItemRepository
from ..utils.functions.HexidecimalToDecimal import HexadecimalToDecimal
from ..utils.functions.AddressIsInRange import AddressIsInRange

def getVendorAndAssetTypeByMacAddress(mac_address: str):
    vendors = KnowledgeBaseItemRepository.getVendorsByMacPrefix(mac_address[:6])
    if not vendors:
        return None
    classifications = KnowledgeBaseItemRepository.getMacRangesAndClassificationByMacPrefix(mac_address[:6])    
    response = {
        "Vendor": vendors[0]["Vendor"],
        "Classification": "Not Found"
    }

    # If there is only one classification and no mac range, 
    # return the default clssification for the mac prefix
    if len(classifications) == 1 and classifications[0]["MacRange"] is None:
        response["Classification"] = classifications[0]["Classification"]
        return response
    
    mac_address_suffix = mac_address[-6:]
    for obj in classifications:
        if AddressIsInRange(mac_address_suffix, obj["MacRange"]):
            response["Classification"] = obj["Classification"]
            break

    return response
        
