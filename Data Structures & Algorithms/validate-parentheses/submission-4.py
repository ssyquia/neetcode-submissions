class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        mapping = {')': '(', '}': '{', ']': '['}
        for i in s:
            if i == '{' or i == '[' or i == '(':
                stack.append(i)
            elif not stack or stack.pop() != mapping[i]:
                return False
        return not stack