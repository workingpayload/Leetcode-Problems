class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:

        s = ""

        for i in num:
            s+=str(i)    

        res = int(s)+k

        li = []

        for i in str(res):
            li.append(int(i))

        return li        