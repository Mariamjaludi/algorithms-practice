# You have a map that marks the location of a treasure island. Some of the map
# area has jagged rocks and dangerous reefs. Other areas are safe to sail in.
# There are other explorers trying to find the treasure. So you must figure out
# a shortest route to the treasure island. Assume the map area is a two
# dimensional grid, represented by a matrix of characters. You must start from
# the top-left corner of the map and can move one block up, down, left or right
# at a time. The treasure island is marked as ‘X’ in a block of the matrix. ‘X’
# will not be at the top-left corner. Any block with dangerous rocks or reefs
# will be marked as ‘D’. You must not enter dangerous blocks. You cannot leave
# the map area. Other areas ‘O’ are safe to sail in. The top-left corner is
# always safe. Output the minimum number of steps to get to the treasure.
from collections import deque
treasureMap = [
    ["D", "O", "O", "O", "D", "O", "D", "X"],
    ["O", "O", "D", "O", "D", "O", "O", "O"],
    ["O", "D", "O", "O", "O", "D", "O", "D"],
    ["O", "O", "O", "D", "O", "D", "O", "D"],
    ["O", "D", "O", "D", "O", "D", "O", "D"],
    ["O", "O", "D", "D", "O", "D", "O", "O"],
    ["D", "O", "O", "O", "O", "O", "D", "O"],
    ["O", "O", "D", "D", "D", "O", "O", "O"]
]
smap = [
    ['O', 'O', 'O', 'O'],
    ['D', 'O', 'D', 'O'],
    ['O', 'O', 'O', 'O'],
    ['X', 'D', 'D', 'O']
]

# step one make a copy of our maze


def findTreasure(treasureMap):
    # if the map is empty, return -1
    if len(treasureMap) == 0 or len(treasureMap[0]) == 0:
        return -1  # impossible
    # make a copy of the map to edit
    visited = [row[:] for row in treasureMap]
    # get the total rows and cols
    nrows, ncols = len(visited), len(visited[0])
    # set up queue to start BFS
    q = deque([((0, 0), 0)])  # ((x, y), step)
    # Mark the start point as seen by setting it to danger so we dont go back
    visited[0][0] = "D"
    # while we have points in our queue
    while q:
        # get the coordinates and path length
        (x, y), path = q.popleft()
        # we can go right, left, up, or down
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # for each direction
        for dx, dy in directions:
            # if we add the direction to the current coordinates, are we still in the map?
            if 0 <= x + dx < nrows and 0 <= y + dy < ncols:
                # if the neighbor is X, we have found the path
                if visited[x + dx][y + dy] == "X":
                    return path + 1
                # if the neighbor is O lets keep going, set the neighbor to D (seen)
                elif visited[x + dx][y + dy] == "O":
                    visited[x + dx][y + dy] == "D"
                    # add the neighbor to our queue because we need to explore its neighbors
                    q.append(((x + dx, y + dy), path + 1))
    return -1


print(findTreasure(smap))
