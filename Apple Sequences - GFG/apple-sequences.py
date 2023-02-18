#User function Template for python3

class Solution:
    def appleSequences(self, n, m, arr):
        res = count = l = r = 0
        
        while r < n:
            if arr[r] == 'O': count += 1
            
            while l < n and count > m:
                if arr[l] == 'O': count -= 1
                l += 1 
                
            res = max(res, r - l + 1)
            
            r += 1
            
        return res 
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        temp = input().split()
        N = int(temp[0])
        M = int(temp[1])
        arr = input()

        ob = Solution()
        print(ob.appleSequences(N, M, arr))

# } Driver Code Ends