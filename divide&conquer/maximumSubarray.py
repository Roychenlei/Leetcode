# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.


# 典型的DP题：
# 1. 状态dp[i]：以A[i]为最后一个数的所有max subarray的和。
# 2. 通项公式：dp[i] = dp[i-1]<=0 ? dp[i] : dp[i-1]+A[i]
# 3. 由于dp[i]仅取决于dp[i-1]，所以可以仅用一个变量来保存前一个状态，而节省内存。

from sys import maxint

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far = -maxint -1
        max_ending_here = 0

        for i in range(0, size):
        	max_ending_here = max_ending_here+nums[i]
        	if(max_so_far < max_ending_here):
        		max_so_far = max_ending_here

        	if max_ending_here < 0:
        		max_ending_here = 0
        return max_so_far


    def maxSubArray1(self, nums):
        if nums is None or len(nums) == 0:
            return 0

        maxSum = nums[0]
        minSum =0
        sum = 0

        for num in nums : 
            sum += num
            print sum,minSum,maxSum
            if sum - minSum > maxSum:
                maxSum = sum - minSum
            if sum < minSum:
                minSum = sum

        return maxSum


if __name__ == '__main__':
    print (Solution().maxSubArray1([7,-1,-5,3,6,-4]))
    print (Solution().maxSubAraay1([7,1,-5,3,-6,4]))
    print (Solution().maxSubArray1([7,-1,-5,3,6,4]))





