# 1672. Richest Customer Wealth

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth=0
        for i in range(0,len(accounts)):
            maxWealth=max(maxWealth,sum(accounts[i]))
        return maxWealth
