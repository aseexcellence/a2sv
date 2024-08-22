class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # Possible knight moves
        knight_moves = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]
        # memory to not calculate repeated works again and again
        cache = [[[None] * (k + 1) for _ in range(n)] for _ in range(n)]
        has_cache = [[[False] * (k + 1) for _ in range(n)] for _ in range(n)]

        '''
        We're required to calculate the probability that the knight remains on the board after
        k moves. Let's take x and y, arbitrary points on the board so, we should find the
        probability that we land on x, y after exactly k moves
        '''

        def dfs(x, y, k):
            if k == 0:
                return 1.0 if x == row and y == column else 0.0
            if has_cache[x][y][k]:
                return cache[x][y][k]
            
            total_probability = 0.0
            for dx, dy in knight_moves:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < n:
                    total_probability += dfs(nx, ny, k - 1)
            has_cache[x][y][k] = True
            cache[x][y][k] = total_probability / 8.0
            return cache[x][y][k]

        total_probability = 0.0
        for x in range(n):
            for y in range(n):
                total_probability += dfs(x, y, k)
        return total_probability
