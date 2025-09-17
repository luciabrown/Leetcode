# 3280. Convert Date to Binary

class Solution:
    def convertDateToBinary(self, date: str) -> str:
        delimitedDate=date.split("-")
        binaryDate=[]
        for i in range(0,len(delimitedDate)):
            binaryDate.append(format(int(delimitedDate[i]),'b'))
            if(i!=len(delimitedDate)-1):
                binaryDate.append("-")
        result= ("".join(binaryDate))
        return result
