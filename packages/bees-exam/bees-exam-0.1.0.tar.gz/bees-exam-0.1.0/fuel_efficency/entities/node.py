from dataclasses import dataclass
from typing import Protocol

from fuel_efficency.entities.position import Position


@dataclass(slots=True)
class Node(Protocol):
    weight: float
    position: 'Position' = Position()

    @property
    def get_weight(self):
        return self.weight

    @property
    def get_position(self):
        return self.position

    def __eq__(self, other):
        if not hasattr(other, 'position') or not hasattr(other, 'weight'):
            raise NotImplementedError("Missing `position` or `weight` attribute")
        return self.position == other.position

    def __lt__(self, other):
        if hasattr(other, 'weight'):
            return self.weight < other.weight
        else:
            raise NotImplementedError("Missing `weight` attribute")
