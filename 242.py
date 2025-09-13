# 242. Valid Anagram

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sC=Counter(s)
        tC=Counter(t)
        if(tC==sC):
            return True
        return False
