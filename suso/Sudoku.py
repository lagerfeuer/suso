import copy
from collections import Counter

class NoSolution(RuntimeError):
    pass


class Sudoku():
    """
    Represents an unsolved or solved Sudoku game.
    """

    def __init__(self, data):
        if isinstance(data, Sudoku):
            # copy constructor
            self.data = copy.deepcopy(data.data)
        elif not isinstance(data, list):
            raise TypeError("Data must be in list form.")

        if len(data) in [9, 81]:
            if len(data) == 9:
                if not all(len(row) == 9 for row in data):
                    raise ValueError("Rows must contain 9 columns.")
                else:
                    self.data = data
            else:
                self.data = [data[i:i+9] for i in range(0, 81, 9)]
        else:
            raise ValueError(
                "Either a single list of size 81 or a list of 9 rows each with 9 columns is required.")

        if not all(isinstance(x, int) for row in self.data for x in row):
            raise TypeError("Values must be integers.")
        if not all(0 <= x <= 9 for row in self.data for x in row):
            raise ValueError(
                "Values must be valid Sudoku values (1-9) or 0 to indicate an empty field.")

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.data == other.data
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        delim = "+---+---+---+"
        string = []

        for ri, row in enumerate(self.data):
            if ri % 3 == 0:
                string.append(delim)

            tmp = []
            for ci, c in enumerate(row):
                if ci % 3 == 0:
                    tmp.append("|")
                tmp.append(str(c))

            string.append("".join(tmp) + "|")

        string.append(delim)
        return "\n".join(string)

    def check(self, grid=None):
        """
        Checks whether current Sudoku is valid or not.
        Fields may be empty, the Sudoku is considered valid but unsolved.
        :param grid: optionally pass grid different than self.data
        :return: True or False
        """
        if grid is None:
            grid = self.data

        def _check(lst):
            c = Counter(lst)
            del c[0]
            if not all(count == 1 for count in c.values()):
                return False
            return True

        valid = True
        for i in range(9):
            row = grid[i]
            column = [grid[j][i] for j in range(9)]
            square = [grid[y][x]
                      for y in range((i % 3) * 3, ((i % 3) * 3) + 3)
                      for x in range(i // 3 * 3, i // 3 * 3 + 3)]
            valid = valid and all(_check(x) for x in [row, column, square])
        return valid


    def solve(self, all=False):
        """
        Solve the Sudoku.
        :param all: whether or not to return ALL solutions as array or just the first solution
        :return: a new Sudoku object, representing the solution
        """
        def _solve(s, idx=0):
            if idx >= 81:
                return True
            row = idx // 9
            col = idx % 9

            if s[row][col] != 0:
                return _solve(s, idx + 1)

            for val in range(1,10):
                s[row][col] = val
                if not self.check(grid=s):
                    s[row][col] = 0
                    continue
                if _solve(s, idx + 1):
                    return True
                s[row][col] = 0
            
            return False # backtrack
                
        grid = copy.deepcopy(self.data)
        if not _solve(grid):
            raise NoSolution("Could not find a solved.")
        return Sudoku(grid)

