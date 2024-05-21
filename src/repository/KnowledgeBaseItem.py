from ..firebase.firebase import db
from ..logging_config import logger

def getVendorsByMacPrefix(mac_prefix: str) -> list | None:
    try:
        vendors_ref = db.collection('KnowledgeBase') 
        query = vendors_ref.where('MacPrefix', '==', mac_prefix)
        results = query.stream()

        vendor_set = set()
        unique_vendors = []

        for doc in results:
            vendor_data = doc.to_dict()
            vendor_name = vendor_data.get("Vendor")
            if vendor_name and vendor_name not in vendor_set:
                vendor_set.add(vendor_name)
                unique_vendors.append({
                    "Vendor": vendor_data.get("Vendor")
                })

        logger.debug(f"Unique vendors found: {unique_vendors}")
        return unique_vendors
    
    except Exception as e:
        logger.error(f"An error occurred while getting vendors by Mac prefix: {e}")
        return None

def getMacRangesAndClassificationByVendor(vendor: str) -> list | None:
    try:
        vendors_ref = db.collection('KnowledgeBase') 
        query = vendors_ref.where('Vendor', '==', vendor)
        results = query.stream()

        mac_ranges = []

        for doc in results:
            vendor_data = doc.to_dict()
            mac_ranges.append({
                "MacRange": vendor_data.get("MacRange"),
                "Classification": vendor_data.get("Classification")
            })

        logger.debug(f"Mac ranges found for vendor {vendor}: {mac_ranges}")
        return mac_ranges
    
    except Exception as e:
        logger.error(f"An error occurred while getting Mac ranges and classification by vendor: {e}")
        return None

def getMacRangesAndClassificationByMacPrefix(mac_prefix: str) -> list | None:
    try:
        vendors_ref = db.collection('KnowledgeBase') 
        query = vendors_ref.where('MacPrefix', '==', mac_prefix)
        results = query.stream()

        mac_ranges = []

        for doc in results:
            vendor_data = doc.to_dict()
            mac_ranges.append({
                "id": doc.id,
                "MacRange": vendor_data.get("MacRange"),
                "Classification": vendor_data.get("Classification")
            })

        logger.debug(f"Mac ranges found for Mac prefix {mac_prefix}: {mac_ranges}")
        return mac_ranges
    
    except Exception as e:
        logger.error(f"An error occurred while getting Mac ranges and classification by Mac prefix: {e}")
        return None
