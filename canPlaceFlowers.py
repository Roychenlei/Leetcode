class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        for i,c in enumerate(flowerbed):
            if (not c and (i==0 or not flowerbed[i-1])) and (i==len(flowerbed)-1 or not flowerbed[i+1]):
                n-=1
                flowerbed[i]=1
                if n<=0: return True
        return not n

if __name__ == '__main__':
    print (Solution().canPlaceFlowers([0,0,0,0,1,0,1],1))