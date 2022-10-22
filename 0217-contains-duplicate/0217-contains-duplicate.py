class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_num = set()
        
        for i in nums:
            if i not in set_num:
                set_num.add(i)
            else:
                return True
            
        return False
        