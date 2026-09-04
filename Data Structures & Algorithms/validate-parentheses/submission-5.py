class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        
        if len(s) == 0:
            return True
        
        elif len(s) == 1:
            return False

        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            
            elif i == ")":
                if stack and stack[-1] == "(":
                    stack.pop(-1)
                else:
                    return False
            
            elif i == "]":
                if stack and stack[-1] == "[":
                    stack.pop(-1)
                else:
                    return False

            elif i == "}":
                if stack and stack[-1] == "{":
                    stack.pop(-1)
                else:
                    return False
        return len(stack) == 0
            