class Solution:
    def countOrders(self, n: int) -> int:
        p = 10**9+7
        fact = 1
        for i in range(1,n+1):
            fact = fact*i
            fact = fact * (2*i-1)
            fact = fact%p
        return fact    