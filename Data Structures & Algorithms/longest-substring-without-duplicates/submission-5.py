class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window=set()
        max_len=0
        left=0
        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left+=1
            max_len=max(max_len,right-left+1)
            window.add(s[right])
        return max_len if max_len!=0 else 0
                
