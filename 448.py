# 448. Find All Numbers Disappeared in an Array

from collections import defaultdict
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        upper=len(nums)+1
        result=[]
        numCount = defaultdict(int)
        for num in nums:
            numCount[num]+=1
        for i in range(1,upper):
            if numCount[i]==0:
                result.append(i)
        return result
