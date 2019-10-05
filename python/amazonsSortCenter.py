# Amazon’s Sort Center
# In Amazon’s sort center, a computer system decides what packages are to be
# loaded on what trucks. All rooms and spaces are abstracted into space units
# which is represented as an integer. For each type of truck, they have
# different space units. For each package, they will be occupying different
# space units. As a software development engineer in sort centers, you will need
# to write a method:

# Given truck space units and a list of product space units, find out exactly
# TWO products that fit into the truck. You will also implement an internal rule
# that the truck has to reserve exactly 30 space units for safety purposes. Each
# package is assigned a unique ID, numbered from 0 to N-1.

# Assumptions:
# You will pick up exactly 2 packages.
# You cannot pick up one package twice.
# If you have multiple pairs, select the pair with the largest package.

truckSpace = 80
packagesSpace = [1, 10, 25, 35, 60]

def packages(truckSpace, pSpace):
    tS = truckSpace - 30  # 50
    sums = {}
    matched = False
    while not matched:
        for i in range(len(pSpace)):
            print("current:", pSpace[i])
            print("tS", tS)
            potentialMatch = tS - pSpace[i]
            if potentialMatch in sums:
                matched = True
                return sorted([sums[potentialMatch], i])
            else:
                sums[pSpace[i]] = i
        tS -= 1
    return []


print(packages(truckSpace, packagesSpace))
