class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mp=defaultdict(list)
        for a,b in prerequisites:
            mp[a]+=[b]
        bl=[0]*numCourses
        def test(ind):
            nonlocal bl
            if bl[ind]==1:
                return True
            if bl[ind]==2:
                return False
            bl[ind]=1
            for i in mp[ind]:
                if test(i):
                    return True
            bl[ind]=2
            return False
        for a,b in prerequisites:
            if not bl[a]:
                if test(a):
                    return False

        return True