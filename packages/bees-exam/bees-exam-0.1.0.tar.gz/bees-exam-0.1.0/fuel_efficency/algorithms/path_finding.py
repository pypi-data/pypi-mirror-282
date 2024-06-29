from abc import ABC, abstractmethod
from typing import List

from fuel_efficency.entities.node import Node


class PathfindingStrategy(ABC):

    @abstractmethod
    def find_path(self, grid: List[List[Node]], start: Node, end: Node):
        """
        Args:
            grid:
            start:
            end:

        Returns:

        """
        pass  # pragma: no cover

    @abstractmethod
    def get_neighbors(self, grid: List[List[Node]], node: Node) -> List[Node]:
        """
        Args:
            grid:
            node:

        Returns:

        """
        pass  # pragma: no cover

    @abstractmethod
    def calculate_distance(self, node1: Node, node2: Node) -> float:
        """
        Args:
            node1:
            node2:

        Returns:

        """
        pass  # pragma: no cover
