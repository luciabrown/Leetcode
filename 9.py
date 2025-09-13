# 9. Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        stringify=str(x)
        low=0
        high=len(stringify)-1
        while(low<high):
            if(stringify[low]!=stringify[high]):
                return False
            low+=1
            high-=1
        return True
