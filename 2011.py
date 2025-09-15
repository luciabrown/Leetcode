# 2011. Final Value of Variable After Performing Operations

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x=0
        for command in operations:
            if command[0]=="+" or command[-1]=="+":
                x+=1
            else:
                x-=1
        return x
