from z3 import *
from typing import List


def solve (gridInput: List[List[str]], constraints: List[List[List[int]]]) :
  """
  gridInput: List[List[str]] = [
      ['4', '', '', ''],
      ['', '', '3', ''],
      ['', '', '', ''],
      ['', '', '', ''],
  ]

  Format [[[0, 0], [1, 0]]] -> grid[0][0] > grid[1][0]
  constraints: List[List[List[int]]] = [
      [[0, 1], [1, 1]],
      [[1, 0], [2, 0]],
  ]
  """


  s = Solver()


  # Grid size
  SIZE = len(gridInput)


  grid = [ [Int(f'{r}-{c}') for c in range(SIZE)] for r in range(SIZE) ]


  # All digits are between 1 and SIZE 
  for r in range(SIZE):
      for c in range(SIZE):
          s.add(grid[r][c] >= 1)
          s.add(grid[r][c] <= SIZE)


  for r in range(SIZE):
      # All digits of a column are distincts
      s.add(Distinct([ grid[c][r] for c in range(SIZE) ]))
      # All digits of a row are distincts
      s.add(Distinct(grid[r]))


  # Complete the current grid with puzzle infos
  for r in range(SIZE):
      for c in range(SIZE):
          x = gridInput[r][c]
          if (x != ''):
              s.add(grid[r][c] == int(x))


  # Check contraints
  for c in constraints:
      s.add(grid[c[0][0]][c[0][1]] > grid[c[1][0]][c[1][1]])


  s.check()
  m = s.model()


  # Return the result
  return [[str(m.eval(grid[r][c])) for c in range(SIZE)] for r in range(SIZE)]


  # Beautiful print
  # for r in range(SIZE):
  #     print(' '.join(str(m.eval(grid[r][c])) for c in range(SIZE)))
