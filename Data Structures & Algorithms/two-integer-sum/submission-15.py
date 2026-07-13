class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # value and index mapping
        prev_input_map={}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in prev_input_map:
                return [prev_input_map[diff],i]
            prev_input_map[n]=i
        