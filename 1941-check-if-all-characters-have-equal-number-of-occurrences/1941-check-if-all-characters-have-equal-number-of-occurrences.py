class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        a = Counter(s).values()
        flag = 1
        nums = []
        for i in a:
            nums.append(i)

        for i in range(len(nums)-1):
            if nums[i]!=nums[i+1]:
                flag = 0
        return flag  
