from typing import List, Optional
from pydantic import BaseModel, Field


class PhysicalState(BaseModel):
    condition: str = Field(..., title = "Condition", description = "Estado de conservação do equipamento.")
    defects: Optional[List[str]] = Field(None, title = "Defects", description = "Lista de defeitos ou problemas conhecidos.")
    repair_history: Optional[List[str]] = Field(None, title = "Repair History", description = "Histórico de reparos.") 
    