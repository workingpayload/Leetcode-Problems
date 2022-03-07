class Solution:
    def average(self, salary: List[int]) -> float:
        mini = min(salary)
        maxi = max(salary)
        sum = 0
        count = 0
        for i in range(len(salary)):
            if salary[i]!=mini and salary[i]!=maxi:
                sum+=salary[i]
                count+=1
        return sum/count        
        