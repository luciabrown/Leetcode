# 2558. Take Gifts From the Richest Pile

import heapq
import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        maxHeap = [-n for n in gifts]
        heapq.heapify(maxHeap)
        while(k>0):
            k-=1
            most=-(heapq.heappop(maxHeap))
            most= math.isqrt(most)
            heapq.heappush(maxHeap,-most)
        return sum(abs(gift) for gift in maxHeap)
