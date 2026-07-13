class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_prod=1
        zero_count=0
        for n in nums:
            if n==0:
                zero_count+=1
            else:
                total_prod *= n
        res=[]
        for n in nums:
            if zero_count>1:
                res.append(0)
            elif zero_count==1:
                res.append(total_prod if n==0 else 0)
            else:
                res.append(total_prod//n)
        return res
        
        
        # res = [1]*(len(nums))
        # prefix = 1

        # for i in range(len(nums)):
        #     res[i] = prefix
        #     prefix *= nums[i]
        
        # postfix = 1

        # for i in range(len(nums)-1,-1,-1):
        #     res[i] *= postfix
        #     postfix*=nums[i]    

       
       
       
        # return res
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # res = [1]*(len(nums))
        # prefix = 1
        # for i in range(len(nums)):
        #     res[i]=prefix
        #     prefix *= nums[i]
        # postfix=1
        # for i in range(len(nums)-1,-1,-1):
        #     res[i] *= postfix
        #     postfix *= nums[i]
        # return res
       
       
       
       
       
