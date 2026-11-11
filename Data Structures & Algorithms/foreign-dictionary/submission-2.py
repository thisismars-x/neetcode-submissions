class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        from collections import defaultdict
        adj = {c: set() for w in words for c in w}

        for word1, word2 in zip(words, words[1:]):
            n1, n2 = len(word1), len(word2)

            if n1 > n2 and word1[:n2] == word2[:n2]:
                return ''

            for char1, char2 in zip(word1, word2):
                if char1 != char2:
                    adj[char1].add(char2)
                    break

        indegree = {c: 0 for c in adj}
            
        for u in adj:
            for v in adj[u]:
                indegree[v] += 1

        from collections import deque
        d = deque(x for x in indegree if indegree[x] == 0)

        res = []

        while d:
            node = d.popleft()
            res.append(node)

            for children in adj[node]:
                indegree[children] -= 1
                if indegree[children] == 0:
                    d.append(children)

        return ''.join(res) if len(res) == len(adj) else ''
