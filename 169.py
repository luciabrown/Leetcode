# 169. Majority Element

from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority=(len(nums)/2)
        cnt=Counter(nums)
        result=0
        for number,frequency in cnt.items():
            if(frequency>majority):
                result=number
                break
        return result
