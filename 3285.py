# 3285. Find Indices of Stable Mountains

class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        output=[]
        for i in range(1,len(height)):
            if(height[i-1]>threshold):
                output.append(i)
        return output
