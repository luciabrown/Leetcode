# 349. Intersection of Two Arrays

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output=set()
        longer=[]
        shorter=[]
        if(len(nums1)>len(nums2)):
            longer=nums1
            shorter=nums2
        else:
            longer=nums2
            shorter=nums1
        for i in range(0,len(longer)):
            if longer[i] in shorter:
                output.add(longer[i])
        return list(output)
