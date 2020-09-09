from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.bfs(i=i, j=j, grid=grid)
                    count += 1
        return count

    def bfs(self, i, j, grid):
        """
        i: index for vertically

        j: index for horizonrally
        """
        # Illegal case (list index out of range. when index is -1, grid return last element.)
        if i>=len(grid) or j>=len(grid[0]) or i<0 or j<0:
            return
        # Base case
        if grid[i][j] != "1":
            return
        grid[i][j] = "#"                # checked
        self.bfs(i=i+1, j=j, grid=grid) # 真下の要素
        self.bfs(i=i-1, j=j, grid=grid) # 真上の要素
        self.bfs(i=i, j=j-1, grid=grid) # 直前の要素
        self.bfs(i=i, j=j+1, grid=grid) # 直後の要素


if __name__ == "__main__":
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"],
    ]
    s = Solution()
    ans = s.numIslands(grid=grid)
    print(ans)