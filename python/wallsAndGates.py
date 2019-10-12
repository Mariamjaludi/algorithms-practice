gate = 0
wall = -1

inf = float("inf")
grid = [
    [inf, -1, 0, inf],
    [inf, inf, inf, -1],
    [inf, -1, inf, -1],
    [0, -1, inf, inf]
]


def fillRooms(grid):

    if len(grid) == 0 or len(grid[0]) == 0:
        return grid

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                dfs(grid, i, j, 0)
    return grid


def dfs(grid, i, j, distance):
    if grid[i][j] < distance:
        return

    grid[i][j] = distance
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for dx, dy in directions:
        if 0 <= i + dx < len(grid) and 0 <= j + dy < len(grid[i]):
            dfs(grid, dx + i, dy + j, distance + 1)


print(fillRooms(grid))
