class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    perimeter += 4  # Add 4 for each land cell
                    if r > 0 and grid[r-1][c] == 1:  # Check above
                        perimeter -= 2
                    if c > 0 and grid[r][c-1] == 1:  # Check left
                        perimeter -= 2
        
        return perimeter
