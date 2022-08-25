import unittest

import numpy as np

from board import Board, Direction


class TestBoardMethods(unittest.TestCase):

    def setUp(self) -> None:
        self.board = Board(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    def test_moveboard_right(self):
        self.board.moveboard([0, 0], Direction.East, 1)
        np.testing.assert_array_equal(
            self.board.board, np.array([[3, 1, 2], [4, 5, 6], [7, 8, 9]]))

    def test_moveboard_up(self):
        self.board.moveboard([0, 0], Direction.North, 1)
        np.testing.assert_array_equal(
            self.board.board, np.array([[4, 2, 3], [7, 5, 6], [1, 8, 9]]))

    def test_moveboard_down(self):
        self.board.moveboard([0, 0], Direction.South, 1)
        np.testing.assert_array_equal(
            self.board.board, np.array([[7, 2, 3], [1, 5, 6], [4, 8, 9]]))

    def test_moveboard_left(self):
        self.board.moveboard([0, 0], Direction.West, 1)
        np.testing.assert_array_equal(
            self.board.board, np.array([[2, 3, 1], [4, 5, 6], [7, 8, 9]]))

    def test_rotationA_cw(self):
        self.board.rotationA([0, 0], [1, 0], [1, 1], "CW")
        np.testing.assert_array_equal(
            self.board.board, np.array([[4, 2, 3], [5, 1, 6], [7, 8, 9]]))

    def test_rotationA_ccw(self):
        self.board.rotationA([0, 0], [1, 0], [1, 1], "CCW")
        np.testing.assert_array_equal(
            self.board.board, np.array([[5, 2, 3], [1, 4, 6], [7, 8, 9]]))

    def test_rotationB_cw(self):
        self.board.rotationB([0, 0], [0, 1], [1, 0], "CW")
        np.testing.assert_array_equal(
            self.board.board, np.array([[4, 1, 3], [2, 5, 6], [7, 8, 9]]))

    def test_rotationB_ccw(self):
        self.board.rotationB([0, 0], [0, 1], [1, 0], "CCW")
        np.testing.assert_array_equal(
            self.board.board, np.array([[2, 4, 3], [1, 5, 6], [7, 8, 9]]))

    def test_rotationC_cw(self):
        self.board.rotationC([0, 0], [0, 1], [1, 1], "CW")
        np.testing.assert_array_equal(
            self.board.board, np.array([[5, 1, 3], [4, 2, 6], [7, 8, 9]]))

    def test_rotationC_ccw(self):
        self.board.rotationC([0, 0], [0, 1], [1, 1], "CCW")
        np.testing.assert_array_equal(
            self.board.board, np.array([[2, 5, 3], [4, 1, 6], [7, 8, 9]]))

    def test_rotationD_cw(self):
        self.board.rotationD([0, 1], [1, 0], [1, 1], "CW")
        np.testing.assert_array_equal(
            self.board.board, np.array([[1, 4, 3], [5, 2, 6], [7, 8, 9]]))

    def test_rotationD_ccw(self):
        self.board.rotationD([0, 1], [1, 0], [1, 1], "CCW")
        np.testing.assert_array_equal(
            self.board.board, np.array([[1, 5, 3], [2, 4, 6], [7, 8, 9]]))

    def test_tw_w(self):
        self.board.tw([2, 0], [2, 1], [2, 2], "W")
        np.testing.assert_array_equal(
            self.board.board, np.array([[1, 2, 3], [4, 5, 6], [8, 9, 7]]))

    def test_tw_e(self):
        self.board.tw([2, 0], [2, 1], [2, 2], "E")
        np.testing.assert_array_equal(
            self.board.board, np.array([[1, 2, 3], [4, 5, 6], [9, 7, 8]]))


if __name__ == "__main__":
    unittest.main()
