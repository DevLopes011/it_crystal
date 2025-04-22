from copy import deepcopy, replace
from unittest.mock import MagicMock
import pytest
from src.core.domain.entities.equipment_entity import EquipmentEntity
from src.core.domain.value_object.physical_state_value_object import PhysicalState
from src.core.helpers.enums.equipment_type_enum import EquipmentTypeEnum
from src.adapters.driven.infra.interfaces.equipment_repository import EquipmentRepository
from src.core.domain.aggregate.asset_aggregate import AssetAggregate
from src.core.use_cases.equipment_use_case import EquipmentUseCase

# GET
# Deve ter sucesso
# deve falhar se náo existir

#UPDATE
# deve ter sucesso OK
# deve ter dados corretos
# deve falhar caso o SN seja editado  OK
# deve falhar caso um valor ser invalido para campo
# deve falhar caso um dado de referencia estiver incorreto trocar ex: trocar id por 
# deve falhar caso o usuário não tenha as devidas permissões para fazer a alteração

class TestAssetUseCase:
    @pytest.fixture
    def asset_use_case(self) -> EquipmentUseCase:
        asset_repository_mock = MagicMock(spec=EquipmentRepository)
        return EquipmentUseCase(asset_repository_mock)
    
    def test_get_success(self, asset_use_case: EquipmentUseCase):
        id_asset_body = 4
        asset_use_case.asset_repository.get = MagicMock(return_value="Status Code 200")
        result = asset_use_case.get(id_asset_body)
        assert result == "Status Code 200"

    def test_get_fail_asset_not_found(self, asset_use_case: EquipmentUseCase):
        asset_use_case.asset_repository.get = MagicMock(return_value=None)
        with pytest.raises(ValueError, match="Equipamento não localizado."):
            asset_use_case.get(2)

    def test_update_success (self, asset_use_case: EquipmentUseCase):
        asset_body = AssetAggregate(
            equipment= EquipmentEntity(
                id_entity="0001",
                sn="UN2399",
                Equipmenttype=EquipmentTypeEnum.NOTEBOOK,
                brand="LG",
                model="L1G4",
                asset_tag="Cy0012",
                physical_state= PhysicalState(
                    condition="Mock condition",
                    defects=["Mock defects"],
                    repair_history=["repair history"],
                )
            ),
            peripherals= [EquipmentEntity(
                id_entity="0002",
                sn="M023",
                Equipmenttype=EquipmentTypeEnum.MOUSE,
                brand="logi",
                model="liga321",
                asset_tag="cy822",
                physical_state= PhysicalState(
                    condition="Mock condition",
                    defects=["Mock defects"],
                    repair_history=["repair history"],
                ),
            )]
        )

        asset_use_case.asset_repository.update = MagicMock(return_value=asset_body)
        result = asset_use_case.asset_repository.update(asset_body)
        assert result == asset_body, "Asset atualizado com sucesso."

    def test_update_edit_sn (self, asset_use_case: EquipmentUseCase):
        asset_body = AssetAggregate(
            equipment= EquipmentEntity(
                id_entity="0001",
                sn="UN2399",
                Equipmenttype=EquipmentTypeEnum.NOTEBOOK,
                brand="LG",
                model="L1G4",
                asset_tag="Cy0012",
                physical_state= PhysicalState(
                    condition="Mock condition",
                    defects=["Mock defects"],
                    repair_history=["repair history"],
                )
            ),
            peripherals= [EquipmentEntity(
                id_entity="0002",
                sn="M023",
                Equipmenttype=EquipmentTypeEnum.MOUSE,
                brand="logi",
                model="liga321",
                asset_tag="cy822",
                physical_state= PhysicalState(
                    condition="Mock condition",
                    defects=["Mock defects"],
                    repair_history=["repair history"],
                ),
            )]
        )
        asset_use_case.asset_repository.get = MagicMock(return_value = asset_body)
        new_asset_body = deepcopy(asset_body)
        new_asset_body.equipment.sn = "UN23a]99"
        with pytest.raises(ValueError, match = "O campo 'sn' não pode ser editado."):
            asset_use_case.update(new_asset_body)

    def test_update_edit_id_entity (self, asset_use_case: EquipmentUseCase):
        asset_body = AssetAggregate(
            equipment= EquipmentEntity(
                id_entity="0001",
                sn="UN2399",
                Equipmenttype=EquipmentTypeEnum.NOTEBOOK,
                brand="LG",
                model="L1G4",
                asset_tag="Cy0012",
                physical_state= PhysicalState(
                    condition="Mock condition",
                    defects=["Mock defects"],
                    repair_history=["repair history"],
                )
            ),
            peripherals= [EquipmentEntity(
                id_entity="0002",
                sn="M023",
                Equipmenttype=EquipmentTypeEnum.MOUSE,
                brand="logi",
                model="liga321",
                asset_tag="cy822",
                physical_state= PhysicalState(
                    condition="Mock condition",
                    defects=["Mock defects"],
                    repair_history=["repair history"],
                ),
            )]
        )

        asset_use_case.asset_repository.get = MagicMock(return_value = asset_body)
        new_asset_body = deepcopy(asset_body)
        new_asset_body.equipment.id_entity = "00a01"


        with pytest.raises(ValueError, match = "O campo 'id_entity' não pode ser editado."):
            asset_use_case.update(new_asset_body)

    def test_create_asset_success(self, asset_use_case: EquipmentUseCase):
        asset_body = AssetAggregate(
            equipment= EquipmentEntity(
                id_entity="0001",
                sn="UN2399",
                Equipmenttype=EquipmentTypeEnum.NOTEBOOK,
                brand="LG",
                model="L1G4",
                asset_tag="Cy0012",
                physical_state= PhysicalState(
                    condition="Mock condition",
                    defects=["Mock defects"],
                    repair_history=["repair history"],
                )
            ),
            peripherals= [EquipmentEntity(
                id_entity="0002",
                sn="M023",
                Equipmenttype=EquipmentTypeEnum.MOUSE,
                brand="logi",
                model="liga321",
                asset_tag="cy822",
                physical_state= PhysicalState(
                    condition="Mock condition",
                    defects=["Mock defects"],
                    repair_history=["repair history"],
                ),
            )]
        )

        asset_use_case.asset_repository.create = MagicMock(return_value=asset_body)
        result = asset_use_case.create(asset_body)
        assert result == asset_body

    def test_create_asset_should_fail_when_serial_number_is_missing(self, asset_use_case: EquipmentUseCase):
        asset_body = AssetAggregate(
            equipment= EquipmentEntity(
                id_entity="",
                sn="UN2399",
                Equipmenttype=EquipmentTypeEnum.NOTEBOOK,
                brand="LG",
                model="L1G4",
                asset_tag="Cy0012",
                physical_state= PhysicalState(
                    condition="Mock condition",
                    defects=["Mock defects"],
                    repair_history=["repair history"],
                )
            ),
            peripherals= [EquipmentEntity(
                id_entity="0002",
                sn="M023",
                Equipmenttype=EquipmentTypeEnum.MOUSE,
                brand="logi",
                model="liga321",
                asset_tag="cy822",
                physical_state= PhysicalState(
                    condition="Mock condition",
                    defects=["Mock defects"],
                    repair_history=["repair history"],
                ),
            )]
        )

        asset_use_case.asset_repository.create = MagicMock(return_value = asset_body)
        result = asset_use_case


        with pytest.raises(ValueError, match = "O campo 'id_entity' não pode ser editado."):
            asset_use_case.update(result)