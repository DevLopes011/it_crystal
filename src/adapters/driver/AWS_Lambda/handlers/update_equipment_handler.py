from src.adapters.driver.AWS_Lambda.schemas.update_asset_schema import MainUpdateAssetEventSchema
from src.core.helpers.exceptions.item_not_found_error import ItemNotFoundError
from src.core.use_cases.equipment_use_case import EquipmentUseCase
import json

def update_equipment_handler(event, context):
    try:
        print('entrou no handler')
        body = json.loads(event["body"])
        equipment_id = event["pathParameters"]["id"]

        
        validate_data = MainUpdateAssetEventSchema(equipment=body)

        equipment_entity = validate_data.equipment 

        equipmentUseCase = EquipmentUseCase()
        response = equipmentUseCase.update(equipment_id, equipment_entity)

        return {
            "statusCode": 200,
            "body": response.model_dump_json()
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
