# coding=utf-8
import pprint
from simpleai.search import SearchProblem
from simpleai.search.local import simulated_annealing


class SolarPannels(SearchProblem):

    # Supply area of roboport MK4 = 200x200
    # We have to fit 36 substations in there (6x6 grid)
    #   Each substation is 25 tiles apart
    initial_state = ""

    def actions(self, state):
        pass

    def result(self, state, action):
        pass

    # def is_goal(self, state):
    #     pass

    def value(self, state):
        pass


class Board:
    """
    Two-dimensional board manipulation model
    The board is represented as an list of single char columns (that are lists)
    Tiles can be added to the board.
    Tiles can have different sizes.
    Tiles cannot overlap each other.
    Tiles can be moved into empty spaces. " "
    There is a special kind of tile that cannot be moved. "0"
    """
    EMPTY = '_'
    IMMOVABLE = '0'
    # Example:
    #
    # [C,C,C]
    #  C C X  --> The X is in board[2][1]
    #  C C C
    #  C C C
    #
    #    1 2 3
    #   0------> x
    # 1 |E E A
    # 2 |E E A
    # 3 |A A A
    #   |
    #   v
    #   y

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.tiles = {}
        self.board = []
        # Generate an empty board
        for x in range(width):
            column = list(self.EMPTY * height)
            self.board.append(column)

    def __repr__(self):
        lines = []
        for i in self.board:
            lines.append(''.join(i))
        return '\n'.join(lines)

    def _store_new_tile(self, x, y, width, height, char):
        """Store the info of a new tile in the index"""
        occupied_coordinates = []
        for i in range(width):
            for j in range(height):
                occupied_coordinates.append((x + i, y + j))

        self.tiles[(x, y)] = {
            'width': width,
            'height': height,
            'char': char,
            'occupied': occupied_coordinates
        }

    def add_gap(self, x, y, width, height):
        """
        Adds a gap, or immovable tile in the specified position
        Gaps are represented with a "0"
        """
        self.add_tile(x, y, width, height, self.IMMOVABLE)

    def add_tile(self, x, y, width, height, char):
        """
        Adds specified elements to the board
        """
        if self.can_fit(x, y, width, height):
            # Turn all squares into the representation of that tile
            for i in range(width):
                for j in range(height):
                    self.board[x + i][y + j] = char
            # And store its info
            self._store_new_tile(x, y, width, height, char)
        else:
            raise Exception('cannot fit')

    def can_fit(self, x, y, width, height):
        """
        Determines if an element of the specified width and height
        fits the board into the provided coordinates
        """
        values = []
        for i in range(width):
            for j in range(height):
                values.append(self.board[x + i][y + j] == self.EMPTY)
        return all(values)


if __name__ == '__main__':
    board = Board(200, 200)
    print(board.can_fit(2, 2, 100, 100))
    board.add_tile(2, 2, 100, 100, 'X')
    print(board)
    # print(board.tiles)
    # board.add_tile(3, 3, 2, 2, "A")
