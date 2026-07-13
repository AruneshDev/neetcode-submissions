class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Brute Force
        lst = []
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                if numbers[i]+numbers[j]==target:
                    lst.append(i+1)
                    lst.append(j+1)
        return lst