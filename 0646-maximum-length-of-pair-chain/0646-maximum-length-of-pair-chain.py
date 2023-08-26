class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:

        ans, chainEnd = 0, -inf
        pairs.sort(key = lambda x: x[1])

        for l, r in pairs:
            if l > chainEnd:
                ans+= 1
                chainEnd = r

        return  ans