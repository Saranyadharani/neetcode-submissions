from collections import Counter #usinga counter to map the char and its freq
class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1)>len(s2):
            return False
        s1_count=Counter(s1) 
        window_count=Counter()
        for i in range(len(s2)):
            window_count[s2[i]]+=1
            if i>=len(s1):
                left_char=s2[i-len(s1)]
                if window_count[left_char]==0:
                    del window_count[left_char]
                else:
                    window_count[left_char]-=1
            if window_count==s1_count:
                return True
        return False       