# 1470. Shuffle the Array

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        mid=len(nums)//2
        result=[]
        for i in range(0,mid):
            result.append(nums[i])
            result.append(nums[mid])
            mid+=1
        return result
