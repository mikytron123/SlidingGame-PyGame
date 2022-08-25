import random
from enum import Enum
from typing import List, Tuple

import numpy as np


class Direction(Enum):
    East = "E"
    West = "W"
    North = "N"
    South = "S"


Point = Tuple[int, int]


class Board:
    def __init__(self, board: np.ndarray):
        self.board = board

    def rotationA(self, pointA: Point, pointB: Point, pointC: Point, dir: str):
        #  A
        #  |
        #  p
        #  |
        #  B - q - C
        #

        q = pointC[1] - pointB[1]
        p = abs(pointB[0] - pointA[0])
        if dir == "CW":
            self.moveboard(pointB, Direction.West, q)
            self.moveboard(pointB, Direction.South, p)
            self.moveboard(pointB, Direction.East, q)
            self.moveboard(pointB, Direction.North, p)

        elif dir == "CCW":
            self.moveboard(pointB, Direction.South, p)
            self.moveboard(pointB, Direction.West, q)
            self.moveboard(pointB, Direction.North, p)
            self.moveboard(pointB, Direction.East, q)

        return self.board

    def rotationB(self, pointA: Point, pointB: Point, pointC: Point, dir: str):
        # A - q - B
        # |
        # p
        # |
        # C
        #

        q = pointB[1] - pointA[1]
        p = abs(pointC[0] - pointA[0])
        if dir == "CW":
            self.moveboard(pointA, Direction.North, p)
            self.moveboard(pointA, Direction.West, q)
            self.moveboard(pointA, Direction.South, p)
            self.moveboard(pointA, Direction.East, q)
        elif dir == "CCW":
            self.moveboard(pointA, Direction.West, q)
            self.moveboard(pointA, Direction.North, p)
            self.moveboard(pointA, Direction.East, q)
            self.moveboard(pointA, Direction.South, p)

    def rotationC(self, pointA: Point, pointB: Point, pointC: Point, dir: str):
        # A - q - B
        #         |
        #         p
        #         |
        #         C
        #

        q = pointB[1]-pointA[1]
        p = pointC[0] - pointB[0]
        if dir == "CW":
            self.moveboard(pointA, Direction.East, q)
            self.moveboard(pointB, Direction.North, p)
            self.moveboard(pointA, Direction.West, q)
            self.moveboard(pointB, Direction.South, p)
        elif dir == "CCW":
            self.moveboard(pointB, Direction.North, p)
            self.moveboard(pointA, Direction.East, q)
            self.moveboard(pointB, Direction.South, p)
            self.moveboard(pointA, Direction.West, q)

    def rotationD(self, pointA: Point, pointB: Point, pointC: Point, dir: str):
        #       A
        #       |
        #       p
        #       |
        # B - q - C

        q = pointC[1] - pointB[1]
        p = pointB[0] - pointA[0]
        if dir == "CW":
            self.moveboard(pointA, Direction.South, p)
            self.moveboard(pointB, Direction.East, q)
            self.moveboard(pointA, Direction.North, p)
            self.moveboard(pointB, Direction.West, q)
        elif dir == "CCW":
            self.moveboard(pointB, Direction.East, q)
            self.moveboard(pointA, Direction.South, p)
            self.moveboard(pointB, Direction.West, q)
            self.moveboard(pointA, Direction.North, p)

    def tw(self, pointA: Point, pointB: Point, pointC: Point, dir: str):
        corner = [pointB[0]-1, pointB[1]]
        if dir == "W":
            self.rotationD(corner, pointA, pointB, "CW")
            self.rotationA(corner, pointB, pointC, "CW")
        elif dir == "E":
            self.rotationA(corner, pointB, pointC, "CCW")
            self.rotationD(corner, pointA, pointB, "CCW")

    def randomize(self):
        direcs = list(Direction)
        n = self.board.shape[0]
        for _ in range(100):
            randx = random.randint(0, n-1)
            randy = random.randint(0, n-1)
            direc = random.choice(direcs)
            amount = random.randint(1, n-1)
            elem = randx, randy
            self.moveboard(elem, direc, amount)

    def moveboard(self, elem: Point, direc: Direction, amount: int):
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

    def where(self, n: int) -> List[int]:
        found = np.where(self.board == n)
        return [found[0][0], found[1][0]]
