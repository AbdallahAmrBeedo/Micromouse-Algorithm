# Micromouse-Algorithm
An algorithm for micromouse competition simulated by a maze made on excel.
The idea of the algorithm is iterative flood-fill algorithm that defines for each cell the distance to the destination. The difference is our algorithm start the flood-fill from the start cell and then return to it and inverse the array values to get a nearly map of the maze. 
# 1- Motion:
An array represents the maze, the location represents where the robot stands, the set is how the robot stands either it’s facing up, down, left or right. By making a list of the cells surrounding the robot cell and giving the set 4 values from 1 to 4 with each one represents where the robot forward direction is. The next move (decided by the algorithm in next part) is either right “r” or left “l” or forward “f” or dead end “d” each one changes the position x and y and the robot set.
# 2-Maze Solving:
- Maze Exploring:
The initial set for the maze with all cells set to -1 except for the 4 middle cells is set to 0 as they are the destination. As the robot moves it leave a trace behind it by counting number of cells walked from the initial cell. 
By reaching a dead end the cell value = -5 as it’s a not preferred cell. if the next cell has a cell value less than the count reached the count is reset to the cell value to continue counting from it. 
The robot favors the cells with values -1 (undiscovered cell with no trace), if 2 available cells have the value -1, it calculates the shortest to the destination and if they are equal, it randomizes the move. With no available cells with value -1, the robot selects the max value from the given possibilities to reach the end of the trace and start discovering, however, this will lead for loop if no -1 cells have shown, so after it visit the cell 4 times it starts to increase the cell value and search for the minimum value to escape the loop. 
- Back to Start:
The rules are simple, return to the start with no human interruption, a bonus time is given. And also the time of the return is not calculated, so we should try to return autonomously, at least we can find a new path that shorten the distance. 
Same is applied, a cell with -1 is preferred, but the reverse for cells with no -1 cell, the cell with minimum value is preferred to find the end of the trace as the counter this time is decreasing till it reaches the start cell. the cells visited more than 5 times is multiplied and the max cell is reached. 
If the counter is decreased it has 2 scenarios, good one it reaches the end with value more than 1 so the new path is shorter than the other, bad one that the counter is 0 and the start cell is not reached, so the robot stops counting and find the shortest way to the 0,0 cell and start the run. 
Every time it returns the available cells, it sees the distance to 0,0 and if the distance = 10 or less it prefers this short way rather than discovering new cells.
Walking out from this phase we have a nearly reverse flood fill for the maze array, so we have to inverse it and delete the ways that leads to dead ends to avoid it in the run.
- Run:
	We need to do 2 things before deciding the path and start to run:
	- Inverse: by subtracting the value of the middle cells from all other cells except dead ends (-5) and loop cells (300) it gives them a value of -10 to make the robot avoid choosing these cells. At the end we get a flood fill made by the path taken by the robot.
	- Path making: perfect cells that we need are cells that has entrance and exit so it has 2 neighbor cells one with value less than its value and the other with value more than its value. The idea is a loop that take each cell and see its neighbors, if there is no cell with less value or large value, the value of the cell will be set to -10. Recruiting the method many times will eliminate the cells that leads to a dead end and leave the cells that have a clear path between the start cell and destination. Start cell and destination are excepted from this method to avoid eliminating the whole array. 

After getting the array with nearly no cells leading to a dead end, the robot just sees the minimum cell available and take the run to the destination. Saving the maze after run to try again with higher speed. 

