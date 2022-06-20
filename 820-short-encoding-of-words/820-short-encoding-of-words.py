class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key=len, reverse=True)
        res = []
        for suffix in words:
            if not any(word.endswith(suffix) for word in res):  # check that this word is not actually a suffix
                res.append(suffix)
        return sum(len(word)+1 for word in res)