column = 9
row = 9

# grid init
# puzzle_map = [[0 for i in range(column)] for j in range(row)]


# setting map
puzzle_map = [[0, 0, 0, 2, 6, 0, 7, 0, 1],
              [6, 8, 0, 0, 7, 0, 0, 9, 0],
              [1, 9, 0, 0, 0, 4, 5, 0, 0],
              [8, 2, 0, 1, 0, 0, 0, 4, 0],
              [0, 0, 4, 6, 0, 2, 9, 0, 0],
              [0, 5, 0, 0, 0, 3, 0, 2, 8],
              [0, 0, 9, 3, 0, 0, 0, 7, 4],
              [0, 4, 0, 0, 5, 0, 0, 3, 6],
              [7, 0, 3, 0, 1, 8, 0, 0, 0]]


# printing map, y = number of rows
def printing(grid, y):
    for i in range(y):
        print(grid[i])


# manually enter map (not recommended :D)
# x = number of columns, y = number of rows
def creating_puzzle_map(grid, x, y):
    for i in range(y):
        for j in range(x):
            grid[i][j] = input('grid[{}][{}]: '.format(j+1, i+1))


# finds next blank cell to fill
# x = number of columns, y = number of rows
def finding_blank_cell(grid, x, y):
    for i in range(y):
        for j in range(x):
            if grid[i][j] == 0:
                # if cell is empty return it's coordinates
                return i, j
            else:
                pass
    return False


# checks whether chosen number = num is valid choice within row, column, sector
# i = num row, j = num column
# x = number of columns, y = number of rows
def validate_number(grid, i, j, num, x, y):
    valid_row = all(num != grid[i][var] for var in range(0, x))
    if valid_row is True:
        valid_column = all(num != grid[var][j] for var in range(0, y))
        if valid_column is True:
            vari = 3 * (i//3)
            varj = 3 * (j//3)
            for n in range(vari, vari+3):
                for m in range(varj, varj+3):
                    if grid[n][m] == num:
                        return False
            return True
    return False


print(validate_number(puzzle_map, 0, 5, 5, column, row))