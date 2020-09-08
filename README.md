# suso
Python 3 Sudoku solver with GUI and the ability to solve images of Sudokus


## Examples
### Sudoku Solver
```python
from suso import Sudoku

grid = [0, 0, 0, 0, 0, 0, 6, 8, 0,
        0, 0, 0, 0, 7, 3, 0, 0, 9,
        3, 0, 9, 0, 0, 0, 0, 4, 5,
        4, 9, 0, 0, 0, 0, 0, 0, 0,
        8, 0, 3, 0, 5, 0, 9, 0, 2,
        0, 0, 0, 0, 0, 0, 0, 3, 6,
        9, 6, 0, 0, 0, 0, 3, 0, 8,
        7, 0, 0, 6, 8, 0, 0, 0, 0,
        0, 2, 8, 0, 0, 0, 0, 0, 0,]
s = Sudoku(grid)
solved = s.solve()
print(solved)
```