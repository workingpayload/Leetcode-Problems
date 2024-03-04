class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        n = len(tokens)
        i = 0
        j = n
        score = 0
        ans = 0
        tokens.sort()
        
        while i < j:
            if power >= tokens[i]:
                power -= tokens[i]
                score+=1
                i+=1
                ans = max(ans, score)
            elif score >= 1 and j > i + 1:
                j-=1
                power += tokens[j]
                score-=1
            else: 
                return ans
            
        return ans
        