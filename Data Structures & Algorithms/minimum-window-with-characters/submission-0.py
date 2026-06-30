class Solution:
    def minWindow(self, s, t):
        from collections import Counter
        
        if len(t) > len(s):
            return ""
        
        need = Counter(t)
        have = {}
        required = len(need)
        formed = 0
        left = 0
        result = (float('inf'), None, None)
        
        for right in range(len(s)):
            char = s[right]
            have[char] = have.get(char, 0) + 1
            
            if char in need and have[char] == need[char]:
                formed += 1
            
            while formed == required and left <= right:
                current_length = right - left + 1
                if current_length < result[0]:
                    result = (current_length, left, right)
                
                left_char = s[left]
                have[left_char] -= 1
                
                if left_char in need and have[left_char] < need[left_char]:
                    formed -= 1
                
                left += 1
        
        return "" if result[0] == float('inf') else s[result[1]:result[2]+1]