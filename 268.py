# 268. Missing Number

from collections import Counter
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        cnt=Counter(nums)
        print(cnt.items())
        result=0
        for i in range(0,len(nums)+1):
            if i not in cnt.keys():
                result=i
                break
        return result
