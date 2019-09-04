class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sorted_s = ''.join(sorted(s))
        sorted_t = ''.join(sorted(t))
        if sorted_s == sorted_t:
            return True
        return False