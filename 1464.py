# 1464. Maximum Product of Two Elements in an Array

import heapq
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxHeap = [-number for number in nums]
        heapq.heapify(maxHeap)
        firstNumber= heapq.heappop(maxHeap)
        secondNumber = heapq.heappop(maxHeap)
        return ((-firstNumber)-1)*((-secondNumber)-1)
