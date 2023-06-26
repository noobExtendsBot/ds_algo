import pdb

from collections import deque



def maxProfit(prices):
    if len(prices) < 2:
            return 0
        
    f, n, m_profit = 0, 1, 0
    pdb.set_trace()
    while f < n and n < len(prices):
        c_profit = 0
        if prices[n] < prices[f]:
            f = n 
        else:
            c_profit = prices[n] - prices[f]
        n += 1

        if c_profit > m_profit:
            m_profit = c_profit
    return m_profit

        

if __name__=="__main__":
    print(maxProfit([1, 2]))
    # print(maxProfit([3, 1, 2, 4, 5]))
    # print(maxProfit([5,5,5,5,5,5]))