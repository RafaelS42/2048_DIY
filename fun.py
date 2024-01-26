import random

# Create a grid#


def create_grid(grid, y, x):
    for i in range(y):
        grid.append([])
        for n in range(x):
            grid[i].append(0)
    return grid

# Print the grid


def print_grid(grid):
    for line in grid:
        print(line)


# add a new number in a random place


def add_num2(grid):
    empty = []
    # verify 0 in grid
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 0:
                empty.append([y, x])

    # print("Empty places = ", (len(empty)))
    # if there is no 0 in grid return 0
    if len(empty) == 0:
        return 0
    else:
        empty_c = random.randint(0, (len(empty)-1))
        # print("Chose location = ", empty_c, empty[empty_c])
        # Add number to the grid
        grid[empty[empty_c][0]][empty[empty_c][1]] = 2


def sum_right(grid):
    can_move = False
    # Slide the nums to the right
    for y in range(len(grid)):
        for x in range(len(grid[y])-1, -1, -1):
            if ((grid[y][x]) != 0):
                for n in range(x, (len(grid[y]) - 1), 1):
                    if grid[y][n + 1] == 0:
                        can_move = True
                        grid[y][n + 1] = grid[y][n]
                        grid[y][n] = 0
                        "print('=', grid[y], y)"

                    if grid[y][n] == grid[y][n+1]:
                        can_move = True
                        "#print('+', grid[y], y)"
                        grid[y][n+1] *= 2
                        grid[y][n] = 0
                        "#print('-', grid[y], y)"
    return (can_move)

def sum_left(grid):
    can_move = False
    # Slide the nums to the left
    for y in range(len(grid)):
        for x in range(0, len(grid[y]), 1):
            if ((grid[y][x]) != 0):
                for n in range(x, 0, -1):
                        if grid[y][n - 1] == 0:
                            can_move = True
                            grid[y][n - 1] = grid[y][n]
                            grid[y][n] = 0
                            "print('=', grid[y], y)"

                        if grid[y][n] == grid[y][n - 1]:
                            can_move = True
                            "print('+', grid[y], y)"
                            grid[y][n - 1] *= 2
                            grid[y][n] = 0
                            "print('-', grid[y], y)"
    return (can_move)


def sum_up(grid):
    can_move = False
    # Slide the nums to the up
    for x in range(0, len(grid[1]), 1):
        for y in range(0, len(grid), 1):
            if (y > 0) and (y < len(grid)) and ((grid[y][x]) != 0):
                for n in range(y, 0, -1):
                    """
                     if x == 0:
                        for p in range(len(grid)):
                            print(grid[p][x])
                    print('==')
                    """
                    if grid[n - 1][x] == 0:
                        can_move = True
                        grid[n - 1][x] = grid[n][x]
                        grid[n][x] = 0
                    if grid[n][x] == grid[n - 1][x]:
                        can_move = True
                        grid[n - 1][x] *= 2
                        grid[n][x] = 0
    return(True)


def sum_down(grid):
    can_move = False
    # Slide the nums to the down
    for x in range(0, len(grid[1]), 1):
        for y in range(((len(grid)) - 1), -1, -1):
            # (y < (len(grid))-1) preventes that code run in the last line
            if ((grid[y][x]) != 0):
                for n in range(y, len(grid)-1, 1):
                    can_move = True
                    if grid[n + 1][x] == 0:
                        grid[n + 1][x] = grid[n][x]
                        grid[n][x] = 0

                    if grid[n][x] == grid[n + 1][x]:
                        can_move = True
                        grid[n + 1][x] *= 2
                        grid[n][x] = 0
    return (can_move)