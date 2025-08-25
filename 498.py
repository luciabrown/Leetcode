# 498. Diagonal Traverse

class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """

        # Variable declaration
        rows=len(mat[0])
        cols=len(mat)
        size=rows*cols
        x=0
        y=0
        outputArray=[mat[x][y]]   
        print("OutputArray: ",outputArray)                     
        actionTaken="UR"

        # If there's only 1 column, it's already in diagonal order
        if(cols==1):
            return mat[0]

        # if all of the subarrays have one element e.g. [[3],[2]]


        # main logic
        while(len(outputArray)<size):
            if((x==0 and actionTaken=="UR")or(x==len(mat)-1 and actionTaken=="DL")):
                if(y==len(mat)-1):
                    x+=1
                    outputArray.append(mat[x][y])
                    actionTaken="SWITCH"
                else:
                    y+=1
                    outputArray.append(mat[x][y])
                    actionTaken="SWITCH"
            elif((y==0 and actionTaken=="DL")or(y==len(mat)-1 and actionTaken=="UR")):
                x+=1
                outputArray.append(mat[x][y])
                actionTaken="SWITCH"

            # Continous movement handling
            elif(self.downLeft(x,y,rows,cols) and actionTaken!="UR"):
                x+=1
                y-=1
                outputArray.append(mat[x][y])
                actionTaken="DL"
            elif(self.upRight(x,y,rows,cols) and actionTaken!="DL"):
                x-=1
                y+=1
                outputArray.append(mat[x][y])
                actionTaken="UR"
        return outputArray

    # Helper functions to check if a move is valid
    def downLeft(self,x,y,rows,cols):
        newX=x+1
        newY=y-1
        if(newX<0 or newY<0 or newX>rows or newY>cols):
            return False
        return True

    def upRight(self,x,y,rows,cols):
        newX=x-1
        newY=y+1
        if(newX<0 or newY<0 or newX>rows or newY>cols):
            return False
        return True
