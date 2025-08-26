# 867. Transpose Matrix

class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        outputMatrix=[]
        rows=len(matrix[0])
        cols=len(matrix)
        for _ in range(rows):
            outputMatrix.append([]) # make cols of new matrix
        for i in range(rows):
            for _ in range(cols):
                outputMatrix[i].append(0) # initialise with zeros

        for i in range(0,rows):
            for j in range(0,cols):
                outputMatrix[i][j]=matrix[j][i] # swap rows & cols
        return outputMatrix
