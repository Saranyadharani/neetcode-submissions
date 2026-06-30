class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        if len(s)!=len(t):
            return False
        s_count=Counter(s)
        window_count=Counter()
        for i in range(len(t)):
            window_count[t[i]]+=1
            if window_count==s_count:
                return True
        return False