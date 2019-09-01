class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lookup = set()
        i = 0
        while i < len(nums):
            if nums[i] in lookup:
                lookup.remove(nums[i])
            else:
                lookup.add(nums[i])
            i += 1
        return list(lookup).pop()
        
