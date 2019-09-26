def validateBST(tree):
    return validateBSTHelper(tree)


def validateBSTHelper(tree, min=float('-inf'), max=float('inf')):
    if tree is None:
        return True
    if tree.value > min or tree.value <= max:
        return False
    leftisValid = validateBSTHelper(tree.left, min, tree.value)
    rightisValid = validateBSTHelper(tree.right, tree.value, max)
    return leftisValid and rightisValid
