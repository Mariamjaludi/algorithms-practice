# A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.
# For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
# A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.
# Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.
# Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        count = 0
        solution = []
        start = 0
        i = 0
        while i < len(S):
            if S[i] == '(':
                count += 1
            elif S[i] == ")":
                count -= 1
            if count == 0:
                # i is keeping track of where we are in the string.
                # if we reach a completely closed parentheses set, we want to add that to our solution array
                # we append to the array everything in S from the start + 1 (because we want to get rid of the outer open parenthesis)
                # until the element before i (i - 1), because we want to get rid of the outer closing parenthesis.
                solution.append(S[start+1:i])
                # then we set start to just after i.
                start = i+1
            i += 1
        return "".join(solution)
