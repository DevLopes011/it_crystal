from pydantic import ValidationError
from src.adapters.driver.AWS_Lambda.schemas.list_asset_schema import MainListAssetResponseSchema
from src.core.domain.entities.equipment_entity import EquipmentEntity
from src.core.domain.aggregate.asset_aggregate import AssetAggregate
from src.core.helpers.exceptions.item_not_found_error import ItemNotFoundError
from src.core.use_cases.equipment_use_case import EquipmentUseCase
import json

def list_equipment_handler (event, context):
    try:
        equipmentUseCase = EquipmentUseCase()
        equipments_raw = equipmentUseCase.list()
        equipments_entities = [
            e if isinstance(e, EquipmentEntity) else EquipmentEntity(**e)
            for e in equipments_raw
        ]

        response = MainListAssetResponseSchema(equipment=equipments_entities)

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