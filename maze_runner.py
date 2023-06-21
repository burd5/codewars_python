# Maze Runner - Codewars 6kyu

"""
You will be given a 2D array of the maze and an array of directions. Your task is to follow the directions given. If you reach the end point before all your moves have gone, you should return Finish. If you hit any walls or go outside the maze border, you should return Dead. If you find yourself still in the maze after using all the moves, you should return Lost.
The Maze array will look like

maze = [[1,1,1,1,1,1,1],
        [1,0,0,0,0,0,3],
        [1,0,1,0,1,0,1],
        [0,0,1,0,0,0,1],
        [1,0,1,0,1,0,1],
        [1,0,0,0,0,0,1],
        [1,2,1,0,1,0,1]]
..with the following key

      0 = Safe place to walk
      1 = Wall
      2 = Start Point
      3 = Finish Point
  direction = ["N","N","N","N","N","E","E","E","E","E"] == "Finish"
Rules
1. The Maze array will always be square i.e. N x N but its size and content will alter from test to test.

2. The start and finish positions will change for the final tests.

3. The directions array will always be in upper case and will be in the format of N = North, E = East, W = West and S = South.

4. If you reach the end point before all your moves have gone, you should return Finish.

5. If you hit any walls or go outside the maze border, you should return Dead.

6. If you find yourself still in the maze after using all the moves, you should return Lost.

"""

def maze_runner(maze, directions):
    n = len(maze)
    
    # find start point
    for i in range(n):
        if 2 in maze[i]:
            row = i
            col = maze[row].index(2)
            break
    
    # follow directions
    for step in directions:
        if   step == "N": row -= 1
        elif step == "S": row += 1
        elif step == "E": col += 1
        elif step == "W": col -= 1
        
        # check the result
        if row < 0 or col < 0 or row == n or col == n or maze[row][col] == 1:
            return "Dead"
        elif maze[row][col] == 3:
            return "Finish"
    
    return "Lost"