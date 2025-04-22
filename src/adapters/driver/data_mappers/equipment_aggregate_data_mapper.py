from src.core.helpers.enums.equipment_type_enum import EquipmentTypeEnum
from src.core.domain.entities.equipment_entity import EquipmentEntity

class EquipmentDataMapper:
    @staticmethod
    def domain_to_db(data: EquipmentEntity) -> dict:
        try:
            db_data = data.model_dump()
            db_data["equipment_type"] = data.equipment_type.value 
            return db_data
        except KeyError as e:
            raise ValueError(f"Campo obrigatório '{e.args[0]}' está faltando ou inválido.")

    @staticmethod
    def db_to_domain(data: dict) -> EquipmentEntity:
        try:
            if "equipment_type" in data and isinstance(data["equipment_type"], str):
                data["equipment_type"] = EquipmentTypeEnum(data["equipment_type"])
            return EquipmentEntity(**data)
        except (KeyError, ValueError) as e:
            raise ValueError(f"Erro ao converter item do banco: {e}")
