# Given an array and a value, remove all instances of that value in place and return the new length.

# Do not allocate extra space for another array, you must do this in place with constant memory.

# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

# Example:
# Given input array nums = [3,2,2,3], val = 3

# Your function should return length = 2, with the first two elements of nums being 2.

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        j=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[j]=nums[i]
                j+=1
            i+=1
        for k in range(j):
        	print nums[k]
        return j
 
if __name__ == "__main__":
    print (Solution().removeElement([1,2,3,4,5,5],5))