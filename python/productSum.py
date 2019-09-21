def productSum(array, m=1):
    # Write your code here.
    sum = 0
    for el in array:
        if type(el) is list:
            sum += productSum(el, m + 1)
        else:
            sum += el
    return sum * m
