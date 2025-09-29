# 1007. Minimum Domino Rotations For Equal Row

from statistics import mode
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        if((len(set(tops))==1) or (len(set(bottoms))==1)):  # Edge cases
            return 0 

        minRotations=len(tops)+1
        currentRotations=0
        modalTop=mode(tops)
        modalBottom=mode(bottoms)
        for i in range(0,len(tops)):
            if tops[i]!=modalTop:
                if(bottoms[i]==modalTop):
                    currentRotations+=1
                else:
                    currentRotations=-1
                    break

        if(currentRotations>0):
            minRotations=min(minRotations,currentRotations)

        currentRotations=0
        for j in range(0,len(bottoms)):
            if bottoms[j]!=modalBottom:
                if(tops[j]==modalBottom):
                    currentRotations+=1
                else:
                    currentRotations=-1
                    break

        if(currentRotations>0):
            minRotations=min(minRotations,currentRotations)

        if minRotations==len(tops)+1:
            return -1
        return minRotations
