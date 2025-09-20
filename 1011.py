# 1011. Capacity To Ship Packages Within D Days

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        minCapacity=max(weights)
        maxCapacity=sum(weights)
        mid=(maxCapacity+minCapacity)//2
        ans=0

        while minCapacity <= maxCapacity:
            shipmentDays=1
            currentShipment=0
            for i in range(0,len(weights)):
                if(currentShipment+weights[i]>mid):
                    shipmentDays+=1
                    currentShipment=0
                currentShipment+=weights[i]

            if(shipmentDays<=days): # finished early - we can try decrease ship capacity
                ans = mid   # save this as a possible answer
                maxCapacity = mid - 1 
            elif(shipmentDays>days): # finished late - must increase ship capacity
                minCapacity = mid + 1
            mid = (maxCapacity + minCapacity) // 2
        return ans
