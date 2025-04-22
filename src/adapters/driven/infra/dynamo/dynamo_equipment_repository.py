from src.adapters.driver.AWS_Lambda.schemas.create_asset_schema import MainCreateAssetEventSchema
from src.adapters.driven.infra.dynamo.dynamo_update_service import DynamoUpdateService
from src.core.domain.entities.equipment_entity import EquipmentEntity
from src.adapters.driver.data_mappers.equipment_aggregate_data_mapper import EquipmentDataMapper
from src.adapters.driven.infra.interfaces.equipment_repository import EquipmentRepository
from typing import List
import logging
import traceback
import boto3
import os
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class DynamoEquipmentRepository(EquipmentRepository):
    def __init__(self):
        self.table_name = os.getenv("DYNAMO_EQUiPMENT")
        if not self.table_name:
            raise ValueError("A variável de ambiente DYNAMO_EQUiPMENT não está definida.")
        
        self.dynamo_updater = DynamoUpdateService(self.table_name)
        
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table(self.table_name)
        self.mapper = EquipmentDataMapper()
        logger.info(f"DynamoAssetRepository inicializado com a tabela: {self.table_name}")
        
    def create(self, equipment: EquipmentEntity) -> EquipmentEntity:
        try:
            equipment_dict = self.mapper.domain_to_db(equipment)        

            self.table.put_item(Item=equipment_dict,
                                ConditionExpression="attribute_not_exists(id)",)
            return equipment
    
        except Exception as e:
            logger.error(f"Erro ao criar asset na tabela: {self.table_name}. {e}")
            logger.debug(traceback.format_exc())
            raise Exception("Erro ao salvar no banco.")

    def get(self, id: str) -> EquipmentEntity:
        try:
            response = self.table.get_item(Key={"id": id})
            if "Item" not in response:
                return None
            item = response["Item"]
            return self.mapper.db_to_domain(item)
        except Exception as e:
            logger.error(f"Erro ao buscar equipamento: {e}")
            logger.debug(traceback.format_exc())
            raise

    def list(self) -> List[EquipmentEntity]:
        try:
            response = self.table.scan()
            items = response.get("Items", [])
            
            print(items)
            equipamentos = [EquipmentEntity(**data) for data in items]
            return equipamentos

        except Exception as e:
            logger.error("Erro ao listar equipamentos do DynamoDB")
            traceback.print_exc()
            return 'caiu no erro'

    def update(self, id: str, equipment: EquipmentEntity) -> EquipmentEntity:
        print(f"Id: {id}")
        equipment_dict = self.mapper.domain_to_db(equipment)
        print(f"Dict do equipamento: {equipment_dict}")
        updated_item = self.dynamo_updater.update_item(id, equipment_dict)
        print("ele quebra antes")
        return self.mapper.db_to_domain(updated_item)

    def delete(self, id: str) -> None:
        print(id)
        response = self.table.delete_item(
            Key={"id": id},
            ReturnValues="ALL_OLD"
        )

        return "Attributes" in response