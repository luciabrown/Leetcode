# 1637. Widest Vertical Area Between Two Points Containing No Points

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x=[]
        for i in range(0,len(points)):
            x.append(points[i][0])
        x.sort(reverse=True)
        maxDiff=0
        for i in range(0,len(x)-1):
            maxDiff=max(maxDiff,x[i]-x[i+1])
        return maxDiff
