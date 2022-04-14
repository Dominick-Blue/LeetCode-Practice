class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if s[0] == ')' or s[0] == ']' or s[0] == '}':
            return False
        
        stack = []
        
        paren_map = {
            ')':'(',
            '}': '{',
            ']':'['
        }
        
        
        for char in s:
            if char in paren_map:
                if stack and stack[-1] == paren_map[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return not stack
            