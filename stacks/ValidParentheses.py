class Solution:
    def isValid(self, s: str) -> bool:
        if s is None:
            return True
        
        brackets = {')': '(', '}': '{', ']': '[' }
        stack = []
        for char in s:
            if char in brackets:
                if not stack or stack.pop() != brackets[char]:
                    return False
            else:
                stack.append(char)
        return not stack

        
