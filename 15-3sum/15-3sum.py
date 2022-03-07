class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 2:
            return []
        
        nums.sort()
        ans = set()
        for i in range(len(nums)):
            j,k = i+1, len(nums)-1
            while j<k:
                if i == j:
                    j += 1
                if i == k:
                    k -= 1
                if j == k:
                    k -= 1
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    ans.add((nums[i], nums[j], nums[k]))
                    j += 1
                elif s < 0:
                    j += 1
                else:
                    k -= 1
                    
        for a in ans:
            a = [a[0], a[1], a[2]]
            
        return list(ans)    