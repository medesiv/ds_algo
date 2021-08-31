class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        res_start = 0
        res_len = 0
        if len(s) <2:
            return s
        def expandRange(s,begin,end):
            while(begin>=0 and end<len(s) and s[begin]==s[end]):
                begin-=1
                end+=1
            if(end-begin-1>res_len):
                res_start=begin+1
                res_len=end-begin-1
                
        for i in range(len(s)):
            expandRange(s,i,i)
            expandRange(s,i,i+1)
            
        return s[res_start:res_start+res_len]
                