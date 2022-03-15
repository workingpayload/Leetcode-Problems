class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        cnt_open, cnt_close, res = 0, 0, ''
        for ch in s:
            if ch == '(': cnt_open += 1
            if ch == ')': cnt_close += 1
            if cnt_open < cnt_close:
                cnt_close -= 1
            else:
                res = res + ch

        s = res
        
        cnt_open, cnt_close, res = 0, 0, ''
        for ch in reversed(s):
            if ch == '(': cnt_open += 1
            if ch == ')': cnt_close += 1
            if cnt_close < cnt_open:
                cnt_open -= 1
            else:
                res = ch + res
                
        return res
        