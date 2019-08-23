# Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.


class Solution(object):
    def sortArrayByParity(self, A):
        left = 0
        right = len(A) - 1
        while left < right:
            # if A[left] & 1 == 1, it is odd
            #if !(A[left] & 1), it is even
            if not A[left] & 1:
                left += 1
                continue
            elif A[right] & 1:
                right -= 1
                continue

            #multiple assignment uses tuples.
            A[left],A[right] = A[right],A[left]
            left += 1
            right -= 1
        return A
