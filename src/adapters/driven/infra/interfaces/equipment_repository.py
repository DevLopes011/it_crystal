from abc import abstractmethod, ABC
from typing import List

from src.core.domain.entities.equipment_entity import EquipmentEntity



class EquipmentRepository(ABC):
    @abstractmethod
    def create(self, equipment: EquipmentEntity) -> EquipmentEntity:
        raise NotImplementedError()

    @abstractmethod
    def get(self, id: str) -> EquipmentEntity | None:
        raise NotImplementedError()

    @abstractmethod
    def list(self) -> List[EquipmentEntity]:
        raise NotImplementedError()

    @abstractmethod
    def update(self, equipment: EquipmentEntity) -> EquipmentEntity:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, id: str) -> None:
        raise NotImplementedError()