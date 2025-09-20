# 875. Koko Eating Bananas

import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minBananas=1          # Eats 1 banana per hour
        maxBananas=max(piles) # Eats the largest pile in an hour
        mid=(minBananas+maxBananas)//2
        ans=maxBananas

        while minBananas<=maxBananas:
            hours=0
            for i in range(0,len(piles)):
                hours += math.ceil(piles[i] / mid)
            if(hours<=h):   # finished before h - try eat less bananas per hour
                ans=mid
                maxBananas=mid-1
            else:          # didn't eat all before guards return - must eat more bananas per hour
                minBananas=mid+1
            mid = (minBananas + maxBananas) // 2
        return ans
