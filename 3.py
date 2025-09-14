# 3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        left=0
        longest=0
        for i in range(0,len(s)):
            while(s[i] in seen):
                seen.remove(s[left])
                left+=1
            seen.add(s[i])
            longest=max(longest,(i-left+1))
        return longest
