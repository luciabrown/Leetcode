# 1678. Goal Parser Interpretation

class Solution:
    def interpret(self, command: str) -> str:
        commandL=(list(command))
        result=''
        for i in range(0,len(commandL)):
            if commandL[i]=="(":
                if commandL[i+1]==")":
                    result+="o"
            elif commandL[i]=="a" or commandL[i]=="l" or commandL[i]=="G":
                result+=commandL[i]
        return result
