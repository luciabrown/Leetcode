# 1486. XOR Operation in an Array

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result=0
        for i in range(0,n):
            result=(result)^(start+2*i)
        return result
            
