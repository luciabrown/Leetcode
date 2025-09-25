# 3146. Permutation Difference between Two Strings

class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        result=0
        listS=list(s)
        listT=list(t)
        for i in range(0,len(listS)):
            iInT=listT.index(listS[i])
            result+=(abs(i-iInT))
        return result
