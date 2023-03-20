class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not flowerbed:
            if n>1:
                return True
            else:
                return False
        if len(flowerbed)==1:
            if flowerbed[0]==0:
                n-=1  
        else:
            if flowerbed[0]==0 and flowerbed[1]==0:
                flowerbed[0]=1
                n-=1
            for i in range(1,len(flowerbed)-1):
                if flowerbed[i]==0:
                    if flowerbed[i-1]==0 and flowerbed[i+1]==0:
                        flowerbed[i]=1
                        n-=1
            if flowerbed[-1]==0 and flowerbed[-2]==0:
                flowerbed[-1]
                n-=1
        if n<1:
            return True
        else:
            return False
                    
        