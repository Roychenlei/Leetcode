class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        for x in  range(1,len(prices)):
        	if prices[x] > prices[x-1]:
        		profit = prices[x]-prices[x-1]
        		maxProfit += profit

        return maxProfit



if __name__ == '__main__':
	print (Solution().maxProfit([1,2,4]))