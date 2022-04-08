from sortedcontainers import SortedList


class KthLargest(object):

    def __init__(self, k, nums):
        self.k, self.sl = k, SortedList(nums)
        

    def add(self, val):
        self.sl.add(val) 
        return self.sl[-self.k]  


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)