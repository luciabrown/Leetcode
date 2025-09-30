# 2221. Find Triangular Sum of an Array

class Solution:
    def triangularSum(self, nums: List[int]) -> int:

        def reversePascal(arr):
            if len(arr)==1:
                return arr[0]
            
            new=[(arr[i]+arr[i+1])%10 for i in range(0,len(arr)-1)]
            return reversePascal(new)

        return reversePascal(nums)
