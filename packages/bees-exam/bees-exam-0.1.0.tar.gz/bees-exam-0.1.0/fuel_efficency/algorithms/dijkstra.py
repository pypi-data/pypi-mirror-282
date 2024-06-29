import math
import heapq

from abc import ABC
from typing import List
from fuel_efficency.algorithms.path_finding import PathfindingStrategy
from fuel_efficency.entities.valley import Valley
from fuel_efficency.entities.node import Node
from fuel_efficency.entities.position import Position


class DijkstraStrategy(ABC):

    cardinal_directions = [Position(-1, -1), Position(-1, 0), Position(-1, 1), Position(0, -1),
                           Position(0, 1), Position(1, -1), Position(1, 0), Position(1, 1)]

    @staticmethod
    def find_path(grid: List[List[Node]], start: Node, end: Node):
        """
        Args:
            grid:
            start:
            end:

        Returns:

        """
        queue = [(0, start)]
        distances = {start: 0}
        came_from = {start: None}

        while queue:
            current_distance, current = heapq.heappop(queue)

            if current == end:
                path = []
                while current:
                    path.append(current)
                    current = came_from[current]
                return path[::-1]

            for neighbor in DijkstraStrategy.get_neighbors(grid, current):
                distance = int(current_distance + neighbor.weight)
                if distance < distances.get(neighbor.position, float('inf')):
                    distances[neighbor.position] = distance
                    heapq.heappush(queue, (distance, neighbor))
                    came_from[neighbor.position] = current
        return queue

    @staticmethod
    def get_neighbors(grid: List[List[Node]], node: Node) -> List[Node]:
        """
        Args:
            grid:
            node:

        Returns:

        """
        neighbors = []
        for direction in DijkstraStrategy.cardinal_directions:
            new_x = node.position.x + direction.x
            new_y = node.position.y + direction.y
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                neighbors.append(grid[new_x][new_y])
        return neighbors

    @staticmethod
    def calculate_distance(node1: Node, node2: Node) -> float:
        """
        Args:
            node1:
            node2:

        Returns:

        """
        return math.sqrt((node1.position.x - node2.position.x)**2 + (node1.position.y - node2.position.y)**2)

