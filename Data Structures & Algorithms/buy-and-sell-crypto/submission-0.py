class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_idx = 0
        right_idx = 1
        max_profit = 0

        while right_idx < len(prices):
            if prices[left_idx] < prices[right_idx]:
                profit = prices[right_idx] - prices[left_idx]
                if profit > max_profit:
                    max_profit = profit
                right_idx += 1

            elif prices[left_idx] >= prices[right_idx]:
                left_idx = right_idx
                right_idx += 1
            
        return max_profit 
