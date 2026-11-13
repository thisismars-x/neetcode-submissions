class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        if 1 in nums:
            return False
        
        visited = set()

        adj = defaultdict(list)

        def GCD(a: int, b: int) -> int:
            for i in range(min(a, b), 1, -1):
                if a % i == 0 and b % i == 0:
                    return i

            return 1

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if GCD(nums[i], nums[j]) > 1:
                    # the reason we can append both is because j only looks ahead
                    adj[nums[i]].append(nums[j])
                    adj[nums[j]].append(nums[i])

        def _dfs(node: int):
            visited.add(node)
            
            for children in adj[node]:
                if children not in visited:
                    _dfs(children)

        _dfs(nums[0])
        for num in nums:
            if num not in visited:
                return False

        return True