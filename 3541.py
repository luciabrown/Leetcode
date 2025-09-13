# 3541. Find Most Frequent Vowel and Consonant

from collections import Counter
class Solution:
    def maxFreqSum(self, s: str) -> int:
        letters=Counter(s)
        maxV=0
        maxC=0
        vowels=set("aeiou")
        for letter,frequency in letters.items():
            if letter in vowels:
                if frequency>maxV:
                    maxV=frequency
            else:
                if frequency>maxC:
                    maxC=frequency
        return maxC+maxV
