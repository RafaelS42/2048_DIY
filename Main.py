import fun

grid = []
y = 4
x = 4

fun.create_grid(grid, y, x)

while True:
    fun.add_num2(grid)
    fun.print_grid(grid)
    print("\n" * 3)
    n = input('go =  ')
    if n == 'w':
        fun.sum_up(grid)

    if n == 's':
        fun.sum_down(grid)

    if n == 'a':
        fun.sum_left(grid)

    if n == 'd':
        fun.sum_right(grid)

    print("\n" * 130)
