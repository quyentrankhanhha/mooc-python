# Write your solution here
def column_correct(sudoku: list, column_no: int):
    numbers_checked = []
    for row in sudoku:
        if row[column_no] in numbers_checked and row[column_no] != 0:
            return False
        numbers_checked.append(row[column_no])
    return True

if __name__ == "__main__":
    sudoku = [
  [ 9, 0, 1, 0, 8, 0, 3, 0, 1 ],
  [ 2, 2, 0, 0, 5, 0, 7, 0, 0 ],
  [ 0, 2, 0, 3, 0, 0, 4, 0, 4 ],
  [ 2, 9, 4, 0, 0, 0, 2, 0, 0 ],
  [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],
  [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],
  [ 0, 0, 7, 8, 0, 3, 9, 8, 6 ],
  [ 3, 0, 1, 0, 0, 0, 0, 0, 1 ],
  [ 3, 0, 0, 0, 2, 0, 2, 0, 1 ],
    ]

    print(column_correct(sudoku, 3))
    print(column_correct(sudoku, 1))