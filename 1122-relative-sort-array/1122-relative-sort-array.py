class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        rem = list(set(arr1) - set(arr2))
        ans = []
        for i in rem:
            for _ in range(arr1.count(i)):
                ans.append(i)
        ans.sort()
        res = []
        for i in arr2:
            for _ in range(arr1.count(i)):
                res.append(i)
        res += ans
        return res