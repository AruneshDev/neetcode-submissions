class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # #Brute Force
        # lst = []
        # for i in range(len(numbers)):
        #     for j in range(i+1,len(numbers)):
        #         if numbers[i]+numbers[j]==target:
        #             lst.append(i+1)
        #             lst.append(j+1)
        # return lst
        diff = 0
        prevMap = {}
        for i,n in enumerate(numbers):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff]+1,i+1]
            prevMap[n]=i
        return
