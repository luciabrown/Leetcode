# 2373. Largest Local Values in a Matrix

class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n=len(grid)
        outputArray=[]
        for _ in range(0,n-2):
            outputArray.append([])

        for i in range(0,n):
            for j in range(0,n):
                if(i<n-2 and j<n-2):
                    maxOf3x3 = max(self.get3x3(grid,i,j))
                    outputArray[i].append(maxOf3x3)
        return outputArray

    def get3x3(self,matrix,i,j):
        threeByThree=[]
        for x in range(i,i+3):
            for y in range(j,j+3):
                threeByThree.append(matrix[x][y])
        print("3x3",threeByThree)
        return threeByThree
