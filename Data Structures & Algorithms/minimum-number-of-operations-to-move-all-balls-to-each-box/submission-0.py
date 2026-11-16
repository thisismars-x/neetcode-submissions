class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        pos = []
        for i in range(len(boxes)):
            if boxes[i] == '1':
                pos.append(i)

        res = [ 0 ] * len(boxes)

        for i in range(len(boxes)):
            dist = 0
            for j in pos:
                dist += abs(j - i)
            res[i] = dist

        return res
