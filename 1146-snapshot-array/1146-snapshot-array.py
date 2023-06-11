class SnapshotArray:
    def __init__(self, length: int):
        self.array = [[(0, 0)] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.array[index].append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        history = self.array[index]
        left, right = 0, len(history) - 1

        while left <= right:
            mid = (left + right) // 2
            if history[mid][0] <= snap_id:
                left = mid + 1
            else:
                right = mid - 1

        return history[right][1]