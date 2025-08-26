# 766. Toeplitz Matrix

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if(len(matrix[0])==1): # if each matrix only has one element
            return True
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if (i!=len(matrix)-1 and j!=len(matrix[0])-1):
                    print(matrix[i][j])
                    print(matrix[i+1][j+1])
                    if(matrix[i][j]!=matrix[i+1][j+1]):
                        return False
        return True
        
