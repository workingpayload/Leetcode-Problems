class Solution:
    def updateMatrix(self, matrix):
        if not matrix:
            return matrix
        
        rows, cols = len(matrix), len(matrix[0])
        distances = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        queue = deque()
        
        # Enqueue all 0 cells and set their distances to 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    distances[i][j] = 0
                    queue.append((i, j))
        
        # Define possible directions to move (up, down, left, right)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Perform BFS to calculate distances
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    if distances[nx][ny] > distances[x][y] + 1:
                        distances[nx][ny] = distances[x][y] + 1
                        queue.append((nx, ny))
        
        return distances
