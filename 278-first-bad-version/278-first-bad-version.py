# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        isbad = isBadVersion(l)
        while not(isbad):
            if isBadVersion((l+n)//2):
                n = (l+n)//2 - 1
            else:
                l = (l+n)//2 + 1
                isbad = isBadVersion(l)
        return l        
                            
        
        