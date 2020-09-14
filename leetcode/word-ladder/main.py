from typing import List
from collections import defaultdict
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        d = defaultdict(list)
        l = len(beginWord)
        for word in wordList:
            for i in range(l):
                d[word[:i] + "*" + word[i+1:]].append(word)
        
        q = deque()
        q.append((beginWord, 1))
        chked = {beginWord: True}
        
        while q:
            k,v = q.popleft()
            for i in range(l):
                w = k[:i] + "*" + k[i+1:]
                for word in d[w]:
                    if word == endWord:
                        return v+1
                    if word not in chked:
                        chked[word] = True
                        q.append((word, v+1))
        return 0


if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    s = Solution()
    ans = s.ladderLength(beginWord=beginWord, endWord=endWord, wordList=wordList)
    print(ans)