class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numdict = defaultdict(int) # number: frequency 
        for num in nums:
            numdict[num] += 1
        revdict = defaultdict(list) # frequency: number
        for key, v in numdict.items():
            revdict[v].append(key)

        ranking = sorted(revdict.keys(), reverse=True)
        topNums = []
        for freq in ranking:    
            for number in revdict[freq]:
                topNums.append(number)
                if len(topNums) == k:
                    return topNums

        return topNums

        
        