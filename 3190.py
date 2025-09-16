# 3190. Find Minimum Operations to Make All Elements Divisible by Three

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations=0
        for i in range(0,len(nums)):
            if(nums[i]%3==0):
                continue
            else:
                operations+=1
        return operations
