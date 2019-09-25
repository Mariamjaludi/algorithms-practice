# Merge Sort: O(nlog(n)) time complexity
def mergeSort(array):
    # Base case:
    if len(array) == 1:
        return array
    middleIndex = len(array) // 2 # find the middle (rounded down)
    leftHalf = array[:middleIndex]
    rightHalf = array[middleIndex:]
    return mergerSortedArrays(mergeSort(leftHalf), mergeSort(rightHalf))
