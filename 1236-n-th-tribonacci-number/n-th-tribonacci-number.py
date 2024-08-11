class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n <= 2: return 1
        import numpy as np

        M = np.array([[1, 1, 1], [1, 0, 0], [0, 1, 0]])
        A = np.linalg.matrix_power(M, n - 2) @ np.array([[1], [1], [0]])

        return A[0, 0]