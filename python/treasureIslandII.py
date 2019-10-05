# Treasure Island II
# You have a map that marks the locations of treasure islands. Some of the map
# area has jagged rocks and dangerous reefs. Other areas are safe to sail in.
# There are other explorers trying to find the treasure. So you must figure out
# a shortest route to one of the treasure island.
# Assume the map area is a two dimensional grid, represented by a matrix of
# characters. You must start from one of the starting point(marked as 'S') of
# the map and can move one block up, down, left or right at a time. The treasure
# island is marked as ‘X’ in a block of the matrix. Any block with dangerous
# rocks or reefs will be marked as ‘D’. You must not enter dangerous blocks. You
# cannot leave the map area. Other areas ‘O’ are safe to sail in. Output the
# minimum number of steps to get to any of the treasure.
from collections import deque

treasureM = [
    ['S', 'O', 'O', 'S', 'S'],
    ['D', 'O', 'D', 'O', 'D'],
    ['O', 'O', 'O', 'O', 'X'],
    ['X', 'D', 'D', 'O', 'O'],
    ['X', 'D', 'D', 'D', 'O']
]


def treasureIslandII(maze):
    if len(maze) == 0 or len(maze[0]) == 0:
        return -1
    allPaths = []
    startingPoints = findStart(maze)
    for s in startingPoints:
        shortest = findPath(maze, s)
        allPaths.append(shortest)
    return min(allPaths)


def findStart(maze):
    s = []
    visited = [[False for col in row] for row in maze]
    nrows, ncols = len(maze), len(maze[0])
    q = deque([[0, 0]]) # put starting position in queue
    visited[0][0] = True # set starting position as seen
    while q:
        x, y = q.popleft() # get the current node
        if maze[x][y] == "S":
            s.append([x, y]) # if its an s, add it to our collection
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for dx, dy in directions:
            if 0 <= x + dx < nrows and 0 <= y + dy < ncols and not visited[x + dx][y + dy]:
                visited[x + dx][y + dy] = True
                q.append([x + dx, y + dy])
    return s


def findPath(maze, s):
    visited = [row[:] for row in maze]
    nrows, ncols = len(maze), len(maze[0])

    q = deque([((s[0], s[1]), 0)])
    visited[s[0]][s[1]] = "D"

    while q:
        (x, y), path = q.popleft()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for dx, dy in directions:
            if 0 <= dx + x < nrows and 0 <= dy + y < ncols:
                if visited[x + dx][y + dy] == "X":
                    return path + 1
                elif visited[x + dx][y + dy] == "O" or visited[x + dx][y + dy] == "S":
                    visited[x + dx][y + dy] = "D"
                    q.append(((x + dx, y + dy), path + 1))
    return -1

print(treasureIslandII(treasureM))    
