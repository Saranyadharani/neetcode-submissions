class Solution:
    def groupAnagrams(self, strs):
        group={}
        for word in strs:
            freq={}
            for char in word:
                freq[char]=freq.get(char,0)+1
            key=tuple(sorted(freq.items()))
            if key not in group:
                group[key]=[]
            group[key].append(word)
        return list(group.values())