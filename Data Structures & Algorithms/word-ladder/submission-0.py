class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        if beginWord == endWord: return 0

        words = set(wordList)

        res = 0
        from collections import deque
        d = deque([beginWord])
        while d:
            l = len(d)
            res += 1
            for _ in range(l):
                node = d.popleft()
                if node == endWord:
                    return res
                    
                import string
                # change the character in the node
                for i in range(len(node)):
                    for c in string.ascii_lowercase:
                        if c == node[i]: continue
                        tmp = node[:i] + c + node[i+1:]
                        if tmp in words:
                            d.append(tmp)
                            words.remove(tmp)
        
        return 0

