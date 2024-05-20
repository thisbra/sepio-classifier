from ..models.KnowledgeBaseItem import KnowledgeBaseItem
from ..models.Override import Override
from ..models.MacAddress import MacAddress
from ..repository import KnowledgeBaseItem as KnowledgeBaseItemRepository
from ..repository import Override as OverrideRepository
from ..utils.functions.HexidecimalToDecimal import HexadecimalToDecimal
from ..utils.functions.AddressIsInRange import AddressIsInRange

def getVendorAndAssetTypeByMacAddress(mac_address: MacAddress.model_fields["MacAddress"]):
    vendors = KnowledgeBaseItemRepository.getVendorsByMacPrefix(mac_address[:6])
    if not vendors:
        vendors = [{"Vendor": "Not Found"}]
    classifications = KnowledgeBaseItemRepository.getMacRangesAndClassificationByMacPrefix(mac_address[:6])    
    response = {
        "Vendor": vendors[0]["Vendor"],
        "Classification": "Not Found"
    }

    # If there is only one classification and no mac range, 
    # return the default clssification for the mac prefix
    if len(classifications) == 1 and classifications[0]["MacRange"] is None:
        response["Classification"] = classifications[0]["Classification"]
        response["id"] = classifications[0]["id"]

    
    if len(classifications) > 1:
        mac_address_suffix = mac_address[-6:]
        for obj in classifications:
            if AddressIsInRange(mac_address_suffix, obj["MacRange"]):
                response["Classification"] = obj["Classification"]
                response["id"] = obj["id"]
                break

    if getVendorOrClassificationFromOverrides(mac_address):
        override = getVendorOrClassificationFromOverrides(mac_address)
        if override.Vendor:
            response["Vendor"] = override.Vendor
        if override.Classification:
            response["Classification"] = override.Classification

    return response

def addOverrideToRepository(override: Override) -> Override | None:
    if OverrideRepository.getOverrideByMacAddress(override.MacAddress):
        return OverrideRepository.updateOverride(override)
    return OverrideRepository.addOverride(override)

def getVendorOrClassificationFromOverrides(mac_address: MacAddress.model_fields["MacAddress"]) -> Override | None:
    return OverrideRepository.getOverrideByMacAddress(mac_address)
