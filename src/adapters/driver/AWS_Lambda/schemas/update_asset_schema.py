
from pydantic import BaseModel
from src.core.domain.entities.equipment_entity import EquipmentEntity


class MainUpdateAssetEventSchema(BaseModel):
    equipment: EquipmentEntity
    
class MainUpdateAssetResponseSchema(BaseModel):
    equipment: EquipmentEntity