from collections import deque
from typing import List

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        # Get the number of rows and columns in the land grid
        rows, cols = len(land), len(land[0]) 
        # List to store the coordinates of farmland groups
        farmland_groups = []
        # Queue for BFS traversal
        queue = deque()
        # Possible movements from each cell (up, right, down, left)
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

        # Iterate through each cell in the grid
        for row in range(rows):
            for col in range(cols):
                # Check if the current cell has a crop
                if land[row][col] == 1:
                    # Initialize BFS with the current cell
                    queue.append((row, col))
                    # Mark the current cell as visited
                    land[row][col] = 0
                    # Initialize coordinates of the current farmland group
                    farmland_coords = [row, col, -1, -1]
                    # Initialize variables to track the maximum row and column indices
                    max_row, max_col = row, col
                    # Perform BFS traversal
                    while queue:
                        r, c = queue.popleft()
                        # Update maximum row and column indices
                        max_row, max_col = max(max_row, r), max(max_col, c)
                        # Explore neighboring cells
                        for dr, dc in directions:
                            new_r, new_c = r + dr, c + dc
                            # Check if the neighboring cell is within the grid and contains a crop
                            if 0 <= new_r < rows and 0 <= new_c < cols and land[new_r][new_c] == 1:
                                # Mark the neighboring cell as visited
                                land[new_r][new_c] = 0
                                # Add the neighboring cell to the queue for further exploration
                                queue.append((new_r, new_c))
                    # Update the coordinates of the current farmland group with maximum row and column indices
                    farmland_coords[2], farmland_coords[3] = max_row, max_col
                    # Add the coordinates of the current farmland group to the list of farmland groups
                    farmland_groups.append(farmland_coords)
        # Return the list of coordinates of all identified farmland groups
        return farmland_groups
