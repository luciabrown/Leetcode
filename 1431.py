# 1431. Kids With the Greatest Number of Candies

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result=[]
        for i in range(0,len(candies)):
            if(max(candies) <= candies[i]+extraCandies):
                result.append(True)
            else:
                result.append(False)
        return result
