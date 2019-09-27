# You're given three inputs, all of which are instances of a class that have an
# "ancestor" property pointing to their youngest ancestor. The first input is
# the top ancestor in an ancestral tree (i.e., the only instance that has no
# ancestor), and the other two inputs are descendants in the ancestral tree.
# Write a function that returns the youngest common ancestor to the two
# descendants.


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    d1depth = findDepth(descendantOne, topAncestor)
    d2depth = findDepth(descendantTwo, topAncestor)
    diff = abs(d1depth - d2depth)
    if d1depth > d2depth:
        descendantOne = levelDescendants(descendantOne, diff)
    elif d1depth < d2depth:
        descendantTwo = levelDescendants(descendantTwo, diff)

    while descendantOne != topAncestor and descendantTwo != topAncestor:
        if descendantOne == descendantTwo:
            return descendantOne
        else:
            descendantOne = descendantOne.ancestor
            descendantTwo = descendantTwo.ancestor
    return topAncestor


def findDepth(node, topAncestor):
    depth = 0
    while node != topAncestor:
        node = node.ancestor
        depth += 1
    return depth


def levelDescendants(descendant, difference):
    while difference > 0:
        descendant = descendant.ancestor
        difference -= 1
    return descendant
