# 2974. Minimum Number Game

import heapq
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr=[]
        heapq.heapify(nums)
        while nums:
            if len(nums) >= 2:
                first = heapq.heappop(nums)
                second = heapq.heappop(nums)
                arr.append(second)
                arr.append(first)
            else:
                arr.append(heapq.heappop(nums))
        return arr
