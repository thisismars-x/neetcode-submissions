class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        table = {c:i for i, c in enumerate(order)}
        return words == sorted(words, key=lambda x: [table[y] for y in x])