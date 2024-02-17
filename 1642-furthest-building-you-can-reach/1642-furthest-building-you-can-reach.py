class Solution:

    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        # prepare: use a min heap to store each difference(climb) between two contiguous buildings

        # strategy: use the ladders for the longest climbs and the bricks for the shortest climbs

        

        min_heap = []

        n = len(heights)

        

        for i in range(n-1):

            climb = heights[i+1] - heights[i]

            

            if climb <= 0:

                continue

            

            # we need to use a ladder or some bricks, always take the ladder at first

            if climb > 0:

                heapq.heappush(min_heap, climb)

            

            # ladders are all in used, find the current shortest climb to use bricks instead!

            if len(min_heap) > ladders:

                # find the current shortest climb to use bricks

                brick_need = heapq.heappop(min_heap)

                bricks -= brick_need

            

            if bricks < 0:

                return i

        

        return n-1
