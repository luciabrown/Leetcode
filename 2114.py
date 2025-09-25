# 2114. Maximum Number of Words Found in Sentences

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxSentenceLength=0
        for i in range(0,len(sentences)):
            maxSentenceLength=max(maxSentenceLength,(len(sentences[i].split())))
        return maxSentenceLength
