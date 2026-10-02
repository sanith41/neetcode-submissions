class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=[]
        m=0
        maxi=1
        i=0
        j=i+1
        if len(s)==0:
            return 0
        while i<len(s):
            
            while j<len(s) and s[j] not in s[i:j]:
                maxi=max(maxi,len(s[i:j])+1)
                j=j+1
                
            i=i+1

            

            
        return maxi
        