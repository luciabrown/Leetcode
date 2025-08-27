# 219. Contains Duplicate II

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        left=0
        seen=set()
        for i in range(0,len(nums)):
            while(nums[i] in seen): #if there is a match
                if(abs(left-i)<=k): # check if match is nearby
                    return True
                seen.remove(nums[left])
                left+=1
            seen.add(nums[i])
        return False
