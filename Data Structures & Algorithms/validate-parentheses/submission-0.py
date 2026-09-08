class Solution:
    def isValid(self, s: str) -> bool:
        para = {"(": ")", "{": "}", "[":"]"}
        stack = []
        for c in s:
            if c in para.keys():
                stack.append(c)
            else:
                if len(stack) == 0 or para[stack.pop()] != c:
                    return False
        return len(stack) == 0