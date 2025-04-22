
from pydantic import BaseModel
from src.core.domain.entities.equipment_entity import EquipmentEntity

class MainDeleteAssetEventSchema(BaseModel):
    id: str

class MainDeleteAssetResponseSchema(BaseModel):
    equipment: EquipmentEntity