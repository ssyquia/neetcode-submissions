class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for i in s:
            if i == '{' or i == '[' or i == '(':
                stack.append(i)
            elif len(stack) != 0 and i == '}' and stack[-1] == '{':
                stack.pop()
            elif len(stack) != 0 and i == ')' and stack[-1] == '(':
                stack.pop()
            elif len(stack) != 0 and i == ']' and stack[-1] == '[': 
                stack.pop()
            else:
                return False
        
        if(len(stack) == 0): return True
        return False