class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

         # Define the direction maps for each type of tile
        directions = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }

         # Check if we can move from (x, y) to (new_x, new_y)
        def is_valid_move(x, y, new_x, new_y):
            if new_x < 0 or new_x >= m or new_y <0 or new_y >= n:
                return False
            # Check the connection between the current cell and the new cell
            tile1, tile2 = grid[x][y], grid[new_x][new_y]
            direction = (new_x - x, new_y -y)
            # Valid if the new cell allows an opposite move back to the current cell
            return (-direction[0], -direction[1]) in directions[tile2]
            
        def dfs(x, y):
            # If we've reached the bottom-right corner, return True
            if (x, y) == (m - 1, n - 1): return True

            visited[x][y] = True
            for dx, dy in directions[grid[x][y]]:
                new_x, new_y = x + dx, y + dy
                if is_valid_move(x, y, new_x, new_y) and not visited[new_x][new_y]:
                    if dfs(new_x, new_y):
                        return True
            
            return False
        
        # Start DFS from the top-left corner
        return dfs(0, 0)
