import sys
from dataclasses import dataclass
from typing import Optional


@dataclass(slots=True)
class Position:
    x: int = sys.maxsize
    y: int = sys.maxsize

    def __add__(self, other:'Position') -> Optional['Position']:
        """
        Add two Position objects together.

        Args:
            other (Position): The other Position object to add to this one.

        Returns:
            Position: The sum of the two Position objects.
        """
        try:
            return Position(self.x + other.x, self.y + other.y)
        except AttributeError:
            raise NotImplementedError(f"Cannot add Position and {type(other)}")

    def __sub__(self, other:'Position') -> Optional['Position']:
        """
        Subtract two Position objects.

        Args:
            other (Position): The other Position object to subtract from this one.

        Returns:
            Position: The difference of the two Position objects.
        """
        try:
            return Position(self.x - other.x, self.y - other.y)
        except AttributeError:
            raise NotImplementedError(f"Cannot subtract Position and {type(other)}")
        