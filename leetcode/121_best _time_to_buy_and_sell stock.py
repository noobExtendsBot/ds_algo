"""
Problem Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
            using two pointers
        """
        
        if len(prices) < 2:
            return 0
        
        f, n, m_profit = 0, 1, 0
        while f < n and n < len(prices):
            c_profit = 0
            if prices[n] < prices[f]:
                f = n 
            else:
                c_profit = prices[n] - prices[f]
            n += 1
            m_profit = max(c_profit, m_profit)
        return m_profit
