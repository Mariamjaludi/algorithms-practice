def canCross(stones):
    for i in range(3, len(stones)):
        if stones[i] > stones[i - 1] * 2:
            return False
    lastStone = stones[-1]
    positions = []  # stack
    jumps = []  # stack
    stonePositions = {}
    for stone in stones:
        stonePositions[stone] = True
    positions.append(0)
    jumps.append(0)
    while positions:
        position = positions.pop()
        jumpDistance = jumps.pop()
        for i in range(jumpDistance - 1, jumpDistance + 2):
            if i <= 0:
                continue
            nextPosition = position + 1
            if nextPosition == lastStone:
                return True
            elif nextPosition in stonePositions:
                positions.append(nextPosition)
                jumps.append(i)
    return False
