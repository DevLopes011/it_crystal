from src.core.domain.entities.equipment_entity import EquipmentEntity
from src.adapters.driver.AWS_Lambda.schemas.get_asset_schema import MainGetAssetEventSchema, MainGetAssetResponseSchema
from src.adapters.driver.AWS_Lambda.exceptions.missing_data_error import MissingDataError
from src.core.helpers.exceptions.item_not_found_error import ItemNotFoundError
from src.core.use_cases.equipment_use_case import EquipmentUseCase
import json

def get_equipment_handler(event, context):
    try:        
        id = event["pathParameters"]["id"]
        
        validated_data = MainGetAssetEventSchema(id=id)
        equipmentUseCase = EquipmentUseCase()
        
        equipment_entity = equipmentUseCase.get(validated_data.id)
        
        response  = MainGetAssetResponseSchema(equipment=equipment_entity)


        return {
            "statusCode": 200,
            "body": response.model_dump_json()

        }
    except KeyError as e:
        print(f"Missing key: {e}")
        return {
            "statusCode": 400,
            "body": json.dumps({"message": f"Missing key: {str(e)}"})
        }

    except ItemNotFoundError as e:
        print(f"Ativo não encontrado: {e}")
        return {
            "statusCode": 404,
            "body": json.dumps({"message": "Ativo não encontrado"})
        }

    except MissingDataError as e:
        print(f"Dados faltando: {e}")
        return {
            "statusCode": 400,
            "body": json.dumps({"message": str(e)})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"message": f"An error occurred: {str(e)}"})
        }
