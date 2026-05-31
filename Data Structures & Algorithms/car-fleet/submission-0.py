class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:


        cardict = defaultdict(int) # (pos: speed), positions are unique
        n = len(position)
        for i in range(n):
            cardict[position[i]] = speed[i]

        carstack = sorted(list(cardict)) # cars sorted by distance, ascending
        fleets = 0
        while carstack:
            fleets += 1
            closecar = carstack.pop()
            benchmark_time = (target - closecar) / cardict[closecar] # here closecar represents the position of the car | also note t = d/v lol
            while carstack and (target - carstack[-1]) / cardict[carstack[-1]] <= benchmark_time:
                carstack.pop()
       
        return fleets
        
        