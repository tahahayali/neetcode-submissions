class Solution:
    def isValid(self, s: str) -> bool:
        start = {'{' : 1, '[' : 2, '(' : 3}
        close = {'}' : 1, ']' : 2, ')' : 3}
        n = len(s)
        if s[0] in close or s[-1] in start or (n % 2) != 0:
            return False
        stack = []
        for c in s:
            print("Stack: " , stack , "PARAN: " , c)
            if start.get(c):
                stack.append(c)
            elif c in close:
                same = stack.pop()
                if close[c] != start[same]:
                    return False
        if len(stack) != 0:
            return False
        return True