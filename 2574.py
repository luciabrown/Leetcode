# 2574. Left and Right Sum Differences

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum=[]
        rightSum=[]
        answer=[]
        tempLeft=0
        tempRight=0
        for i in range(0,len(nums)):
            leftSum.append(tempLeft)
            tempLeft+=nums[i]
            rightSum.insert(0,tempRight)
            tempRight+=nums[len(nums)-1-i]
        for i in range(0,len(nums)):
            answer.append(abs(leftSum[i]-rightSum[i]))
        return answer
