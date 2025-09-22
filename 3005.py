# 3005. Count Elements With Maximum Frequency

from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        maxFreq=max(Counter(nums).values())
        result=0
        for number,frequency in Counter(nums).items():
            if(frequency==maxFreq):
                result +=maxFreq
        return result
