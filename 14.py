# 14. Longest Common Prefix

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        sortedList=sorted(strs)
        first=sortedList[0]
        last=sortedList[-1]
        length=min(len(first),len(last))
        output=""
        for i in range(0,length):
            if(first[i]==last[i]):
                output=output+first[i]
            else:
                break
        return output
