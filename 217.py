#217. Contains Duplicate
from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cnt=Counter(nums)
        for number,frequency in cnt.items():
            if frequency>1:
                return True
        return False
