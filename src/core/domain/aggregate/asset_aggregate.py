from typing import List
from pydantic import BaseModel
from src.core.domain.entities.equipment_entity import EquipmentEntity

class AssetAggregate(BaseModel):
    equipment: EquipmentEntity