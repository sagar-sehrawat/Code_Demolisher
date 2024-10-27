#!/usr/bin/env python3

## This is Hakcer rank python exam Question

def is_dominant(grid, i, j, rows, cols):
    # Get the value of the current cell
    current_value = grid[i][j]

    # List of neighbor coordinates (top, bottom, left, right, diagonals)
    neighbors = [
        (i-1, j),   # Top
        (i+1, j),   # Bottom
        (i, j-1),   # Left
        (i, j+1),   # Right
        (i-1, j-1), # Top-left
        (i-1, j+1), # Top-right
        (i+1, j-1), # Bottom-left
        (i+1, j+1)  # Bottom-right
    ]

    # Check all valid neighbors
    for x, y in neighbors:
        if 0 <= x < rows and 0 <= y < cols:  # Check if the neighbor is within bounds
            if grid[x][y] >= current_value:  # If any neighbor is greater or equal, not dominant
                return False
    return True

# Function to count dominant cells
def numCells(grid):
    rows = len(grid)
    cols = len(grid[0])

    dominant_count = 0
    for i in range(rows):
        for j in range(cols):
            if is_dominant(grid, i, j, rows, cols):
                dominant_count += 1
    return dominant_count

if __name__ == '__main__':
    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    # Debugging output: print the grid
    print(grid)

    # Calculate and print the number of dominant cells
    result = numCells(grid)
    print(result)
