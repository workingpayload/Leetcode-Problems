class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        return [pattern.find(i) for i in pattern]==  [s.split().index(j) for j in s.split()]