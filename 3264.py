# 3264. Final Array State After K Multiplication Operations I

import heapq
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        # Define heap
        heap = [(number,index) for index, number in enumerate(nums)]
        heapq.heapify(heap)

        # Perform operations k times
        while(k>0):
            k-=1
            number,index = heapq.heappop(heap)
            number*=multiplier
            heapq.heappush(heap,(number,index))

        # Reconstruct after operations
        result = [0] * len(nums)
        for number, index in heap:
            result[index] = number

        return result
