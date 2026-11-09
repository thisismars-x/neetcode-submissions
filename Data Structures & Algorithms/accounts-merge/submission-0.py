class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        class DSU:
            def __init__(self, n: int):
                self.par = list(range(n))

            def find(self, n: int):
                while self.par[n] != n:
                    self.par[n] = self.par[self.par[n]]
                    n = self.par[n]
                return n

            def union(self, a: int, b: int):
                ra, rb = self.find(a), self.find(b)
                if ra == rb:
                    return False

                self.par[ra] = rb
                return True

        
        n = len(accounts)
        uf = DSU(n)
        email_to_acc = {}

        for i, a in enumerate(accounts):
            for email in a[1:]:
                if email in email_to_acc:
                    uf.union(i, email_to_acc[email])
                else:
                    email_to_acc[email] = i

        from collections import defaultdict
        mail_grp = defaultdict(list)

        for email, i in email_to_acc.items():
            leader = uf.find(i)
            mail_grp[leader].append(email)

        res = []
        for i, emails in mail_grp.items():
            res.append([accounts[i][0]] + sorted(mail_grp[i]))

        return res