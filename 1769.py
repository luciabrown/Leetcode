# 1769. Minimum Number of Operations to Move All Balls to Each Box

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans=[0]*len(boxes)
        for i in range (0,len(boxes)):
            for j in range (0,len(boxes)):
                if(boxes[j]=="1"):
                    ans[i]+=abs(i-j)
        return ans
