class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for i in range(len(strs[0])):
            char=strs[0][i]
            for s in strs:
                if i>=len(s) or char!=s[i]:
                    return strs[0][:i]
        return strs[0]

"""Brute force approach 

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        strs.sort()                 # 1. Sort alphabetically
        first = strs[0]             # 2. First word (index 0!)
        last = strs[-1]             # 3. Last word (index -1)
        
        i = 0
        # Compare characters while within bounds of both words and matching
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
            
        return first[:i]


"""