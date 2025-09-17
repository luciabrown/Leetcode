# 22. Generate Parentheses

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Count of open must be <=n n
        # Closed can be added if closed < open
        # Valid IFF open = n = closed
        stack=[]
        result=[]

        def backtrack(openN,closedN):
            if(openN==closedN==n):
                result.append("".join(stack))
                return result

            if openN<n:
                stack.append("(")
                backtrack(openN+1,closedN)
                stack.pop()
            
            if closedN<openN:
                stack.append(")")
                backtrack(openN,closedN+1)
                stack.pop()
        backtrack(0,0)
        return result
