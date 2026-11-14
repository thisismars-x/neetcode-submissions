class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [ list(col) for col in zip(*matrix) ]
