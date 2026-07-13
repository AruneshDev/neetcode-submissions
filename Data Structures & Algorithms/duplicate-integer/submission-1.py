class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
        #  list=[]
        #  for i in  range(len(nums)):
        #     if nums[i] in list:
        #         return True
        #     else:
        #         list.append(nums[i])
        #  return False
