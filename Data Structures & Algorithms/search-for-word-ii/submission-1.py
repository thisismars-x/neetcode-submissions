
class Try:
    def __init__(self):
        self.children, self.i, self.refs = [None] * 26, -1, 0

    def add(self, w: tuple[str, int]):
        curr = self
        word, i = w
        curr.refs += 1

        for c in word:
            index = ord(c) - ord('a')
            if not curr.children[index]:
                curr.children[index] = Try()
            curr = curr.children[index]
            curr.refs += 1
        curr.i = i


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        r, c = len(board), len(board[0])

        root = Try()
        for (i, w) in enumerate(words):
            root.add((w, i))

        res = []

        def _dfs(i: int, j: int, node: Try):
            if not (0 <= i < r and 0 <= j < c) or board[i][j] == '*' or not node.children[ord(board[i][j]) - ord('a')]:
                return 0

            tmp = board[i][j]
            board[i][j] = '*'
            prev = node
            node = node.children[ord(tmp) - ord('a')]

            found = 0
            if node.i != -1:
                res.append(words[node.i])
                node.i = -1
                found += 1

            found += _dfs(i + 1, j, node)
            found += _dfs(i - 1, j, node)
            found += _dfs(i, j + 1, node)
            found += _dfs(i, j - 1, node)

            board[i][j] = tmp
            node.refs -= found

            if not node.refs:
                prev.children[ord(tmp) - ord('a')] = None
            return found

        for i in range(r):
            for j in range(c):
                root.refs -= _dfs(i, j, root)

        return res