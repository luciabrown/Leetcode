# 1512. Number of Good Pairs

from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        countNums = Counter(nums)
        total=0
        for value in countNums.values():
            total+=(value*(value-1)//2)
        return total
