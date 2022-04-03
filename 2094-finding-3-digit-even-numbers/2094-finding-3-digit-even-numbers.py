class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        arr = []
        
        per = set(permutations(digits,3))
        
        for i in list(per):
            if i[0]!=0:
                number = ""
                for j in i:
                    number+=str(j)
                if not int(number)%2:
                    arr.append(int(number))
        arr.sort()
        return arr
        