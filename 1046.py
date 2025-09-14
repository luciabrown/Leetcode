# 1046. Last Stone Weight

import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-n for n in stones]
        heapq.heapify(maxHeap)
        print(maxHeap)

        while(len(maxHeap)>1):
            firstStone = heapq.heappop(maxHeap)
            secondStone = heapq.heappop(maxHeap)
            if(firstStone!=secondStone):
                difference = (-(firstStone) - -(secondStone))
                heapq.heappush(maxHeap,-difference)
        if maxHeap:
            return -maxHeap[0] # at most one stone left
        return 0
