# 1684. Count the Number of Consistent Strings

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowedLetters=set(allowed)
        count=len(words)
        for word in words:
            for letter in list(word):
                if letter not in allowedLetters:
                    count-=1
                    break
        return count
