class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closeToOpen={"}":"{",")":"(","]":"["}
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1]==closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # stack=[]
        # closeToOpen={')':'(','}':'{',']':'['}
        # for char in s:
        #     if char in closeToOpen:
        #         if stack and stack[-1] == closeToOpen[char]:
        #             stack.pop()
        #         else:
        #             return False
        #     else:
        #         stack.append(char)
        # return True if not stack else False
        
        
        
        
        
        
        
        
        