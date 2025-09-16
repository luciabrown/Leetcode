# 3467. Transform Array by Parity

class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        result=[]
        for i in range(0,len(nums)):
            if(nums[i]%2==0):
                result.insert(0,0)
            else:
                result.append(1)
        return result
