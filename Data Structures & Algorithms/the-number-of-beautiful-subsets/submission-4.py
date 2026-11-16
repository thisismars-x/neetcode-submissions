class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        
        def _dfs(i: int, table: dict[int, int]) -> int:
            if i == len(nums):
                return 1

            res = _dfs(i + 1, table)
            if not (table[nums[i] + k] or table[nums[i] - k]):
                table[nums[i]] += 1
                res += _dfs(i + 1, table)
                table[nums[i]] -= 1

            return res

        from collections import defaultdict
        return _dfs(0, defaultdict(int)) - 1 # empty