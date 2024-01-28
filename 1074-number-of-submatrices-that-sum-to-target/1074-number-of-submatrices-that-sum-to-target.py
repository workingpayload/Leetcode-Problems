class Solution:

  def numSubmatrixSumTarget(self, M: List[List[int]], t: int) -> int:

    res,rs = 0,[list(accumulate(r,operator.add))+[0] for r in M]

    for y1,y2 in combinations(range(-1,len(M[0])),2):

      su,d = 0,{0:1}

      for r in rs:

        su += r[y2] - r[y1]

        res += d.get(su-t,0)

        d[su] = d.get(su,0) + 1

    return res
    
        