class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_prof = 0
        
        for price in prices:
            print(price)
            min_price =min(min_price, price)
            max_prof = max(max_prof, price - min_price)
            print('max', max_prof, 'min',min_price)
            
        return max_prof