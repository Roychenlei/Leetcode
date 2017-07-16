class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        k=0
        for i in numbers:
            x=i
            if target-x in dict:
                return (dict[target-x]+1,k+1)
            dict[x]=k
            k += 1

if __name__ == "__main__":
    print (Solution().twoSum([2,7,11,15],18))