"""Program code"""

# David Barnes
# CIS 226
# 05-28-23

# First-party imports
from maze_solver import MazeSolver


def main(*args):
    """Method to run program"""

    # Starting Coordinates
    X_START = 1
    Y_START = 1

    # The first maze that needs to be solved.
    # NOTE: You may want to make a smaller version to test and debug with.
    # You don't have to, but it might make your life easier.
    maze1 = [
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", ".", ".", ".", "#", ".", ".", ".", ".", ".", ".", "#"],
        ["#", ".", "#", ".", "#", ".", "#", "#", "#", "#", ".", "#"],
        ["#", "#", "#", ".", "#", ".", ".", ".", ".", "#", ".", "#"],
        ["#", ".", ".", ".", ".", "#", "#", "#", ".", "#", ".", "."],
        ["#", "#", "#", "#", ".", "#", ".", "#", ".", "#", ".", "#"],
        ["#", ".", ".", "#", ".", "#", ".", "#", ".", "#", ".", "#"],
        ["#", "#", ".", "#", ".", "#", ".", "#", ".", "#", ".", "#"],
        ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#", ".", "#"],
        ["#", "#", "#", "#", "#", "#", ".", "#", "#", "#", ".", "#"],
        ["#", ".", ".", ".", ".", ".", ".", "#", ".", ".", ".", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ]

    # Create new instance of a MazeSolver
    maze_solver = MazeSolver()
    # If you would like to see the screen clear on each step,
    # use the following line in place of the above one.
    # maze_solver = MazeSolver(clear_screen=True)

    # Create the second maze by transposing the first maze
    maze2 = transpose_maze(maze1)

    # Solve the original maze
    maze_solver.solve_maze(maze1, X_START, Y_START)

    # Break between solves
    print("Press enter to solve the 2nd maze")
    input()

    # Solve the transposed maze
    maze_solver.solve_maze(maze2, X_START, Y_START)


def transpose_maze(maze_to_transpose):
    """This method will take in a 2d list (list of lists) and return a new
    2d list maze that is flipped along the diagonal, or in mathematical terms,
    transposed.

    ie. If the array looks like:
    1, 2, 3
    4, 5, 6
    7, 8, 9
    Then the returned result will be:
    1, 4, 7
    2, 5, 8
    3, 6, 9

    The current return statement is just a placeholder so the program doesn't
    contain any syntax errors. You need to replace this with the work you need
    to do for actually transposing the maze.

    It is important that you make a new 2d list and copy each element from the
    original to the new transposed one. Failure to do so may lead you to only
    be able to solve the transposed one.
    """
    if len(maze_to_transpose) < 1 or len(maze_to_transpose[0]) < 1:
        raise ValueError("Maze is not 2D. Can not transpose.")

    # Get width and length
    width = len(maze_to_transpose)
    length = len(maze_to_transpose[0])

    # Init a transposed maze filled with the letter "e"
    transposed_maze = [["e"] * width for i in range(length)]

    # Do the actual transpose
    for i in range(width):
        for j in range(length):
            transposed_maze[j][i] = maze_to_transpose[i][j]

    return transposed_maze
