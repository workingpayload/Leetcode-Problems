class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr[:])):
            if arr[i]!=0:
                if (arr[i]*2) in arr:
                    return True
            else:
                if arr.count(0) >1:
                    return True
                
        return False    