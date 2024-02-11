# 1463. Cherry Pickup II

# Hint
# You are given a rows x cols matrix grid representing a field of cherries where grid[i][j] represents the number of cherries that you can collect from the (i, j) cell.

# You have two robots that can collect cherries for you:

# Robot #1 is located at the top-left corner (0, 0), and
# Robot #2 is located at the top-right corner (0, cols - 1).
# Return the maximum number of cherries collection using both robots by following the rules below:

# From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
# When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.
# When both robots stay in the same cell, only one takes the cherries.
# Both robots cannot move outside of the grid at any moment.
# Both robots should reach the bottom row in grid.


def cherryPickup(grid):
    rows, cols = len(grid), len(grid[0])
    
    # Initialize dp array with -1
    dp = [[[-1] * cols for _ in range(cols)] for _ in range(rows)]
    
    def dfs(row, col1, col2):
        # Base case: if out of bounds or already visited
        if row == rows or col1 < 0 or col1 >= cols or col2 < 0 or col2 >= cols:
            return 0
        
        # If already calculated, return the result
        if dp[row][col1][col2] != -1:
            return dp[row][col1][col2]
        
        # Current cell cherries
        cherries = grid[row][col1] + (grid[row][col2] if col1 != col2 else 0)
        
        # Maximum cherries from three possible moves
        max_cherries = 0
        for d1 in [-1, 0, 1]:
            for d2 in [-1, 0, 1]:
                max_cherries = max(max_cherries, dfs(row + 1, col1 + d1, col2 + d2))
        
        # Update dp array
        dp[row][col1][col2] = cherries + max_cherries
        return dp[row][col1][col2]
    
    return dfs(0, 0, cols - 1)

# Test case
grid = [[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]
print(cherryPickup(grid))  # Output: 24
