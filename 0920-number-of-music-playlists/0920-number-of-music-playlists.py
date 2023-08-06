class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        @lru_cache(None)
        def dp(uniques, repeats, rem, songsTilNewRepeat):
            if songsTilNewRepeat == 0:
                repeats += 1
                songsTilNewRepeat = 1
            if uniques > rem:
                return 0
            if rem == 0:
                return 1
            
            res = 0
            # either pick from uniques, or from repeats
            if uniques > 0:
                res += dp(uniques - 1, repeats, rem - 1, songsTilNewRepeat - 1) * uniques
            if repeats > 0:
                res += dp(uniques, repeats - 1, rem - 1, songsTilNewRepeat - 1) * repeats
            return res

        
        return dp(n, 0, goal, k + 1) % (10 ** 9 + 7)