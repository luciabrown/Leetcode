# 1464. Maximum Product of Two Elements in an Array

import heapq
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxHeap = [(-number,index) for index, number in enumerate(nums)]
        heapq.heapify(maxHeap)
        firstNumber,firstIndex = heapq.heappop(maxHeap)
        secondNumber,secondIndex = heapq.heappop(maxHeap)
        return ((-firstNumber)-1)*((-secondNumber)-1)
