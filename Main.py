column = 9
row = 9

puzzle_map = [[0 for i in range(column)] for j in range(row)]


# printing map
def printing(grid, y):
    for i in range(y):
        print(grid[i])


# manually enter map
def creating_puzzle_map(grid, x, y):
    for i in range(y):
        for j in range(x):
            grid[i][j] = input('grid[{}][{}]: '.format(j+1, i+1))
    return grid


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


printing(puzzle_map, row)


def finding_blank_cell(grid, x, y):
    for i in range(y):
        for j in range(x):
            if grid[i][j] == 0:
                # if cell is empty return it's coordinates
                return i, j
            else:
                pass
    return False


print(finding_blank_cell(puzzle_map, column, row))
