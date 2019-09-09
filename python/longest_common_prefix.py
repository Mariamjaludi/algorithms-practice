class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        checker = True
        ans = []
        i = 0
        shortest = ''
        # find shortest string
        for word in strs:
            if shortest == '' or shortest > len(word):
                shortest = len(word)
        if shortest == '':
            return ''
        while i < shortest and checker:
            letter = strs[0][i]
            for word in strs:
                if word[i] != letter:
                    checker = False
            if checker:
                ans.append(letter)
                i += 1
        return ''.join(ans)
