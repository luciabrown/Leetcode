# 1791. Find Center of Star Graph

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        seen=set()
        for i in range(0,len(edges)):
            if(edges[i][0] in seen):
                return edges[i][0]
            elif(edges[i][1] in seen):
                return edges[i][1]
            else:
                seen.add(edges[i][0])
                seen.add(edges[i][1])
