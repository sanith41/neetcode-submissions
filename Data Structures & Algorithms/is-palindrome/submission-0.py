class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss=s.replace(" ","").lower()
        st="".join(char for char in ss if char.isalnum())
        print(st)
        l=len(st)
        j=l-1
        i=0
        while i<l//2 and j>=0:
            if st[i]!=st[j]:
                return False
            else:
                i=i+1
                j=j-1
        return True
        
        