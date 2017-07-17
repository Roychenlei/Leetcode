class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # two pointer : one for increment,one for traverse
        y = 0
        a = len(nums)

        for i in range(a):
            if nums[i] :
                nums[i], nums[y] = nums[y], nums[i]
                y += 1
        return nums



if __name__ == '__main__':
    print (Solution().moveZeroes([0,0,0,0,2,0,1]))