class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,sell, maxProfit = prices[0], prices[0], 0
        for current in prices:
            if current > sell:
                sell = current
            elif current < buy:
                buy = current
                sell = current
            if(sell-buy > maxProfit):
                maxProfit = sell - buy
        return maxProfit