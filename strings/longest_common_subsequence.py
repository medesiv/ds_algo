class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        table = [[0]*(n+1) for _ in range(m+1)]
        
        for r in range(m+1):
            for c in range(n+1):
                if text2[c-1] == text1[r-1]:
                    table[r][c] = 1+table[r-1][c-1]
                else:
                    table[r][c]= max(table[r][c-1],table[r-1][c])
                    
        #return table[m-1][n-1]

        index = table[m][n]
  
        # Create a character array to store the lcs string
        lcs = [""] * (index+1)
        lcs[index] = ""
      
        # Start from the right-most-bottom-most corner and
        # one by one store characters in lcs[]
        i = m 
        j = n
        while i > 0 and j > 0:
      
            # If current character in X[] and Y are same, then
            # current character is part of LCS
            if text1[i-1] == text2[j-1]:
                lcs[index-1] = text1[i-1]
                i-=1
                j-=1
                index-=1
      
            # If not same, then find the larger of two and
            # go in the direction of larger value
            elif table[i-1][j] > table[i][j-1]:
                i-=1
            else:
                j-=1
      
        print("LCS of " + text1 + " and " + text2 + " is " + "".join(lcs))


s = Solution()
print(s.longestCommonSubsequence("AGGTAB","BAGXTXAYB"))