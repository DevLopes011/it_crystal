from pydantic import BaseModel, Field


class AddressValueObject(BaseModel):
    cep: str = Field(..., title = "CEP", description = "")
    estado: int = Field(..., title = "estado", description = "")
    cidade: int = Field(..., title = "cidade", description = "")
    bairro: int = Field(..., title = "bairro", description = "")
    numero: int = Field(..., title = "numero", description = "")
    logradouro: str = Field(..., title = "logradouro", description = "")
