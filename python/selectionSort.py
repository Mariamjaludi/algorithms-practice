def selectionSort(array):
    # Write your code here.
    for i in range(0, len(array)):
        smallest = array[i]
        index = i
        for j in range(i, len(array)):
            if array[j] < smallest:
                smallest = array[j]
                index = j
        array[index] = array[i]
        array[i] = smallest
    return array
