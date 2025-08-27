# 594. Longest Harmonious Subsequence

from collections import Counter

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        occurrences=Counter(nums)
        keys=sorted(occurrences.keys())
        total=0
        for i in range(1,len(keys)):
            current = keys[i]
            prev = keys[i - 1]
            if(abs(current-prev)==1):
                total=max(total,(occurrences[current])+(occurrences[prev]))
        return total
