import json
from src.core.domain.aggregate.asset_aggregate import AssetAggregate
from src.core.domain.entities.equipment_entity import EquipmentEntity
from src.core.domain.value_object.physical_state_value_object import PhysicalState
from src.core.helpers.enums.equipment_type_enum import EquipmentTypeEnum
from src.adapters.driver.AWS_Lambda.handlers.create_equipment_handler import create_asset_handler

def test_create_asset_handler():
    mock_event = AssetAggregate(
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


    mock_context = {}

    response = create_asset_handler(mock_event, mock_context)

    assert response["statusCode"] == 200
    assert "body" in response