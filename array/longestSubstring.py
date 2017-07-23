#!/user/bin/env python
#coding: 'utf-8'
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        ans = 0
        left = 0
        last = {}
        for i in range(len(s)):
            if s[i] in last and last[s[i]] >= left:
                left = last[s[i]] + 1
            last[s[i]] = i
            ans = max(ans, i - left + 1)
        return ans    

if __name__ == '__main__':
	print (Solution().lengthOfLongestSubstring("seweasdfghjklmmmmsdm"))






        