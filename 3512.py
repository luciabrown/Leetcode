# 3512. Minimum Operations to Make Array Sum Divisible by K

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums)%k
