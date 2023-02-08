class Solution:
    def jump(self, nums: List[int]) -> int:
                                            #          0 1 2 3 4
        ans, mx, end = 0, 0, 0              #  nums = [2,3,0,1,4]  
        
        for i, num in enumerate(nums[:-1]): #  i    num   mx    end   ans
                                            # –––   –––   –––   –––   –––
            mx = max(mx, i + num)           #  0     2     2     2     1
                                            #  1     3     4     2     1
            if i == end:                    #  2     0     4     4     2     
                ans += 1                    #  3     1     4     4     2                
                end = mx 

        return ans 