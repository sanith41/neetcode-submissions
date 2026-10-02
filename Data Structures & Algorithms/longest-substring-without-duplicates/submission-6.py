class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=[]
        m=0
        maxi=1
        
        j=0
        sset=set()
        if len(s)==0:
            return 0
        for i in range(len(s)):
            while s[i] in sset:
                sset.remove(s[j])
                j=j+1
            sset.add(s[i])
            maxi=max(maxi,i-j+1)
        return maxi

        