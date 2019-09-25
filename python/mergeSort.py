# Merge Sort: O(nlog(n)) time complexity O(nlog(n)) space
def mergeSort(array):
    # Base case:
    if len(array) == 1:
        return array
    middleIndex = len(array) // 2  # find the middle (rounded down)
    leftHalf = array[:middleIndex]
    rightHalf = array[middleIndex:]
    return mergeSortedArrays(mergeSort(leftHalf), mergeSort(rightHalf))


def mergeSortedArrays(leftHalf, rightHalf):
    sortedArray = [None] * (len(leftHalf) + len(rightHalf))
    i = j = k = 0
    while i < len(leftHalf) and j < len(rightHalf):
        if leftHalf[i] < rightHalf[j]:
            sortedArray[k] = leftHalf[i]
            i += 1
        else:
            sortedArray[k] = rightHalf[j]
            j += 1
        k += 1
    while i < len(leftHalf):
        sortedArray[k] = leftHalf[i]
        i += 1
        k += 1
    while j < len(rightHalf):
        sortedArray[k] = rightHalf[j]
        j += 1
        k += 1
    return sortedArray

################################################################################


# second method O(nlog(n)) time, O(n) space
def mergeSort2(array):
    if len(array) <= 1:
        return array
    auxArray = array[:]
    mergeSortHelper(array, 0, len(array) - 1, auxArray)
    return array


def mergeSortHelper(mainArray, start, end, auxArray):
    if start == end:
        return
    middle = (start + end) // 2
    mergeSortHelper(auxArray, start, middle, mainArray)
    mergeSortHelper(auxArray, middle + 1, end, mainArray)
    doMerge(mainArray, start, middle, end, auxArray)


def doMerge(mainArray, start, middle, end, auxArray):
    k = start
    i = start
    j = middle + 1

    while i <= middle and j <= end:
        if auxArray[i] < auxArray[j]:
            mainArray[k] = auxArray[i]
            i += 1
        else:
            mainArray[k] = auxArray[j]
            j += 1
        k += 1

    while i <= middle:
        mainArray[k] = auxArray[i]
        i += 1
        k += 1
    while j <= end:
        mainArray[k] = auxArray[j]
        j += 1
        k += 1
