# Write a function that takes in an array of positive integers and returns an
# integer representing the maximum sum of non-adjacent elements in the array.
# If a sum cannot be generated, the function should return 0.

def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return 0
    if len(array) == 1:
        return array[0]

    sums = [array[0], max(array[0], array[1])]
    for i in range(2, len(array)):
        currentSum = max(sum[1], sum[0] + array[i])
        sums[0] = sums[1]
        sums[1] = currentSum
    return sums[1]
