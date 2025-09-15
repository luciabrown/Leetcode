# 2423. Remove Letter To Equalize Frequency

from collections import Counter
from statistics import multimode
class Solution:
    def equalFrequency(self, word: str) -> bool:
        # Edge case handling
        if (len(word) == len(set(word))):   # all chars are unique
            return True
        if(len(set(word))==1):              # all chars are same
            return True

        wordCount = Counter(word)
        if(len(multimode(wordCount.values()))==2):  # if there are two modes
            if (1 in (multimode(wordCount.values())) and len(set(word))==2):
                return True     # if one of the modes is 1, it's a solo character, remove it
                
        removedFlag=False
        targetFreq= min(multimode(wordCount.values()))
        for letters in wordCount:
            if wordCount[letters] != targetFreq:
                word = word.replace(letters, '', 1) 
                removedFlag=True
                break
        if(not removedFlag and len(set(Counter(word).values()))==1):
            return False
        return len(set(Counter(word).values()))==1
