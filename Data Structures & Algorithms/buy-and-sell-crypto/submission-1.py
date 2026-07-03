class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_p = 0
        right_p = 0
        profit = 0
        n = len(prices)
        while right_p < n:
            if prices[right_p] < prices[left_p]:
                left_p = right_p
                right_p += 1
                if right_p >= n:
                    break
                profit = max(profit, prices[right_p] - prices[left_p])
            else:
                right_p += 1
                if right_p >= n:
                    break
                profit = max(profit, prices[right_p] - prices[left_p])
        return profit


    