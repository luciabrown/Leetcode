# 1313. Decompress Run-Length Encoded List

import itertools 
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        output=[]
        for i in range(0,len(nums),2):
            output.append([nums[i+1]]*nums[i])
        return list(chain.from_iterable(output))
