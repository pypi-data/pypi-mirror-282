import sys

from typing import Optional
from dataclasses import dataclass


@dataclass(slots=True)
class Position:
    x: int = sys.maxsize
    y: int = sys.maxsize

    @property
    def get_x(self):
        return self.x

    @property
    def get_y(self):
        return self.y

    def __eq__(self, other):
        """
        Check instances equalities

        Args:
            other:

        Returns:

        """
        if isinstance(other, Position):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        """
        Hash method

        Returns:

        """
        return hash((self.x, self.y))

    def __add__(self, other: 'Position') -> Optional['Position']:
        """
        Add two Position objects together.

        Args:
            other (Position): The other Position object to add to this one.

        Returns:
            Position: The sum of the two Position objects.
        """
        if not isinstance(other, Position):
            raise NotImplementedError(f"Cannot add Position and {type(other)}")
        return Position(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Position') -> Optional['Position']:
        """
        Subtract two Position objects.

        Args:
            other (Position): The other Position object to subtract from this one.

        Returns:
            Position: The difference of the two Position objects.
        """
        if not isinstance(other, Position):
            raise NotImplementedError(f"Cannot subtract Position and {type(other)}")
        return Position(self.x - other.x, self.y - other.y)
