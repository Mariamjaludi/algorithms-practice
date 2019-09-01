# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
# You may assume the integer does not contain any leading zero, except the number 0 itself.
class Solution(object):
    def plusOne(self, digits):
    # [8, 9 , 9]
    # [8, 9, 0] plus = 1
    # [8, 0 , 0 ] plus = 1
    # [9, 0, 0] plus = 0
    # return [9, 0, 0]

    # [9, 9, 9]
    # [9, 9, 0] plus = 1
    # [9, 0, 0] plus = 1
    # [0, 0, 0] plus = 1
    # return [1] + [0, 0 , 0]

        i = len(digits)-1
        plus = 0

        while i >= 0:
            d = digits[i]
            if d < 9:
                digits[i] += 1
                plus = 0
                break
            else:
                digits[i] = 0
                plus = 1

            i -= 1

        if plus == 1:
            return [1] + digits
        else:
            return digits
