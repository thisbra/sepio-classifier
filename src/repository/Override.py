from ..firebase.firebase import db
from ..models.Override import Override
from ..models.MacAddress import MacAddress

def addOverride(override: Override) -> Override:
    try:
        override_ref = db.collection('Overrides')
        override_ref.add(override.model_dump())
        return override
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

def getOverrideByMacAddress(mac_address: MacAddress.model_fields["MacAddress"]) -> Override | None:
    try:
        overrides_ref = db.collection('Overrides')
        query = overrides_ref.where('MacAddress', '==', mac_address)
        results = query.stream()

        for doc in results:
            override_data = doc.to_dict()
            return Override(**override_data)
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

def updateOverride(override: Override) -> Override:
    try:
        overrides_ref = db.collection('Overrides')
        query = overrides_ref.where('MacAddress', '==', override.MacAddress)
        results = query.stream()

        override_dict = override.model_dump()
        # remove empty field from override
        if not override.Vendor:
            override_dict.pop("Vendor")
        if not override.Classification:
            override_dict.pop("Classification")

        for doc in results:
            doc.reference.update(override_dict)
            return override
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

    