# 1816. Truncate Sentence

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        output=s.split()
        return(' '.join(output[0:k]))
