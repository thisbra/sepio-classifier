from ..models.KnowledgeBaseItem import KnowledgeBaseItem
from ..models.MacAddress import MacAddress
from ..repository import KnowledgeBaseItem as KnowledgeBaseItemRepository

def getVendorAndAssetTypeByMacAddress(mac_address: MacAddress):
    vendors = KnowledgeBaseItemRepository.getVendorsByMacPrefix(mac_address.mac_address[:6])
    # TODO get asset type
    if not vendors:
        return None
    return vendors    
