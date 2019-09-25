def getNthFib(n):
    # Write your code here.
    if n == 1 or n == 2:
        return n - 1
    else:
        return getNthFib(n - 1) + getNthFib(n - 2)
