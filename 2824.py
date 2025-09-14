# 2824. Count Pairs Whose Sum is Less than Target

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        left=0
        right=len(nums)-1
        occurrences=0
        while left<right:
            if(nums[right]+nums[left] >= target):
                right-=1
            else:
                occurrences+=(right-left)
                left+=1
        return occurrences
