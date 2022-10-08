class Solution:
	def threeSumClosest(self, nums: List[int], target: int) -> int:
		nums.sort()
		min_diff = float("inf")
		closest = None
		prev = None
		
		for i in range(len(nums)-2):
			if nums[i] == prev: continue
			
			prev = nums[i]
			l = i + 1
			r = len(nums) - 1
			while l < r:
				sum_ = nums[i] + nums[l] + nums[r]
				diff = abs(target-sum_)
				if diff == 0: return target
				
				if diff < min_diff:
					min_diff = diff
					closest = sum_
				elif (l==i+1) and (r==l+1): return closest
				
				if sum_ > target: r -= 1
				else: l += 1
		return closest