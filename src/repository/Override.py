from ..firebase.firebase import db
from ..models.Override import Override
from ..models.MacAddress import MacAddress
from ..logging_config import logger

def addOverride(override: Override) -> Override | None:
    try:
        override_ref = db.collection('Overrides')
        override_ref.add(override.model_dump())
        logger.info("Successfully added override")
        return override
    except Exception as e:
        logger.error(f"An error occurred while adding override: {e}")
        return None

def getOverrideByMacAddress(mac_address: MacAddress.model_fields["MacAddress"]) -> Override | None:
    try:
        overrides_ref = db.collection('Overrides')
        query = overrides_ref.where('MacAddress', '==', mac_address)
        results = query.stream()

        for doc in results:
            override_data = doc.to_dict()
            logger.info("Successfully retrieved override by MacAddress")
            return Override(**override_data)
    except Exception as e:
        logger.error(f"An error occurred while retrieving override by MacAddress: {e}")
        return None

def updateOverride(override: Override) -> Override | None:
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
            logger.info("Successfully updated override")
            return override
    except Exception as e:
        logger.error(f"An error occurred while updating override: {e}")
        return None
