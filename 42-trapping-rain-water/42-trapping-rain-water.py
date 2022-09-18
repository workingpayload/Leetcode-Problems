class Solution:
    def trap(self, height: List[int]) -> int:
        maximum = max(height)
        tol = maximum * len(height)
        pre = 0
        for i, h in enumerate(height):
            if h > pre:
                tol -= i * (h-pre)
                pre = h
                if h == maximum:
                    break
        pre = 0
        for i, h in reversed(list(enumerate(height))):
            if h > pre:
                tol -= (len(height) - i - 1) * (h-pre)
                pre = h
                if h == maximum:
                    break
        tol -= sum(height)
        return tol