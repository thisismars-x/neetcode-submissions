class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        n = len(people)
        l, r = 0, n - 1

        saved = 0
        while l <= r:
            left = limit - people[r]
            r -= 1
            saved += 1

            if l <= r and people[l] <= left:
                l += 1

        return saved
            