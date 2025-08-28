# 66. Plus One

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if(digits[-1]!=9):
            digits[-1] = digits[-1]+1
        else:
            if(self.nineHandler(digits,len(digits)-1)):
                digits.insert(0,1)
        return digits
        
    def nineHandler(self,digits,length):
        if length < 0:
            return True
        if digits[length] < 9:
            digits[length] += 1
            return False
        digits[length] = 0
        return self.nineHandler(digits, length - 1)
