from pydantic import BaseModel, Field
from typing import Optional, List
from src.core.domain.value_object.address_value_object import AddressValueObject

class UserProfileEntity(BaseModel):
    name: str = Field(..., title = "Name", description = "Nome do colaborador portador do equipamento.")
    cpf: int = Field(..., title = "CPF", description = "CPF do colaborador.")
    age: str = Field(..., title = "Age", description = "Idade do colaborador")
    phone_number: str = Field(..., title = "phone_number", description = "")
    address: AddressValueObject


    
