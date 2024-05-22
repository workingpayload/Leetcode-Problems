class Solution:
    def isPalindrome(self, s):
        i, j = 0, len(s)-1
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def backtrack(self, s, combo, partitions):
        temp = list(combo)
        if self.isPalindrome(s):
            if tuple(temp+[s]) not in partitions:
                partitions.add(tuple(temp+[s]))
        for i in range(1,len(s)):
            if self.isPalindrome(s[:i]):
                self.backtrack(s[i:],tuple(temp+[s[:i]]),partitions)

    def partition(self, s: str) -> List[List[str]]:
        partitions = set()
        self.backtrack(s,(),partitions)
        answer = []
        for p in partitions:
            answer.append(list(p))
        return answer
        