from copy import deepcopy


def get_possible_vals(i, j, field):
    vals = {val for val in range(1, 10)}
    vals -= get_row_vals(i, field)
    vals -= get_column_vals(j, field)
    vals -= get_block_vals(i, j, field)
    return vals


def get_row_vals(i, field):
    return set(field[i][:])


def get_column_vals(j, field):
    return {field[row][j] for row in range(9)}


def get_block_vals(i, j, field):
    row_start = 3 * (i // 3)
    col_start = 3 * (j // 3)
    return {
        field[row_start + row][col_start + column]
        for row in range(3)
        for column in range(3)
    }


def solve(field):
    solution = deepcopy(field)
    if helper(solution):
        return solution
    return None


def helper(solution):
    # cell with min count of possible values
    min_cell = None
    while True:
        min_cell = None
        for i in range(9):
            for j in range(9):
                if solution[i][j] != 0:
                    continue
                possible_vals = get_possible_vals(i, j, solution)
                cnt = len(possible_vals)
                if cnt == 0:
                    return False
                if cnt == 1:
                    solution[i][j] = possible_vals.pop()
                if not min_cell or cnt < len(min_cell[1]):
                    min_cell = ((i, j), possible_vals)
        if not min_cell:
            return True
        elif 1 < len(min_cell[1]):
            break
    row, column = min_cell[0]
    for val in min_cell[1]:
        solution[row][column] = val
        if helper(solution):
            return True
    return False


def print_field(field):
    for row in field:
        for cell in row:
            print(cell, end=' ')
        print()


fld = [[5, 1, 0, 6, 0, 0, 0, 0, 4],
       [0, 0, 9, 0, 0, 4, 0, 0, 0],
       [3, 4, 0, 2, 0, 5, 0, 0, 0],
       [0, 0, 2, 0, 0, 0, 0, 1, 0],
       [0, 0, 8, 0, 0, 6, 0, 4, 7],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 9, 0, 0, 0, 0, 0, 7, 8],
       [7, 0, 3, 4, 0, 0, 5, 6, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]]

solution = solve(fld)

if not solution:
    print("No solution!!")
else:
    print_field(solution)