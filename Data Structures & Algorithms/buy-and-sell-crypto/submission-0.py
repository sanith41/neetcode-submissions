class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        maxprodfit=0
        for i in range(1,len(prices)):
            mini=min(mini,prices[i])
            profit=prices[i]-mini
            maxprodfit=max(profit,maxprodfit)
        return maxprodfit


        