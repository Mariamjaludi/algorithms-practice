def isBalanced(str):
    s = []
    is_balanced = True
    i = 0
    while i < len(str) and is_balanced:
        paren = str[i]
        if paren == "(":
            s.append(paren)
        elif s:
            s.pop()
        else:
            is_balanced = False
        i += 1
    return is_balanced

str = "((()))"

print(isBalanced(str))
str2= "((()"
print(isBalanced(str2))
