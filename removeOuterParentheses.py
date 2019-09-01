class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        count = 0
        stack = []
        start = 0
        i = 0
        while i < len(S):
            if S[i] == '(':
                count += 1
            elif S[i] == ")":
                count -= 1
            if count == 0:
                stack.append(S[start+1:i])
                start = i+1
            i += 1
        return "".join(stack)
