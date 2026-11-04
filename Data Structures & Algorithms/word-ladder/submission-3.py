class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        # perform a bfs from beginWord to endWord
        if endWord not in wordList: return 0
        words = set(wordList)

        from collections import deque
        d = deque([(beginWord, 1)])
        
        while d:
            word, dist = d.popleft()
            if word == endWord:
                return dist

            from string import ascii_lowercase

            for i in range(len(word)): # which character to replace
                for char in ascii_lowercase:
                    tmp_word = word[:i] + char + word[i+1:]

                    if tmp_word in words:
                        words.remove(tmp_word)
                        d.append((tmp_word, dist + 1))

        return 0