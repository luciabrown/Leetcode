# 643. Maximum Average Subarray I

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        currentSum=sum(nums[:k])#sum of nums up until k'th index
        maxAvg=currentSum
        for i in range(k,len(nums)):# start loop at k
            currentSum+=nums[i]-nums[i-k] # add newest number, remove oldest number
            maxAvg=max(maxAvg,currentSum)
        return maxAvg/float(k)
