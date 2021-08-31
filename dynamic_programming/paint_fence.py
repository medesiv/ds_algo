class Solution:
    def numWays(self, n: int, k: int) -> int:
        """
        :type n:int
        :type k:int
        :rtype: int
        
        """
        
        if n == 0:
            return 0
        if n == 1:
            return k
        
        same = [0] * (n+1)
        different = [0] * (n+1)
        total = [0] * (n+1)
        
        
        same[2] = k * 1 #No. of ways to paint i posts such that i and i-1 have same color
        different[2] = k*(k-1) #No. of ways to paint i posts such that i and i-1 have different color
        total[2] = same[2]+different[2] #Total no. of ways to paint posts 0..i
        
        for i in range(3,n+1):
            print(n,i)
            same[i] = different[i-1]
            different[i] = total[i-1]*(k-1)
            total[i] = same[i] + different[i]
        return total[n]
        