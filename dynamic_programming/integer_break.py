class Solution:
    def integerBreak(self, n: int) -> int:
        
        #What could the last peice be?
        #The last possible peice could be of length 1,2,3,..n
        #Let f(n) = max possible prod obtained from 1,...n
        #In general, f(i) = max possible product obtainable from rod of length i
        #The overall rod must be broken at lease once, but the smaller pieces don't have to be broken further in general, so lets ignore the requirement that overall rod must be broken at least once, and handle it as special case
        
        
        if n == 2: # Rod of length 2 must be broken into 1 and 1
            return 1
        
        table = [0] * (n+1) #table[0] has no meaning but just creating table at index i
        table[1] = 1
        table[2] = 2 #Note that subproblem rods don't have to be split up (unlike the special case above with overall rod size being 2)
        
        for i in range(3, n+1):
            if i == n: #Special case: The overall rod must be split at least once, so we won't consider it remaining at length n, pick any valid split(eg. 1 and n-1) and initialize best so far to be 1*(n-1) or 2*(n-2) doesn't really matter
                best = 1*(n-1)
            else:
                best = i # If rod was not cut at all this would be the default product
            for j in range(1,i): #If it was cut, then the last peice could be of length 1,..i-1
                if table[j]*table[i-j] > best:
                    best = table[j]*table[i-j]
            table[i] = best #The best product including no split case defines the value of table[i]
            
        return table[n]