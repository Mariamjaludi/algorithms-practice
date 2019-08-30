# In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.
# Return the element repeated N times.

class Solution(object):
    def repeatedNTimes(self, A):
        i = 0
        dict = {}
        while i < len(A):
            if dict.get(A[i]) != None:
                return A[i]
            else:
                dict[A[i]] = A[i]
            i += 1

    def repeatedSimple(self, A):
        return (sum(A)-sum(set(A))) // (len(A)//2-1)
