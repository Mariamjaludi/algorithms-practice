def findClosestValueInBst(tree, target):
    # Write your code here.
	closest = float('inf')
	current = tree
	while current is not None:
		currentV = current.value
		diff = abs(currentV - target)
		if diff < abs(closest - target):
			closest = current.value
		if currentV == target:
			return current.value
		elif currentV < target:
			current = current.right
		elif currentV > target:
			current = current.left
	return closest
