#!/user/bin/env python
#coding: 'utf-8'

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = pa = pb = pc = None
        na = nb = 0x7FFFFFFF
        for n in nums:
            if n > pa: pa, pb, pc = n, pa, pb
            elif n > pb: pb, pc = n, pb
            elif n > pc: pc = n
            if n < na: na, nb = n, na
            elif n < nb: nb = n
        result = max(ans, pa * na * nb, pa * pb * pc)
        return result

if __name__ == '__main__':
    print (Solution().maximumProduct([1,2,3,5,-4,-100]))