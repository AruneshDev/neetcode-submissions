class Solution:
    def twoSum(self,nums:List[int],target:int)->List[int]:
        prev_input={}
        #empty dictionary to store nums as keys and indices as values
        for i,n in enumerate(nums):
            diff = target-n
            if diff in prev_input:
                return [prev_input[diff],i]
            prev_input[n]=i
            