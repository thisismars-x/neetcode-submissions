class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        from collections import defaultdict

        graph = defaultdict(list)

        for u, v in tickets:
            graph[u].append(v)

        for u in graph:
            graph[u].sort(reverse=True)

        route = []

        def dfs(u: str):
            while graph[u]:
                v = graph[u].pop()
                dfs(v)

            route.append(u)

        dfs("JFK")

        return route[::-1]