import os
from pathlib import Path
import sys

#teste2
sys.path.insert(0, f"{str(Path(os.path.abspath(__file__)).parents[1])}/vendor")

from src.adapters.driver.AWS_Lambda.handlers.create_equipment_handler import create_equipment_handler
from src.adapters.driver.AWS_Lambda.handlers.get_equipment_handler import get_equipment_handler
from src.adapters.driver.AWS_Lambda.handlers.list_equipment_handler import list_equipment_handler
from src.adapters.driver.AWS_Lambda.handlers.update_equipment_handler import update_equipment_handler
from src.adapters.driver.AWS_Lambda.handlers.delete_equipment_handler import delete_equipment_handler