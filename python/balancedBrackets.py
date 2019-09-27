def balancedBrackets(string):
    stack = []
    openingBrackets = "({["
    closingBrackets = ")}]"
    matchingBrackets = { ")":"(", "}":"{", "]":"[" }

    for char in string:
        if char in openingBrackets:
            stack.append(char)
        elif char in closingBrackets:
            if len(stack) == 0:
                return False
            else:
                bracket = stack.pop()
                if bracket == matchingBrackets[char]:
                    continue
                else:
                    return False
    return len(stack) == 0
