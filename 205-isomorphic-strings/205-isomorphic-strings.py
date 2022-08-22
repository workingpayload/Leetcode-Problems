class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        data = {}
        for i, j in zip(s,t):
            if i not in data:
                if j in data.values():
                            return False
                data[i] = j
            elif i in data and data[i] != j:
                            return False
        return True
      