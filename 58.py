# 58. Length of Last Word

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        splitted=s.split()
        return len(splitted[-1])
