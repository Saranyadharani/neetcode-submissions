from collections import Counter #usinga counter to map the char and its freq
class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1)>len(s2):
            return False
        s1_count=Counter(s1)
        s2_count=Counter()
        left=0
        for right in range(len(s2)):
            s2_count[s2[right]]+=1
            if right-left+1>len(s1):
                left_char=s2[left]
                s2_count[left_char]-=1
                if s2_count[left_char]==0:
                    del s2_count[left_char]
                left+=1
            if s1_count==s2_count:
                return True
        return False