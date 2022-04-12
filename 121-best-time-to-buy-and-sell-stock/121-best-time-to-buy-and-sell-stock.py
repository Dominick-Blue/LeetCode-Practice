class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        window_start, window_end = 0, 1
        max_profit = 0

        while window_end < len(prices):
            if prices[window_start] < prices[window_end]:
                current_profit = prices[window_end] - prices[window_start]
                max_profit = max(max_profit, current_profit)
            else:
                window_start = window_end
            window_end += 1
        return max_profit