# 350. Intersection of Two Arrays II

from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output=[]
        longer=None
        shorter=None
        cnt1=Counter(nums1)
        cnt2=Counter(nums2)
        if(cnt1>cnt2):
            longer=cnt1
            shorter=cnt2
        else:
            longer=cnt2
            shorter=cnt1
        for number,freq in shorter.items():
            if number in longer:
                minFreq=min(longer[number],shorter[number])
                output.extend([number]*minFreq)
        return output
