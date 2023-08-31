class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        range_stack = []
        covered = 0
        for idx, range_ in enumerate(ranges):
            if range_stack and idx+range_ < range_stack[-1][1]:
                continue
            while range_stack and range_stack[-1][0] >= idx - range_:
                popped_range = range_stack.pop()
                covered -= popped_range[1] - popped_range[0]
            if not range_stack or range_stack[-1][1] < idx+range_:
                if not range_stack:
                    left_point = max(idx-range_, 0)
                else:
                    left_point = max([idx-range_, 0, range_stack[-1][1]])
                new_coverage = min(idx+range_, n)-left_point
                range_stack.append([left_point, min(idx+range_, n)])
                covered += new_coverage
            if covered >= n:
                return len(range_stack)
        return -1