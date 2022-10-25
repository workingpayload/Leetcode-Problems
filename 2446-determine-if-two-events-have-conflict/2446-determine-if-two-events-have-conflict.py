class Solution:
    def haveConflict(self, e1, e2):
        return e1[0] <= e2[1] and e2[0] <= e1[1]