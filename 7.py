# 7. Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        output=""
        xString = str(x)
        if(xString[0]=="-"):
            output+="-"
            xString=xString[1:]
        output+=xString[::-1]
        if int(output)>=(2**31)-1 or -int(output)>=(2**31)-1:
            return 0
        return int(output)
