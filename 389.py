# 389. Find the Difference

from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cS=Counter(s)
        cT=Counter(t)
        result=0
        for letter,freq in cT.items():
            if cS[letter]<freq:
                result=letter
                break
        return result
