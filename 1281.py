# 1281. Subtract the Product and Sum of Digits of an Integer

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod=1
        summ=0
        while(n>0):
            prod=prod*(n%10)
            summ=summ+(n%10)
            n=n//10
        return prod-summ
