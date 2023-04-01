class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for brac in s:
            if brac in mapping:
                if not stack or stack.pop() != mapping[brac]:
                    return False
            else:
                stack.append(brac)
        return not stack
