class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dictionary to map index and number
        prevInput={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in prevInput:
                return [prevInput[diff],i]
            prevInput[n]=i
