class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while(len(stones)>1):
            p = max(stones)
            pi= stones.index(p)
            stones.pop(pi)
            q = max(stones)
            qi = stones.index(q)
            stones.pop(qi)
            stones.append(p-q)
        return stones[0]    
            
        