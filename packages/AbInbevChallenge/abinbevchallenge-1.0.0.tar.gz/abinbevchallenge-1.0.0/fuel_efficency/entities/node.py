from dataclasses import dataclass, field
from typing import Protocol

from fuel_efficency.entities.position import Position


@dataclass(slots=True)
class Node(Protocol):
    weight: float
    position: 'Position' = field(default_factory=Position)

    def __hash__(self):
        pass
    
    def __eq__(self, other):
        pass

    def __lt__(self, other):
        pass
