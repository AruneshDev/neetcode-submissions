class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited=set()
        #stores unique values
        for num in nums:
            if num in visited:
                return True
            else:
                visited.add(num)
        return False

























        # visited=set()
        # for num in nums:
        #     if num in visited:
        #         return True
        #     visited.add(num)
        # return False



