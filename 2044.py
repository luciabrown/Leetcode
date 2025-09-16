# 2044. Count Number of Maximum Bitwise-OR Subsets

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxBitOr=0
        for n in nums:
            maxBitOr |= n # maximum bitwise OR is the bitwise OR of the whole array
        
        # Find the subsets with the same bitwise OR as the maxBitOr
        def dfs(index,bitOr):
            nonlocal maxBitOr   # need to use this global variable for comparison purposes
            if(index==len(nums)):#hit the end
                return 1 if bitOr==maxBitOr else 0 # function is recursive so this adds 1 or 0
            take=dfs(index+1,bitOr | nums[index]) # subsets do not have to be contiguous
            skip=dfs(index+1,bitOr)     # so skipping a number in the index is allowed
            return (take+skip)
        
        return dfs(0,0)
