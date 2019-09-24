def subarraySort(array):
    # Write your code here.
    minOutOfOrder = float('inf')
    maxOutOfOrder = float('-inf')

    for i in range(len(array)):
        num = array[i]
        if isOutOfOrder(i, num, array):
            minOutOfOrder = min(minOutOfOrder, num)
            maxOutOfOrder = max(maxOutOfOrder, num)
    if minOutOfOrder == float('inf'):
        return [-1, -1]

    left = 0
    right = len(array) - 1

    while minOutOfOrder >= array[left]:
        left += 1
    while maxOutOfOrder <= array[right]:
        right -= 1
    return [left, right]


def isOutOfOrder(i, num, array):
    if i == 0:
        return num > array[i + 1]
    if i == len(array) - 1:
        return num < array[i - 1]
    return num > array[i + 1] or num < array[i - 1]
