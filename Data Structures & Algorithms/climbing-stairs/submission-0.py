class Solution:
    def climbStairs(self, n: int) -> int:
        series=[0,1]
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            for i in range(2,n+2):
                series.append(series[i-1]+series[i-2])
        return series[-1]
            
        
                