# 506. Relative Ranks

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        result=[""]*len(score)
        order = [(number,index) for index,number in enumerate(score)]
        order.sort()

        rank=len(order)
        for i in range(len(order)):
            if rank==1:
                result[order[i][1]] = "Gold Medal"
            elif rank==2:
                result[order[i][1]] = "Silver Medal"
            elif rank==3:
                result[order[i][1]] = "Bronze Medal"
            else:
                result[order[i][1]] = str(rank)
            rank-=1
        return result
