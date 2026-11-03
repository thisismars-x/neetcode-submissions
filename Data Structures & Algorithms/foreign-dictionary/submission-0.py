class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        # so this solution is kahns algo using topo sort??
        adj = {c: set() for w in words for c in w}
        # compare first and next word
        for w1, w2 in zip(words, words[1:]):
            n1, n2 = len(w1), len(w2)
            # if n2 > n1 and w1[:n1] == w2[:n1]:
            #     return ''

            if n1 > n2 and w1[:n2] == w2[:n2]:
                return ''

            for cw1, cw2 in zip(w1, w2):
                if cw1 != cw2:
                    adj[cw1].add(cw2)
                    break

        indegree = {c: 0 for c in adj}
        for u in adj:
            for v in adj[u]:
                indegree[v] += 1

        from collections import deque
        d = deque(i for i in indegree if indegree[i] == 0)
        res = []

        while d:
            node = d.popleft()
            res.append(node)

            for children in adj[node]:
                indegree[children] -= 1
                if indegree[children] == 0:
                    d.append(children)

        return "".join(res) if len(res) == len(adj) else ''