import random
from enum import Enum

import numpy as np


class Direction(Enum):
    East = "E"
    West = "W"
    North = "N"
    South = "S"


class RotationDirection(Enum):
    CW = "CW"
    CCW = "CCW"


class TwistDirection(Enum):
    East = "E"
    West = "W"


Point = tuple[int, int]


class Board:
    def __init__(self, board: np.ndarray):
        """Initialize a board wrapper.

        Args:
            board: The NumPy array used as the puzzle state.
        """
        self.board = board

    def rotationA(
        self,
        pointA: Point,
        pointB: Point,
        pointC: Point,
        direction: RotationDirection,
    ):
        """Rotate the cells around an A-shaped three-point configuration.

        Args:
            pointA: The first point of the configuration.
            pointB: The center point of the configuration.
            pointC: The third point of the configuration.
            direction: The clockwise or counterclockwise rotation direction.

        Returns:
            The mutated NumPy board array.
        """
        #  A
        #  |
        #  p
        #  |
        #  B - q - C
        #

        q = pointC[1] - pointB[1]
        p = abs(pointB[0] - pointA[0])
        if direction == RotationDirection.CW:
            self.moveboard(pointB, Direction.West, q)
            self.moveboard(pointB, Direction.South, p)
            self.moveboard(pointB, Direction.East, q)
            self.moveboard(pointB, Direction.North, p)

        elif direction == RotationDirection.CCW:
            self.moveboard(pointB, Direction.South, p)
            self.moveboard(pointB, Direction.West, q)
            self.moveboard(pointB, Direction.North, p)
            self.moveboard(pointB, Direction.East, q)

        return self.board

    def rotationB(
        self,
        pointA: Point,
        pointB: Point,
        pointC: Point,
        direction: RotationDirection,
    ):
        """Rotate the cells around a B-shaped three-point configuration.

        Args:
            pointA: The first point of the configuration.
            pointB: The second point of the configuration.
            pointC: The third point of the configuration.
            direction: The clockwise or counterclockwise rotation direction.
        """
        # A - q - B
        # |
        # p
        # |
        # C
        #

        q = pointB[1] - pointA[1]
        p = abs(pointC[0] - pointA[0])
        if direction == RotationDirection.CW:
            self.moveboard(pointA, Direction.North, p)
            self.moveboard(pointA, Direction.West, q)
            self.moveboard(pointA, Direction.South, p)
            self.moveboard(pointA, Direction.East, q)
        elif direction == RotationDirection.CCW:
            self.moveboard(pointA, Direction.West, q)
            self.moveboard(pointA, Direction.North, p)
            self.moveboard(pointA, Direction.East, q)
            self.moveboard(pointA, Direction.South, p)

    def rotationC(
        self,
        pointA: Point,
        pointB: Point,
        pointC: Point,
        direction: RotationDirection,
    ):
        """Rotate the cells around a C-shaped three-point configuration.

        Args:
            pointA: The first point of the configuration.
            pointB: The second point of the configuration.
            pointC: The third point of the configuration.
            direction: The clockwise or counterclockwise rotation direction.
        """
        # A - q - B
        #         |
        #         p
        #         |
        #         C
        #

        q = pointB[1] - pointA[1]
        p = pointC[0] - pointB[0]
        if direction == RotationDirection.CW:
            self.moveboard(pointA, Direction.East, q)
            self.moveboard(pointB, Direction.North, p)
            self.moveboard(pointA, Direction.West, q)
            self.moveboard(pointB, Direction.South, p)
        elif direction == RotationDirection.CCW:
            self.moveboard(pointB, Direction.North, p)
            self.moveboard(pointA, Direction.East, q)
            self.moveboard(pointB, Direction.South, p)
            self.moveboard(pointA, Direction.West, q)

    def rotationD(
        self,
        pointA: Point,
        pointB: Point,
        pointC: Point,
        direction: RotationDirection,
    ):
        """Rotate the cells around a D-shaped three-point configuration.

        Args:
            pointA: The first point of the configuration.
            pointB: The second point of the configuration.
            pointC: The third point of the configuration.
            direction: The clockwise or counterclockwise rotation direction.
        """
        #       A
        #       |
        #       p
        #       |
        # B - q - C

        q = pointC[1] - pointB[1]
        p = pointB[0] - pointA[0]
        if direction == RotationDirection.CW:
            self.moveboard(pointA, Direction.South, p)
            self.moveboard(pointB, Direction.East, q)
            self.moveboard(pointA, Direction.North, p)
            self.moveboard(pointB, Direction.West, q)
        elif direction == RotationDirection.CCW:
            self.moveboard(pointB, Direction.East, q)
            self.moveboard(pointA, Direction.South, p)
            self.moveboard(pointB, Direction.West, q)
            self.moveboard(pointA, Direction.North, p)

    def tw(
        self,
        pointA: Point,
        pointB: Point,
        pointC: Point,
        direction: TwistDirection,
    ):
        """Twist a corner using paired board rotations.

        Args:
            pointA: The first point of the twist configuration.
            pointB: The center point of the twist configuration.
            pointC: The third point of the twist configuration.
            direction: The east or west twist direction.
        """
        corner = (pointB[0] - 1, pointB[1])
        if direction == TwistDirection.West:
            self.rotationD(corner, pointA, pointB, RotationDirection.CW)
            self.rotationA(corner, pointB, pointC, RotationDirection.CW)
        elif direction == TwistDirection.East:
            self.rotationA(corner, pointB, pointC, RotationDirection.CCW)
            self.rotationD(corner, pointA, pointB, RotationDirection.CCW)

    def randomize(self):
        """Apply random valid moves to scramble the board."""
        direcs = list(Direction)
        n = self.board.shape[0]
        for _ in range(100):
            randx = random.randint(0, n - 1)
            randy = random.randint(0, n - 1)
            direc = random.choice(direcs)
            amount = random.randint(1, n - 1)
            elem = randx, randy
            self.moveboard(elem, direc, amount)

    def moveboard(self, elem: Point, direc: Direction, amount: int):
        """Move a row or column by a wrapped amount.

        Args:
            elem: The row and column of the line to move.
            direc: The direction in which to move the line.
            amount: The number of positions to move.
        """
        x, y = elem
        amount = abs(amount)
        if direc == Direction.North:
            self.board[:, y] = np.roll(self.board[:, y], -amount)
        elif direc == Direction.South:
            self.board[:, y] = np.roll(self.board[:, y], amount)
        elif direc == Direction.West:
            self.board[x, :] = np.roll(self.board[x, :], -amount)
        elif direc == Direction.East:
            self.board[x, :] = np.roll(self.board[x, :], amount)

    def where(self, n: int) -> Point:
        """Find the row and column containing a value.

        Args:
            n: The board value to locate.

        Returns:
            The row and column containing the value.
        """
        found = np.where(self.board == n)
        return (found[0][0], found[1][0])
