class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis_map = {
            "]": "[",
            "}": "{",
            ")": "("
        }
        stack = []

        for p in s:
            if p in parenthesis_map:
                if stack and stack[-1] == parenthesis_map[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)

        return True if not stack else False