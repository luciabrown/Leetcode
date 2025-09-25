# 1221. Split a String in Balanced Strings

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance=0
        result=0
        listS=list(s)
        for i in range(0,len(listS)):
            if listS[i]=="L":
                balance-=1
            if listS[i]=="R":
                balance+=1
            if balance==0:
                result+=1
        return result
