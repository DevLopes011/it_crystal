
from pydantic import BaseModel
from src.core.domain.entities.equipment_entity import EquipmentEntity

class MainGetAssetEventSchema(BaseModel):
    id: str
    
class MainGetAssetResponseSchema(BaseModel):
    equipment: EquipmentEntity
