def strStr(haystack, needle):
    if not needle:
        return 0
    if not haystack:
        return -1

    nlength = len(needle)
    hlength = len(haystack)
    i = 0
    while i <= hlength - nlength:
        if haystack[i:(i+nlength)] == needle:
            return i
        else:
            i += 1

    return -1
