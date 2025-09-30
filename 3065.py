# 3065. Minimum Operations to Exceed Threshold Value I

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        x=0
        while(min(nums)<k):
            nums.remove(min(nums))
            x+=1
        return x
