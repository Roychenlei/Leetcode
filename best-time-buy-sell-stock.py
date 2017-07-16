import sys
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

    def maxProfit_opt1(self,prices):
        total = 0
        low, high = sys.maxint, 0
        for x in prices:
            if x-low > total:
                total = x - low
            if x < low:
                low = x
        return total




if __name__ == '__main__':
    print (Solution().maxProfit([7,1,5,3,6,4]))
    print (Solution().maxProfit_opt1([7,1,5,3,6,4]))
    print (Solution().maxProfit_opt2([7,1,5,3,6,4]))






        