# 2348. Number of Zero-Filled Subarrays

class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        countOfConsecutiveZeros=0
        consecutiveList=[]
        for i in range(0,len(nums)):
            if(nums[i]==0):
                countOfConsecutiveZeros+=1
                if(i==len(nums)-1):
                    consecutiveList.append(countOfConsecutiveZeros)
            else:
                if(countOfConsecutiveZeros!=0):
                    consecutiveList.append(countOfConsecutiveZeros)
                countOfConsecutiveZeros=0

        endTotal=0
        for i in range(0,len(consecutiveList)):
            endTotal += self.calculateSubArrays(consecutiveList[i])
        return endTotal

    def calculateSubArrays(self, number):
        return number*(number+1)/2
