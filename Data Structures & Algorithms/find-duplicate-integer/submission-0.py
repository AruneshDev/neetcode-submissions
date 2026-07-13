class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        countofDups={}
        for num in nums:
            if num in countofDups:
                countofDups[num]+=1
            else:
                countofDups[num]=1
        for key,value in countofDups.items():
            if value>1:
                return key
