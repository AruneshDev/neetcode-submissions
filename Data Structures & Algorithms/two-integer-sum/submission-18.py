class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # value and index mapping
        prev_input={}
        for i,num in enumerate(nums):
            diff=target-num
            if diff in prev_input:
                return [prev_input[diff],i]
            prev_input[num]=i

        