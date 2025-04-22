import json
from src.adapters.driver.AWS_Lambda.schemas.create_asset_schema import MainCreateAssetEventSchema
from src.core.use_cases.equipment_use_case import EquipmentUseCase
from src.core.helpers.exceptions.item_not_found_error import ItemNotFoundError
from pydantic import ValidationError
from src.core.use_cases.equipment_use_case import EquipmentEntity

def create_equipment_handler(event, context):
    try:
        body = json.loads(event["body"])
        # validated_data = EquipmentEntity(**body)
        create_equipment_schema = MainCreateAssetEventSchema(**body)

        equipmentUseCase = EquipmentUseCase()
        equipmentUseCase.create(create_equipment_schema)

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Equipment criado com sucesso"})
        }

    except ValidationError as e:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Invalid input data", "details": str(e)})
        }

    except KeyError as e:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": f"Missing key: {e}"})
        }

    except ItemNotFoundError as e:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Ativo não encontrado"})
        }

    except Exception as e:
        print(f"An error occurred: {e, event}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
