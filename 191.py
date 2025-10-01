# 191. Number of 1 Bits

from collections import Counter
class Solution:
    def hammingWeight(self, n: int) -> int:
        return Counter(bin(n))['1']
