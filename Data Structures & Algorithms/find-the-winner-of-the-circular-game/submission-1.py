class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = [True] * n

        def _ftw(i: int, nel: int) -> int:
            if nel == n - 1:
                return i

            nind = i

            for _ in range(k - 1):
                nind = (nind + 1) % n

                while not players[nind]:
                    nind = (nind + 1) % n

            players[nind] = False

            nind = (nind + 1) % n

            while not players[nind]:
                nind = (nind + 1) % n

            return _ftw(nind, nel + 1)

        return _ftw(0, 0) + 1