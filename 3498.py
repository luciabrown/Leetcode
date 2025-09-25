# 3498. Reverse Degree of a String

class Solution:
    def reverseDegree(self, s: str) -> int:
        letterList=list(s)
        result=0
        for i in range(0,len(letterList)):
            result+= ((123-ord(letterList[i]))*(i+1))
        return result
