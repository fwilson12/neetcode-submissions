class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        res = [0] * n
        
        stack = [] # list of tuples: (idx, temp)
        for i in range(n):
            while stack and temperatures[i] > stack[-1][1]:
                day = stack.pop()
                res[day[0]] = i - day[0]
            stack.append((i, temperatures[i]))

        return res





