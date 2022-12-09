number_of_grids = int(input())
houses_index = input()

grid = list(houses_index)
is_grid_good = True

for i in range(len(grid)):
    if grid[i] == '.':
        grid[i] = 'B'

for i in range(len(grid) - 1):
    if grid[i] == 'H':
        if grid[i + 1] == 'H':
            print('NO')
            is_grid_good = False
            break

if is_grid_good:
    print('YES')
    print(''.join(grid))
