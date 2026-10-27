class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:

        # naive brute force does not work for 10^5
        
        # result = []
        # stack = []

        # for i in range(len(temperatures)):
        #     stack.append(temperatures[i])

        #     for j in range(i + 1, len(temperatures)):
        #         stack.append(temperatures[j])
        #         if temperatures[j] > temperatures[i]:
        #             break

        #     if stack[-1] <= temperatures[i]:
        #         result.append(0)
        #         stack = []
        #     else:
        #         i = 0
        #         while stack:
        #             i += 1
        #             stack.pop()
        #         result.append(i - 1)

        # return result

        result = [ 0 ] * len(temp)
        stack = []

        for (i, t) in enumerate(temp):
            while stack and stack[-1][0] < t:
                temp, index = stack.pop()
                result[index] = i - index
            stack.append((t, i))

        return result


