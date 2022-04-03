class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = [[],[]]
        
        for i in nums1:
            if i not in nums2:
                if i not in ans[0]:
                    ans[0].append(i)
                
        for j in nums2:
            if j not in nums1:
                if j not in ans[1]:
                    ans[1].append(j)
                
                
        return ans        
        