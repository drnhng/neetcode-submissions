class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i, a in enumerate(s):
            if a == '(' or a== '{' or a=='[':
                stack.append(a)
            if a== '}':
                if not stack:
                    return False
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            if a== ']':
                if not stack:
                    return False
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False

            if a== ')':
                if not stack:
                    return False
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        return False