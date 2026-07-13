class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result=set()
        for num in nums:
            if num in result:
                return True
            else:
                result.add(num)
        return False






        # visited=set()
        # for num in nums:
        #     if num in visited:
        #         return True
        #     visited.add(num)
        # return False



