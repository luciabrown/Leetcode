# 1935. Maximum Number of Words You Can Type

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        result=0
        words=text.split()
        for word in words:
            if all(letter not in brokenLetters for letter in word):
                    result+=1
        return result
