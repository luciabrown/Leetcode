# 2161. Partition Array According to Given Pivot

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lesser=[]
        pivotHandler=[]
        higher=[]
        for i in range(0,len(nums)):
            if(nums[i]<pivot):
                lesser.append(nums[i])
            elif(nums[i]==pivot):
                pivotHandler.append(nums[i])
            else:
                higher.append(nums[i])
        nums = lesser+pivotHandler+higher
        return nums
