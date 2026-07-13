class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        for i in range(len(s)):
            charSet=set()
            for j in range(i,len(s)):
                if s[j] in charSet:
                    break
                charSet.add(s[j])
            res=max(res,len(charSet))
        return res
        
        
        
        
        
        
        
        
        
        
        # l=0
        # longest=0
        # setofchar = set()
        # n=len(s)
        # for r in range(len(s)):
        #     while s[r] in setofchar:
        #         setofchar.remove(s[l])
        #         l+=1

        #     w=r-l+1
        #     longest=max(longest,w)
        #     setofchar.add(s[r])
        # return longest
