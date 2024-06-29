from dataclasses import dataclass

from fuel_efficency.entities.node import Node
from fuel_efficency.entities.position import Position


@dataclass(slots=True)
class DownHill(Node):
    weight: float = float(0.5)
    position: 'Position' = Position()

    def __eq__(self, other):
        """
        Check instances equalities

        Args:
            other:

        Returns:

        """
        if not hasattr(other, 'position') or not hasattr(other, 'weight'):
            raise NotImplementedError("Missing `position` or `weight` attribute")

        if isinstance(other, DownHill):
            return self.weight == other.weight and self.position == other.position
        return False

    def __hash__(self):
        """
        Hash method

        Returns:

        """
        return hash((self.weight, self.position))
