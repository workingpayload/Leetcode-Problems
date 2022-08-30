class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s='0'
        size=1
        while size<k:
            s+="1"+''.join(["1" if ch=="0" else "0" for ch in s][::-1])
            size=(size<<1)+1
        return s[k-1]