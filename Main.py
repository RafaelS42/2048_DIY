import fun

#grid = []
grid = [
[64, 32, 16, 2],
[16, 8, 4, 0],
[8, 4, 0, 0],
[4, 0, 0, 0]]
y = 4
x = 4

#fun.create_grid(grid, y, x)

can_move = False
#fun.add_num2(grid)

while True:


    print(can_move)
    if can_move == True:
      fun.add_num2(grid)
    
    fun.print_grid(grid)
    print("\n" * 3)

    n = input('go =  ')
    if n == 'w':
        can_move = fun.sum_up(grid)

    if n == 's':
        can_move = fun.sum_down(grid)

    if n == 'a':
        can_move = fun.sum_left(grid)

    if n == 'd':
        can_move = fun.sum_right(grid)

    if n == 'q':
        ab = []
        grid = fun.create_grid(ab, y, x)
        
    print("\n" * 130)
