class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False

        from collections import Counter
        count = Counter(hand)

        for card in sorted(count):
            if count[card] > 0:
                freq = count[card]

                for i in range(card, card + groupSize):
                    if count[i] < freq:
                        return False
                    count[i] -= freq

        return True

