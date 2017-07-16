class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        value=[]
        a, b = 0, 0

        for i in prices:
        	a = i
        	value.append(i)
        	for j in value :
        		if b < a-j:
        			b = a-j
        return b
if __name__ == '__main__':
	print (Solution().maxProfit([7,1,5,3,6,4]))





        