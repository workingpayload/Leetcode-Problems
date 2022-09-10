class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        unique = set(s)
        for letter in unique:
            index = s.index(letter) # get the first index of the letter
            dis = distance[ord(letter)-97]
            if index+dis+1 > len(s)-1 or s[index+dis+1] != letter:
                return False
        return True
        