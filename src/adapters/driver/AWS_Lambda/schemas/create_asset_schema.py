from pydantic import BaseModel
from src.core.domain.value_object.physical_state_value_object import PhysicalState
from src.core.helpers.enums.equipment_type_enum import EquipmentTypeEnum
from src.core.domain.entities.equipment_entity import EquipmentEntity
from pydantic import BaseModel, Field

class MainCreateAssetEventSchema(BaseModel):
    sn: str = Field(..., title = "Serial Number", description = "Número de série do equipamento.")
    equipment_type: EquipmentTypeEnum = Field(..., title = "Type Equipment", description = "Tipo de equipamento.")
    brand: str = Field(..., title = "Brand", description = "Marca do equipamento.")
    model: str = Field(..., title = "Model", description = "Modelo do equipamento.")
    asset_tag: str = Field(..., title = "Asset Tag", description = "Tag de patrimônio do equipamento.")
    physical_state: PhysicalState
    
class MainGetAssetResponseSchema(BaseModel):
    equipment: EquipmentEntity