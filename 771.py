# 771. Jewels and Stones

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result=0
        sJewels=set(jewels)
        for i in stones:
            if i in sJewels:
                result+=1
        return result
