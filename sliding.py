import sys

import numpy as np
import pygame

from board import Board, Direction, RotationDirection, TwistDirection

SQUARESIZE = 100
n = int(input("Enter Grid Size:"))
HEIGHT = SQUARESIZE * n
WIDTH = SQUARESIZE * n


Point = tuple[int, int]


class SlidingGame:
    def __init__(self, board: np.ndarray):
        """Initialize the Pygame game with a board state.

        Args:
            board: The initial NumPy puzzle array.
        """
        self.board = Board(board)

    def rotationA(
        self,
        pointA: Point,
        pointB: Point,
        pointC: Point,
        direction: RotationDirection,
    ):
        """Animate an A-shaped board rotation.

        Args:
            pointA: The first point of the configuration.
            pointB: The center point of the configuration.
            pointC: The third point of the configuration.
            direction: The clockwise or counterclockwise rotation direction.

        Returns:
            The wrapped board after the rotation.
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
            self.drawboard(delay=200)
            self.moveboard(pointB, Direction.South, p)
            self.drawboard(delay=200)
            self.moveboard(pointB, Direction.East, q)
            self.drawboard(delay=200)
            self.moveboard(pointB, Direction.North, p)
            self.drawboard(delay=200)

        elif direction == RotationDirection.CCW:
            self.moveboard(pointB, Direction.South, p)
            self.drawboard(delay=200)
            self.moveboard(pointB, Direction.West, q)
            self.drawboard(delay=200)
            self.moveboard(pointB, Direction.North, p)
            self.drawboard(delay=200)
            self.moveboard(pointB, Direction.East, q)
            self.drawboard(delay=200)

        return self.board

    def rotationB(
        self,
        pointA: Point,
        pointB: Point,
        pointC: Point,
        direction: RotationDirection,
    ):
        """Animate a B-shaped board rotation.

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
            self.drawboard(delay=200)
            self.moveboard(pointA, Direction.West, q)
            self.drawboard(delay=200)
            self.moveboard(pointA, Direction.South, p)
            self.drawboard(delay=200)
            self.moveboard(pointA, Direction.East, q)
            self.drawboard(delay=200)

        elif direction == RotationDirection.CCW:
            self.moveboard(pointA, Direction.West, q)
            self.drawboard(delay=200)
            self.moveboard(pointA, Direction.North, p)
            self.drawboard(delay=200)
            self.moveboard(pointA, Direction.East, q)
            self.drawboard(delay=200)
            self.moveboard(pointA, Direction.South, p)
            self.drawboard(delay=200)

    def rotationC(
        self,
        pointA: Point,
        pointB: Point,
        pointC: Point,
        direction: RotationDirection,
    ):
        """Animate a C-shaped board rotation.

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
            self.drawboard(delay=200)
            self.moveboard(pointB, Direction.North, p)
            self.drawboard(delay=200)
            self.moveboard(pointA, Direction.West, q)
            self.drawboard(delay=200)
            self.moveboard(pointB, Direction.South, p)
            self.drawboard(delay=200)

        elif direction == RotationDirection.CCW:
            self.moveboard(pointB, Direction.North, p)
            self.drawboard(delay=200)
            self.moveboard(pointA, Direction.East, q)
            self.drawboard(delay=200)
            self.moveboard(pointB, Direction.South, p)
            self.drawboard(delay=200)
            self.moveboard(pointA, Direction.West, q)
            self.drawboard(delay=200)

    def rotationD(
        self,
        pointA: Point,
        pointB: Point,
        pointC: Point,
        direction: RotationDirection,
    ):
        """Animate a D-shaped board rotation.

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
            self.drawboard(delay=200)
            self.moveboard(pointB, Direction.East, q)
            self.drawboard(delay=200)
            self.moveboard(pointA, Direction.North, p)
            self.drawboard(delay=200)
            self.moveboard(pointB, Direction.West, q)
            self.drawboard(delay=200)

        elif direction == RotationDirection.CCW:
            self.moveboard(pointB, Direction.East, q)
            self.drawboard(delay=200)
            self.moveboard(pointA, Direction.South, p)
            self.drawboard(delay=200)
            self.moveboard(pointB, Direction.West, q)
            self.drawboard(delay=200)
            self.moveboard(pointA, Direction.North, p)
            self.drawboard(delay=200)

    def tw(
        self,
        pointA: Point,
        pointB: Point,
        pointC: Point,
        direction: TwistDirection,
    ):
        """Animate a corner twist.

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

    def gameover(self):
        """Display the game-over screen and exit the process."""
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
        """Solve the current puzzle using board rotations."""
        for r in range(1, n * n + 1 - n, 1):
            correctspot = ((r - 1) // n, (r - 1) % n)
            actualloc = self.board.where(r)
            if correctspot == actualloc:
                continue

            elif actualloc[1] > correctspot[1]:
                if actualloc[0] == correctspot[0]:
                    corner = (actualloc[0] + 1, actualloc[1])
                    self.rotationC(
                        correctspot, actualloc, corner, RotationDirection.CCW
                    )
                elif actualloc[0] > correctspot[0]:
                    corner = (correctspot[0], actualloc[1])
                    self.rotationC(correctspot, corner, actualloc, RotationDirection.CW)
            elif actualloc[1] < correctspot[1]:
                if actualloc[0] > correctspot[0]:
                    corner = (actualloc[0], correctspot[1])
                    self.rotationD(correctspot, actualloc, corner, RotationDirection.CW)
            elif actualloc[1] == correctspot[1]:
                if actualloc[1] == n - 1:
                    corner = (actualloc[0], actualloc[1] - 1)
                    self.rotationD(correctspot, corner, actualloc, RotationDirection.CCW)
                elif actualloc[1] >= 0:
                    corner = (actualloc[0], actualloc[1] + 1)
                    self.rotationA(correctspot, actualloc, corner, RotationDirection.CW)

        for r in range(n * n - n + 1, n * n - 1, 1):
            correctspot = ((r - 1) // n, (r - 1) % n)
            actualloc = self.board.where(r)
            if correctspot == actualloc:
                continue
            if actualloc[1] == correctspot[1] + 1:
                pointC = (correctspot[0], actualloc[1] + 1)
                self.tw(correctspot, actualloc, pointC, TwistDirection.West)
            elif actualloc[1] - correctspot[1] > 1:
                pointC = (correctspot[0], correctspot[1] + 1)
                self.tw(correctspot, pointC, actualloc, TwistDirection.East)

        self.checkwin()
        # swap last two pieces
        for i in range(n - 2, -2, -2):
            self.tw(
                (n - 1, i - 1),
                (n - 1, i),
                (n - 1, i + 1),
                TwistDirection.East,
            )
        self.moveboard((n - 1, 0), Direction.West, 1)
        self.drawboard(delay=200)
        self.checkwin()

    def rungame(self):
        """Initialize Pygame and run the main game loop."""
        running = True
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.font = pygame.font.SysFont("arial", 20)

        self.randomize()
        self.drawboard()

        drag_start = None
        drag_elem = None
        drag_direction = None
        drag_offset = 0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    print("solving")
                    self.solve()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    elemx, elemy = (
                        event.pos[0] // SQUARESIZE,
                        event.pos[1] // SQUARESIZE,
                    )
                    drag_start = event.pos
                    drag_elem = (elemy, elemx)
                    drag_direction = None
                    drag_offset = 0

                if event.type == pygame.MOUSEMOTION and drag_start is not None:
                    dx = event.pos[0] - drag_start[0]
                    dy = event.pos[1] - drag_start[1]

                    if abs(dx) >= abs(dy):
                        if abs(dx) > 4:
                            drag_direction = Direction.East if dx > 0 else Direction.West
                        drag_offset = dx
                    else:
                        if abs(dy) > 4:
                            drag_direction = Direction.South if dy > 0 else Direction.North
                        drag_offset = dy

                    if drag_direction is not None:
                        self.drawboard(drag_elem, drag_direction, drag_offset)

                if event.type == pygame.MOUSEBUTTONUP:
                    if drag_start is not None and drag_elem is not None:
                        dx = event.pos[0] - drag_start[0]
                        dy = event.pos[1] - drag_start[1]

                        if abs(dx) >= abs(dy):
                            delta = dx
                            direc = Direction.East if delta > 0 else Direction.West
                        else:
                            delta = dy
                            direc = Direction.South if delta > 0 else Direction.North

                        amount = min(n - 1, int(abs(delta) / SQUARESIZE + 0.5))
                        if amount > 0:
                            target_offset = amount * SQUARESIZE
                            if delta < 0:
                                target_offset = -target_offset
                        else:
                            target_offset = 0

                        start_offset = drag_offset
                        for step in range(1, 7):
                            progress = step / 6
                            eased = 1 - (1 - progress) * (1 - progress)
                            current_offset = start_offset + (
                                target_offset - start_offset
                            ) * eased
                            self.drawboard(drag_elem, direc, current_offset)
                            pygame.time.wait(12)

                        if amount > 0:
                            self.moveboard(drag_elem, direc, amount)

                        drag_start = None
                        drag_elem = None
                        drag_direction = None
                        drag_offset = 0
                        self.drawboard()

                self.checkwin()

    def randomize(self):
        """Scramble the wrapped board."""
        self.board.randomize()

    def checkwin(self):
        """End the game if the board matches the solved state."""
        solved = np.arange(1, n * n + 1, 1).reshape((n, n))
        if np.array_equal(solved, self.board.board):
            self.gameover()

    def drawboard(
        self,
        drag_elem: Point | None = None,
        drag_direction: Direction | None = None,
        drag_offset: float = 0,
        delay: int = 0,
    )->None:
        """Draw the board and any active drag animation.

        Args:
            drag_elem: The row or column currently being dragged.
            drag_direction: The direction of the active drag.
            drag_offset: The pixel offset of the active drag.
            delay: The number of milliseconds to wait after drawing.
        """
        self.screen.fill((0, 0, 0))
        for x in range(n):
            for y in range(n):
                pygame.draw.rect(
                    self.screen,
                    (255, 255, 255),
                    [x * SQUARESIZE, y * SQUARESIZE, SQUARESIZE, SQUARESIZE],
                    3,
                )

                dragged_row = (
                    drag_elem is not None
                    and drag_direction in (Direction.East, Direction.West)
                    and y == drag_elem[0]
                )
                dragged_column = (
                    drag_elem is not None
                    and drag_direction in (Direction.North, Direction.South)
                    and x == drag_elem[1]
                )
                if dragged_row or dragged_column:
                    continue

                self.draw_number(self.board.board[y][x], x * SQUARESIZE, y * SQUARESIZE)

        if drag_elem is not None and drag_direction is not None:
            if drag_direction in (Direction.East, Direction.West):
                row = drag_elem[0]
                for x in range(n):
                    numtxt = self.board.board[row][x]
                    for copy in range(-2, 3):
                        posx = x * SQUARESIZE + drag_offset + copy * WIDTH
                        self.draw_number(numtxt, posx, row * SQUARESIZE)
            elif drag_direction in (Direction.North, Direction.South):
                column = drag_elem[1]
                for y in range(n):
                    numtxt = self.board.board[y][column]
                    for copy in range(-2, 3):
                        posy = y * SQUARESIZE + drag_offset + copy * HEIGHT
                        self.draw_number(numtxt, column * SQUARESIZE, posy)

        pygame.display.update()
        if delay > 0:
            pygame.time.wait(delay)

    def draw_number(self, numtxt: int, posx: float, posy: float)->None:
        """Draw a puzzle value at a screen position.

        Args:
            numtxt: The number to render.
            posx: The horizontal position of the number.
            posy: The vertical position of the number.
        """
        img = self.font.render(str(numtxt), True, (255, 255, 255))
        textposx = int(posx + SQUARESIZE // 3)
        textposy = int(posy + SQUARESIZE // 3)
        self.screen.blit(img, (textposx, textposy))

    def moveboard(self, elem: Point, direc: Direction, amount: int)->None:
        """Move a board row or column.

        Args:
            elem: The row and column of the line to move.
            direc: The direction in which to move the line.
            amount: The number of positions to move.
        """
        self.board.moveboard(elem, direc, amount)


if __name__ == "__main__":
    matrix = np.arange(1, n * n + 1, 1).reshape((n, n))
    game = SlidingGame(matrix)
    game.rungame()
