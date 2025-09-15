# 1346. Check If N and Its Double Exist

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        left=0
        right=len(arr)-1
        while left<right:
            if(arr[left]*2==arr[right] or arr[right]*2==arr[left]):
                return True
            elif(left==(right-1)):
                left=0
                right-=1
            else:
                left+=1
        return False
