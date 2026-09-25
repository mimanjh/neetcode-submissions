class Solution:
    def isValid(self, s: str) -> bool:
        openingPairs = {
            "(" : ")",
            "[" : "]",
            "{" : "}",
        }
        closingPairs = {
            ")" : "(",
            "]" : "[",
            "}" : "{",
        }
        stack = []

        if len(s) % 2 != 0:
            return False

        # put closing bracket in stack everytime there's an opening bracket
        # if a closing bracket shows up, check if the stack's last element is the correct closing bracket
        # if it is, pop it out and continue
        # if not, return False
        # default to returning True
        for c in s:
            if c in openingPairs:
                stack.append(openingPairs[c])
            if c in closingPairs:
                # how to check if there's an opening
                if stack:
                    if stack[-1] != c:
                        return False
                    else:
                        stack.pop()
                else:
                    return False
        if stack:
            return False
        return True