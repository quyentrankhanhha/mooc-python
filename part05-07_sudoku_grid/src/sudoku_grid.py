# Write your solution here
def get_row(grid, row_idx):
    return grid[row_idx]

def get_col(grid, col_idx):
    return [row[col_idx] for row in grid]

def get_block(grid, block_idx):
    start_row = (block_idx // 3) * 3
    start_col = (block_idx % 3) * 3
    return [grid[row][col] for row in range(start_row, start_row+3) for col in range(start_col, start_col+3)]

def check_sequence(seq):
    seen = set()
    for num in seq:
        if num == 0:
            continue
        if num in seen:
            return False
        seen.add(num)
    return True

def sudoku_grid_correct(sudoku):
    for i in range(9):
        if not check_sequence(get_row(sudoku, i)):
            return False
        if not check_sequence(get_col(sudoku, i)):
            return False
        if not check_sequence(get_block(sudoku, i)):
            return False
    return True

if __name__ == "__main__":
  sudoku1 = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
  ]

  print(sudoku_grid_correct(sudoku1))

  sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
  ]

  print(sudoku_grid_correct(sudoku2))