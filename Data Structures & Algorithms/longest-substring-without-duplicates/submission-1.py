class Solution:
    def lengthOfLongestSubstring(self,s):
        seen=set()
        left=0
        longest=0
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[i])
            longest=max(longest,i-left+1)
        return longest
        