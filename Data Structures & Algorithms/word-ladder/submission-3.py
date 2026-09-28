from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #define a set for the wordlist
        wordset=set(wordList)
        if endWord not in wordset:
            return 0
        queue=deque([(beginWord,1)]) #word,level
        visited=set([beginWord])
        # if there nodes in the queue
        while queue:
            word,level=queue.popleft()
            for i in range(len(word)):
                for c  in "abcdefghijklmnopqrstuvwxyz":
                    new_word=word[:i]+c+word[i+1:]
                    if new_word==endWord:
                        return level+1
                    if new_word in wordset and new_word not in visited:
                        visited.add(new_word)
                        queue.append((new_word,level+1))
        return 0