class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mini = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            mini = min(mini, prices[i])
            profit = max(profit, prices[i] - mini)
        
        return profit
