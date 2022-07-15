class Solution:
    def fillCups(self, amount: List[int]) -> int:
        m,s = max(amount),sum(amount)
        return max(m,s//2+s%2)
        