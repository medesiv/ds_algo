class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc]==newColor:
            return image
        dirs = [[-1,0],[1,0],[0,-1],[0,1]]
        def dfs(image,sr,sc,newColor,oldColor):
            if sr>=len(image) or sc >=len(image[0]) or sc<0 or sr<0 or image[sr][sc]!=oldColor:
                return
            image[sr][sc]=newColor
            for d in dirs:
                dfs(image,d[0]+sr,d[1]+sc,newColor,oldColor)
        dfs(image,sr,sc,newColor,image[sr][sc])
        return image
    