# Write your solution here
def copy_and_add(sudoku: list, row_no: int, column_no: int, number:int):
    new_sudoku = []
    for i in range(len(sudoku)):
        new_sudoku.append([])
        for j in range(len(sudoku)):
            new_sudoku[i].append(sudoku[i][j])
    new_sudoku[row_no][column_no] = number
    return new_sudoku
def  print_sudoku(sudoku: list):
    for row in range(len(sudoku)):
        if row == 3 or row == 6:
            print()
        for column in range(len(sudoku)):
            if column == 3 or column == 6:
                print("", end=" ")
            if sudoku[row][column] != 0: 
                print(sudoku[row][column], end=" ")
            else:
                print("_", end=" ")
        print()
    return 
if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)