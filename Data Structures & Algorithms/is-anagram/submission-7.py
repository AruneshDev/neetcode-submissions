class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check the length
        if len(s)!=len(t):
            return False
        # by definition anagrams are strings containing exact same letters
        # create an empty dictionary 
        countS,countT={},{}
        for i in range(len(s)):
            countS[s[i]]=1+countS.get(s[i],0)
            countT[t[i]]=1+countT.get(t[i],0)
        return countS==countT
        
  
  
  
  
  
  
  
  
  
        # if len(s)!=len(t):
        #     return False
        
        # countS,countT={},{}
        # for i in range(len(s)):
        #     countS[s[i]]=1+countS.get(s[i],0)
        #     countT[t[i]]=1+countT.get(t[i],0)
        # return countS == countT
  
  
  