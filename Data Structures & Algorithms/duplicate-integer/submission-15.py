class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appeared=[]
        for n in nums:
            if n in appeared:
                return True
            else:
                appeared.append(n)
        return False        
            
