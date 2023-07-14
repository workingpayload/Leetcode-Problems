class Solution:
    def longestSubsequence(self, arr: List[int], d: int) -> int:

        subseqs = {}
        for n in arr:
            cnt_prev = subseqs.get(n, 0)
            cnt_next = subseqs.get(n+d,0)
            subseqs[n+d] = max(cnt_prev + 1, cnt_next)
        
        return max(subseqs.values())