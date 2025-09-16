# 1863. Sum of All Subset XOR Totals

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(index,xor):
            if index==len(nums): # indexed through all
                return xor
            getNewIndex = dfs(index+1,xor^nums[index]) # take another element from the input
            stayOnSame = dfs(index+1,xor)              # explore the current subset
            return getNewIndex+stayOnSame
        return dfs(0,0)
