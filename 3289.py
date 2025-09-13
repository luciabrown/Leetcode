# 3289. The Two Sneaky Numbers of Digitville

from collections import Counter
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        result=[]
        cnt=Counter(nums)
        for number,freq in cnt.items():
            if freq==2:
                result.append(number)
        return result
