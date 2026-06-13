from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list) # str: list[tuple(int, str)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        tvPairs = self.timeMap[key]

        L = 0
        R = len(tvPairs) - 1
        while L <= R:
            M = L + (R - L) // 2

            if tvPairs[M][0] == timestamp:
                return tvPairs[M][1]

            elif timestamp > tvPairs[M][0]:
                L = M + 1
            
            else:
                R = M - 1
        # get next smallest value if not found 
        if L - 1 >= 0 and tvPairs[L - 1][0] < timestamp:
            return tvPairs[L - 1][1]
        else:
            return ""
        
