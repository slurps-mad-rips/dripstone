from typing import Text, Option
from types import dataclass

@dataclass
class Label:
    description: Text
    name: Text
    color: Color
