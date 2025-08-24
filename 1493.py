# 1493. Longest Subarray of 1's After Deleting One Element

class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(any(nums)==0 or len(nums)==1):
            return 0
        if(nums.count(1)==1):
            return 1
        
        currentZeros=0
        leftPointer=0
        rightPointer=0
        countList=0
        for rightPointer in range(0,len(nums)):
            if(nums[rightPointer]==0):
                currentZeros+=1
            while currentZeros > 1:
                if nums[leftPointer] == 0:
                    currentZeros -= 1
                leftPointer += 1
            countList=max(countList,rightPointer-leftPointer)
        return countList
