from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        return the maximun number in adjacent 1s    
        """
        m = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    m = max(m, self.count1(i=i, j=j, grid=grid))
        return m
    
    def count1(self, i, j, grid):
        """
        Count the number of adjacent 1s
        """
        # Illegal case (list index out of range. when index is -1, grid return last element.)
        if i>=len(grid) or j>=len(grid[0]) or i<0 or j<0:
            return 0
        # Base case
        if grid[i][j] != 1:
            return 0
        # checked
        grid[i][j] = -1
        return 1 \
            + self.count1(i=i+1, j=j, grid=grid) \
            + self.count1(i=i-1, j=j, grid=grid) \
            + self.count1(i=i, j=j-1, grid=grid) \
            + self.count1(i=i, j=j+1, grid=grid)


if __name__ == "__main__":
    grid = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0],
    ]
    s = Solution()
    ans = s.maxAreaOfIsland(grid=grid)
    print(ans)