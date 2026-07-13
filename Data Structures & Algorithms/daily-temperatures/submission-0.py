class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        outcome=[0]*len(temperatures)
        stack=[]
        for i,current_temp in enumerate(temperatures):
            while stack and current_temp>temperatures[stack[-1]]:
                previous_index=stack.pop()
                outcome[previous_index]=i-previous_index

            stack.append(i)

        return outcome
            
            