class Solution(object):
    def isValid(self, s):
        mapping = {']':'[', '}':'{', ')':'('}
        stack = []
        for c in s:
            if c in mapping:
                top = stack.pop() if stack else '#'
                if mapping[c] != top:
                    return False
            else:
                stack.append(c)
                
        return not stack
    
    def isValid2(self,s):
        stack = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char) 
            elif len(stack) <= 0:
                return False
            elif char == ")" and stack.pop() != "(":
                return False
            elif char == "]" and stack.pop() != "[":
                return False
            elif char == "}" and stack.pop() != "{":
                return False
        if len(stack) == 0:
            return True
        return False
       
                
            
            