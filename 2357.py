# 2357. Make Array Zero by Subtracting Equal Amounts

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations=0
        nums = [num for num in nums if num > 0] # Take out zeros from the start because they skew the min
        while not all(number == 0 for number in nums):
            smallest=min(nums)              # Smallest non-zero number
            operations+=1
            nums = [num - smallest for num in nums if num - smallest > 0]   # Subtract smallest non-zero
        return operations
