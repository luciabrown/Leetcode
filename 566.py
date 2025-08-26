# 566. Reshape the Matrix

class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if(r*c!=len(mat)*len(mat[0])): # if r*c is illegal on the given matrix
            return mat                 # return given matrix
        outputArray=[]
        for _ in range(0,r):
            outputArray.append([])

        outputIndex=0
        for i in range(0,len(mat)):
            for j in range(0,len(mat[0])):
                print(outputIndex)
                if outputIndex>=r or (len(outputArray[outputIndex])>=c):
                    outputIndex+=1
                outputArray[outputIndex].append(mat[i][j])
        return outputArray
        
