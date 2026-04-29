class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        coolmap = {} # str: List[str]
        for word in strs:
            if "".join(sorted(word)) in coolmap:
                coolmap["".join(sorted(word))].append(word) 
            else:
                coolmap["".join(sorted(word))] = [word]

        returnArr = []
        for wordlist in coolmap:
            returnArr.append(coolmap[wordlist])
        return returnArr

