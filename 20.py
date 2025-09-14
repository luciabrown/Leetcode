# 20. Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in range(0,len(s)):
            if s[i] in "([{":
                stack.append(s[i])
            elif(s[i]==")"):
                if(not stack or stack[-1]!="("):
                    return False
                del stack[-1]
            elif(s[i]=="]"):
                if(not stack or stack[-1]!="["):
                    return False
                del stack[-1]
            elif(s[i]=="}"):
                if(not stack or stack[-1]!="{"):
                    return False
                del stack[-1]
        if(stack):
            return False
        return True
