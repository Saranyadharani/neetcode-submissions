class Solution:
    def maxProfit(self, prices):
        n=len(prices)
        minsofar=prices[0]
        max_profit=0
        for i in range(1,n):
            minsofar=min(minsofar,prices[i])
            max_profit=max(max_profit,prices[i]-minsofar)
        return max_profit      