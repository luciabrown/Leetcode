# 3090. Maximum Length Substring With Two Occurrences

class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        occurrences={}
        for i in range(0,len(s)):
            occurrences[s[i]]=0 # initialise dictionary of occurrences

        maxLen=0
        left=0
        for i in range(0,len(s)):
            occurrences[s[i]]+=1
            while(occurrences[s[i]]>2):
                occurrences[s[left]]-=1
                left+=1
            maxLen=max(maxLen,i-left+1)
        return maxLen
