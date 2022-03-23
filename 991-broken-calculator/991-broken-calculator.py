class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        if target <= startValue:
            return startValue - target
        if target % 2 == 0:
            return 1 + self.brokenCalc(startValue, target // 2)
        else:
            return 1 + self.brokenCalc(startValue, target + 1)
        