class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff = high - low

        if high % 2 !=0 or low %2 !=0:
            return diff //2 +1
        else:
            return diff // 2