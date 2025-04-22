
from src.adapters.driver.AWS_Lambda.schemas.create_asset_schema import MainCreateAssetEventSchema
from src.core.helpers.exceptions.item_not_found_error import ItemNotFoundError
from src.adapters.driven.infra.dynamo.dynamo_equipment_repository import DynamoEquipmentRepository
from src.core.domain.entities.equipment_entity import EquipmentEntity
import uuid


class EquipmentUseCase:
    def __init__(self):
        self.repository = DynamoEquipmentRepository()  

    def create(self, equipment_body: MainCreateAssetEventSchema) -> EquipmentEntity:
        equipment_entity = EquipmentEntity(id=str(uuid.uuid4()), **equipment_body.model_dump())
        if not equipment_entity:
            raise ValueError("Erro ao criar o Equipamento.")
        if not equipment_entity.sn:
            raise ValueError("Erro ao criar equipamento sem SN")
        self.repository.create(equipment_entity)
        
        return equipment_entity
    
    def get(self, id: str) -> EquipmentEntity:
        equipment = self.repository.get(id)
        if not equipment:
            raise ItemNotFoundError(f"Equipamento com id '{id}' não encontrado.")
        return equipment
    
    def list(self) -> EquipmentEntity:
        equipments = self.repository.list()
        return equipments
    
    def update(self, id:str, equipment:EquipmentEntity) -> EquipmentEntity:

        equipment = self.repository.update(id, equipment)            


        return equipment
    
    def delete(self, id)  -> None:
        print(f'Entrou no use case \n {id}')
        
        self.repository.delete(id)
        return None