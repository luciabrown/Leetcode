# 1480. Running Sum of 1d Array

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningTotal=nums[0]
        result=[nums[0]]
        for i in range (1,len(nums)):
            runningTotal+=nums[i]
            result.append(runningTotal)
        return result
