class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        snums = sorted(nums)
        med = snums[int(len(snums) / 2)]
        minMoveCount = 0
        for n in snums: minMoveCount += abs(n-med)
        return minMoveCount