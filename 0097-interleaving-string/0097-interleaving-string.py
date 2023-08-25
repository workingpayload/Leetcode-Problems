from functools import lru_cache


class Solution:
    def isInterleave(self, a: str, b: str, target: str) -> bool:
        n, m = len(a), len(b)

        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> bool:
            if i == n and j == m:
                return True
            return any([
                i < n and a[i] == target[i + j] and dp(i + 1, j),
                j < m and b[j] == target[i + j] and dp(i, j + 1),
            ])

        return n + m == len(target) and dp(0, 0)