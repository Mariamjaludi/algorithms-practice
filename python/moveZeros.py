class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        counter = len(nums)
        while counter:
            if nums[i] == 0:
                temp = nums.pop(i)
                nums.append(temp)
            else:
                i += 1
            counter -= 1
