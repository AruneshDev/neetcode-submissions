class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # intuition 
        # use letters of strs as key so any other word containing them in the same freq 
        # can be grouped together
        res=defaultdict(list)
        for s in strs:
            sortedS=''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())