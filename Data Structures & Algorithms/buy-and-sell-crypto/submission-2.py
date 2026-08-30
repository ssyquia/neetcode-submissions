class Solution:
    # prices=[2,1,2,1,0,1,2]
    
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        res = 0
        while (left < right and right < len(prices)):
            curr = 0
            if(prices[left] > prices[right]):
                left = right 
                right += 1
            else:
                curr = prices[right] - prices[left]
                res = max(res, curr)
                right += 1
        return res
