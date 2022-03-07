class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = min(strs,key=len)
        
        while len(pre)>0:
            if all([i.startswith(pre) for i in strs]):
                break
            pre = pre[:-1]
        return pre    