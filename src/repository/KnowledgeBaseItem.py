from ..firebase.firebase import db

def getVendorsByMacPrefix(mac_prefix: str):
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

        print(f"Unique vendors found: {unique_vendors}")
        return unique_vendors
    
    except Exception as e:
        print(f"An error occurred: {e}")
        raise