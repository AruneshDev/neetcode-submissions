class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dictionary to map index and number
        prev_input={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in prev_input:
                return[prev_input[diff],i]
            prev_input[n]=i
        


