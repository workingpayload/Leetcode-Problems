class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for i in range(len(edges)):
            u, v = edges[i]
            prob = succProb[i]
            graph[u].append((v, prob))
            graph[v].append((u, prob))

        maxProb = [0.0] * n
        maxProb[start] = 1.0

        pq = [(-1.0, start)]
        heapq.heapify(pq)
        while pq:
            currProb, currNode = heapq.heappop(pq)
            currProb = -currProb

            if currNode == end:
                return currProb

            for nextNode, nextProb in graph[currNode]:
                nextProb *= currProb

                if nextProb > maxProb[nextNode]:
                    maxProb[nextNode] = nextProb
                    heapq.heappush(pq, (-nextProb, nextNode))

        return 0.0