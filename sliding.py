import sys
from typing import Tuple

import numpy as np
import pygame

from board import Board, Direction

SQUARESIZE = 100
n = int(input("Enter Grid Size:"))
HEIGHT = SQUARESIZE * n
WIDTH = SQUARESIZE * n


Point = Tuple[int, int]


class SlidingGame:
    def __init__(self, board: np.ndarray):
        self.board = Board(board)

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
            self.drawboard(200)
            self.moveboard(pointB, Direction.South, p)
            self.drawboard(200)
            self.moveboard(pointB, Direction.East, q)
            self.drawboard(200)
            self.moveboard(pointB, Direction.North, p)
            self.drawboard(200)

        elif dir == "CCW":
            self.moveboard(pointB, Direction.South, p)
            self.drawboard(200)
            self.moveboard(pointB, Direction.West, q)
            self.drawboard(200)
            self.moveboard(pointB, Direction.North, p)
            self.drawboard(200)
            self.moveboard(pointB, Direction.East, q)
            self.drawboard(200)

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
            self.drawboard(200)
            self.moveboard(pointA, Direction.West, q)
            self.drawboard(200)
            self.moveboard(pointA, Direction.South, p)
            self.drawboard(200)
            self.moveboard(pointA, Direction.East, q)
            self.drawboard(200)

        elif dir == "CCW":
            self.moveboard(pointA, Direction.West, q)
            self.drawboard(200)
            self.moveboard(pointA, Direction.North, p)
            self.drawboard(200)
            self.moveboard(pointA, Direction.East, q)
            self.drawboard(200)
            self.moveboard(pointA, Direction.South, p)
            self.drawboard(200)

    def rotationC(self, pointA: Point, pointB: Point, pointC: Point, dir: str):
        # A - q - B
        #         |
        #         p
        #         |
        #         C
        #

        q = pointB[1] - pointA[1]
        p = pointC[0] - pointB[0]
        if dir == "CW":
            self.moveboard(pointA, Direction.East, q)
            self.drawboard(200)
            self.moveboard(pointB, Direction.North, p)
            self.drawboard(200)
            self.moveboard(pointA, Direction.West, q)
            self.drawboard(200)
            self.moveboard(pointB, Direction.South, p)
            self.drawboard(200)

        elif dir == "CCW":
            self.moveboard(pointB, Direction.North, p)
            self.drawboard(200)
            self.moveboard(pointA, Direction.East, q)
            self.drawboard(200)
            self.moveboard(pointB, Direction.South, p)
            self.drawboard(200)
            self.moveboard(pointA, Direction.West, q)
            self.drawboard(200)

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
            self.drawboard(200)
            self.moveboard(pointB, Direction.East, q)
            self.drawboard(200)
            self.moveboard(pointA, Direction.North, p)
            self.drawboard(200)
            self.moveboard(pointB, Direction.West, q)
            self.drawboard(200)

        elif dir == "CCW":
            self.moveboard(pointB, Direction.East, q)
            self.drawboard(200)
            self.moveboard(pointA, Direction.South, p)
            self.drawboard(200)
            self.moveboard(pointB, Direction.West, q)
            self.drawboard(200)
            self.moveboard(pointA, Direction.North, p)
            self.drawboard(200)

    def tw(self, pointA: Point, pointB: Point, pointC: Point, dir: str):
        corner = [pointB[0] - 1, pointB[1]]
        if dir == "W":
            self.rotationD(corner, pointA, pointB, "CW")
            self.rotationA(corner, pointB, pointC, "CW")
        elif dir == "E":
            self.rotationA(corner, pointB, pointC, "CCW")
            self.rotationD(corner, pointA, pointB, "CCW")

    def gameover(self):
        # If game over is true, draw game over
        text = self.font.render("Game Over", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_x = self.screen.get_width() / 2 - text_rect.width / 2
        text_y = self.screen.get_height() / 2 - text_rect.height / 2
        self.screen.fill((0, 0, 0))
        self.screen.blit(text, [text_x, text_y])
        pygame.display.update()
        pygame.time.wait(1000)
        pygame.display.quit()
        pygame.quit()
        sys.exit()

    def solve(self):
        for r in range(1, n * n + 1 - n, 1):
            correctspot = [(r - 1) // n, (r - 1) % n]
            actualloc = self.board.where(r)
            if correctspot == actualloc:
                continue

            elif actualloc[1] > correctspot[1]:
                if actualloc[0] == correctspot[0]:
                    corner = [actualloc[0] + 1, actualloc[1]]
                    self.rotationC(correctspot, actualloc, corner, "CCW")
                elif actualloc[0] > correctspot[0]:
                    corner = [correctspot[0], actualloc[1]]
                    self.rotationC(correctspot, corner, actualloc, "CW")
            elif actualloc[1] < correctspot[1]:
                if actualloc[0] > correctspot[0]:
                    corner = [actualloc[0], correctspot[1]]
                    self.rotationD(correctspot, actualloc, corner, "CW")
            elif actualloc[1] == correctspot[1]:
                if actualloc[1] == n - 1:
                    corner = [actualloc[0], actualloc[1] - 1]
                    self.rotationD(correctspot, corner, actualloc, "CCW")
                elif actualloc[1] >= 0:
                    corner = [actualloc[0], actualloc[1] + 1]
                    self.rotationA(correctspot, actualloc, corner, "CW")

        for r in range(n * n - n + 1, n * n - 1, 1):
            correctspot = [(r - 1) // n, (r - 1) % n]
            actualloc = self.board.where(r)
            if correctspot == actualloc:
                continue
            if actualloc[1] == correctspot[1] + 1:
                pointC = [correctspot[0], actualloc[1] + 1]
                self.tw(correctspot, actualloc, pointC, "W")
            elif actualloc[1] - correctspot[1] > 1:
                pointC = [correctspot[0], correctspot[1] + 1]
                self.tw(correctspot, pointC, actualloc, "E")

        self.checkwin()
        # swap last two pieces
        for i in range(n - 2, -2, -2):
            self.tw([n - 1, i - 1], [n - 1, i], [n - 1, i + 1], "E")
        self.moveboard([n - 1, 0], Direction.West, 1)
        self.drawboard(200)
        self.checkwin()

    def rungame(self):
        running = True
        moved = False
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.font = pygame.font.SysFont("arial", 20)

        self.randomize()
        self.drawboard()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        print("solving")
                        self.solve()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    elemx, elemy = (
                        event.pos[0] // SQUARESIZE,
                        event.pos[1] // SQUARESIZE,
                    )

                if event.type == pygame.MOUSEBUTTONUP:
                    elem2x, elem2y = (
                        event.pos[0] // SQUARESIZE,
                        event.pos[1] // SQUARESIZE,
                    )

                    deltax = elem2x - elemx
                    deltay = elem2y - elemy

                    if deltax > 0:
                        direc = Direction.East
                        amount = deltax
                    elif deltax < 0:
                        direc = Direction.West
                        amount = deltax
                    elif deltay < 0:
                        direc = Direction.North
                        amount = deltay
                    elif deltay > 0:
                        direc = Direction.South
                        amount = deltay
                    moved = deltax != 0 or deltay != 0
                if moved:
                    elem = elemy, elemx
                    self.moveboard(elem, direc, amount)
                    moved = False
                    self.drawboard()

                self.checkwin()

    def randomize(self):
        self.board.randomize()

    def checkwin(self):
        solved = np.arange(1, n * n + 1, 1)
        solved.resize((n, n))
        if np.array_equal(solved, self.board.board):
            self.gameover()

    def drawboard(self, delay: int = 0):
        self.screen.fill((0, 0, 0))
        for x in range(n):
            for y in range(n):
                pygame.draw.rect(
                    self.screen,
                    (255, 255, 255),
                    [x * SQUARESIZE, y * SQUARESIZE, SQUARESIZE, SQUARESIZE],
                    3,
                )
                numtxt = str(self.board.board[y][x])
                img = self.font.render(numtxt, True, (255, 255, 255))
                posx, posy = int(x * SQUARESIZE + SQUARESIZE // 3), int(
                    y * SQUARESIZE + SQUARESIZE // 3
                )
                self.screen.blit(img, (posx, posy))
        pygame.display.update()
        if delay > 0:
            pygame.time.wait(delay)

    def moveboard(self, elem: Point, direc: Direction, amount: int):
        self.board.moveboard(elem, direc, amount)


if __name__ == "__main__":
    matrix = np.arange(1, n * n + 1, 1)
    matrix.resize((n, n))
    game = SlidingGame(matrix)
    game.rungame()
