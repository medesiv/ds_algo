class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        ans = 0
        table = [[0]*(n+1) for _ in range(m+1)]
        
        for r in range(m):
            for c in range(n):
                if nums2[c] == nums1[r]:
                    table[r][c] = 1+table[r-1][c-1]
                    ans = max(table[r][c],ans)
                    
        return ans