from src.adapters.driver.AWS_Lambda.schemas.delete_asset_schema import MainDeleteAssetEventSchema
from src.core.domain.entities.equipment_entity import EquipmentEntity
from src.core.helpers.exceptions.item_not_found_error import ItemNotFoundError
from src.core.use_cases.equipment_use_case import EquipmentUseCase
import json

def delete_equipment_handler (event, context):
    try:
        id = event["pathParameters"]["id"]
        asset_use_case = EquipmentUseCase()

        validated_data = MainDeleteAssetEventSchema(id=id)

        delete =  asset_use_case.delete(validated_data.id)
              
        return {
            "statusCode": 200,
            "body": json.dumps(delete)
        }

    except KeyError as e:
        print(f"Missing key: {e}")
        return {
            "statusCode": 400,
            "body": f"Missing key: {e}"
        }
    
    except ItemNotFoundError as e:
        print(f"Asset não encontrado: {e}")
        return {
            "statusCode": 400,
            "body": "Ativo não encontrado"
        }

    except Exception as e:
        print(f"An error occurred: {e}")
        return {
            "statusCode": 500,
            "body": f"An error occurred: {e}"
        }