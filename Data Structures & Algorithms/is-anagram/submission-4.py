class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        if len(s)!=len(t):
            return False
        s_count=Counter(s)
        t_count=Counter()
        for i in range(len(t)):
            t_count[t[i]]+=1
        if t_count==s_count:
            return True
        else:
            return False

        