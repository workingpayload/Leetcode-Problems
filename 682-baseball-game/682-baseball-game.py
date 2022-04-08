class Solution:
    def calPoints(self, ops: List[str]) -> int:
        score = []
        for i in ops:
            if i == "C":
                score.pop(-1)
            elif i == "D":
                score.append(score[-1]*2)
            elif i == "+":
                score.append(score[-2]+score[-1])
            else:
                score.append(int(i))
                
                
        return sum(score)       