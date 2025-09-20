# 2798. Number of Employees Who Met the Target

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        result=0
        for i in range(0,len(hours)):
            if hours[i]>=target:
                result+=1
        return result
