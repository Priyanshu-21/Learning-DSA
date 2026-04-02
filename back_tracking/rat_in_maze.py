class Solution:
    def __init__(self):
        self.choices = {
            "D": [1, 0],
            "L": [0, -1],
            "R": [0, 1],
            "U": [-1, 0],
        }

    def ratInMaze(self, maze):
        # BackTracking approach 
        path = ""
        x, y = 0, 0 # Current position in maze 
        results = []

        # Base case: 
        if (maze[x][y] == 0):
            return results

        self.solve(maze, x, y, path, results)
        
        # Return in lexicographical order
        return results
    
    def solve(self, maze, x, y, path, results):

        # Base condition:
        if (x == len(maze) - 1 and y == len(maze) - 1):
            # Rat is now out of maze
            results.append(path) 
            return 
        
        # Mark position as visited 
        maze[x][y] = 0

        # Number of choices ('L', 'R', 'U', 'D')
        for choice, (dx, dy) in self.choices.items():
            new_x = x + dx
            new_y = y + dy 

            # controlled-recursion (out of bound, not_revisted, not_pass)
            if (0 <= new_x < len(maze)) and (0 <= new_y < len(maze)) and (maze[new_x][new_y] == 1):
                
                new_path = path + choice
                # Recursive call
                self.solve(maze, new_x, new_y, new_path, results)
        
        # BackTrack 
        maze[x][y] = 1


sol = Solution()
maze = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
print(sol.ratInMaze(maze))
