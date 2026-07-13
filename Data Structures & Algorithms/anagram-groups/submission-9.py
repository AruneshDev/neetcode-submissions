class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # intuition 
        # use letters of strs as key so any other word containing them in the same freq 
        # can be grouped together
        # using hash tables
        res=defaultdict(list)
        for s in strs:
            count=[0]*25
            for c in s:
                count[ord(c)-ord('a')]+=1
            res[tuple(count)].append(s)
        return list(res.values())






















