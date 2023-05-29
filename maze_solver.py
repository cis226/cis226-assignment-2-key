"""Maze Solver Module"""

# David Barnes
# CIS 226
# 05-28-23

# System imports
import time

# First-party imports
from colors import Style


class MazeSolver:
    """This class is used for solving a 2d list maze.

    You might want to add other methods to help you out.
    A print maze method would be very useful, and probably necessary to print the solution.
    If you are real ambitious, you could make a separate class to handle that."""

    def __init__(self, clear_screen=False):
        """Constructor for MazeSolver"""

        # NOTE: Though not required, you may wan to define some class level
        # variables here that you are able to access and set anywhere during
        # recursion. This is why the init constructor is defined here for you.

        # Class var to hold maze.
        self._maze = None
        # Class var to know whether the exit has been found
        self._found_exit = False
        # Create Width and Length for easier access in the program.
        self.width = 0
        self.length = 0
        # Set whether the screen should be cleared on each print.
        self._clear_screen = clear_screen

    def solve_maze(self, maze, x_start, y_start):
        """This is the public method that will allow someone to use this class to solve the maze.
        Feel free to change the return type, or add more parameters if you like.
        But, it can be done exactly as it is here without adding anything other
        than code in the body."""

        if len(maze) < 1 or len(maze[0]) < 1:
            raise ValueError("Maze is not 2D. Can not solve.")

        # Assign the passed in maze to the class level var.
        self._maze = maze

        # Set the width and length of the maze based on the passed in maze
        self.width = len(self._maze)
        self.length = len(self._maze[0])

        # Re-initialize Found Exit to False
        self._found_exit = False

        # Print out the starting state of the maze
        self._print_maze(x_start, y_start)

        # Make the recursive call to solve the maze
        self._maze_traversal(x_start, y_start)

    def _maze_traversal(self, x, y):
        """This should be the recursive method that gets called to solve the maze.
        Feel free to have it return something if you would like. But, it can be
        done without having it return anything. Also feel free to change the
        signature to take in parameters that you might need.

        This is only a very small starting point.
        More than likely you will need to pass in at a minimum the current position
        in X and Y maze coordinates. EX: _maze_traversal(current_x, current_y)"""

        # Mark the position that we are at when the method is called with an X.
        self._maze[y][x] = "X"

        # Print out the maze.
        self._print_maze(x, y)

        # Call the class level method to check and see if we are standing on the
        # exit. If so, the found_exit flag needs to be flipped.
        self._check_for_exit(x, y)

        ######## Move Right ########
        # If we haven't found the exit, and the position to the right is a valid
        # move, (A period ".") we should move there with the recursive call.
        if not self._found_exit and self._maze[y][x + 1] == ".":
            # Make the recursive call to this same function setting the passed
            # in coordinates to the same value as the current plus on more in
            # the right direction.
            self._maze_traversal(x + 1, y)

            # Print out the maze if we have not found the exit
            if not self._found_exit:
                self._print_maze(x, y)

        ######## Move Down ########
        # Refer to the above comments for moving right.
        # Everything is the same except for the fact
        # that we are moving down instead of right.
        if not self._found_exit and self._maze[y + 1][x] == ".":
            self._maze_traversal(x, y + 1)
            if not self._found_exit:
                self._print_maze(x, y)

        ######## Move Left ########
        # Refer to the above comments for moving right.
        # Everything is the same except for the fact
        # that we are moving left instead of right.
        if not self._found_exit and self._maze[y][x - 1] == ".":
            self._maze_traversal(x - 1, y)
            if not self._found_exit:
                self._print_maze(x, y)

        ######## Move Up ########
        # Refer to the above comments for moving right.
        # Everything is the same except for the fact
        # that we are moving up instead of right.
        if not self._found_exit and self._maze[y - 1][x] == ".":
            self._maze_traversal(x, y - 1)
            if not self._found_exit:
                self._print_maze(x, y)

        # If we reached here, it is because either there was a dead end further
        # down from the recursive call, or, we found the exit and we are backing
        # out of all of the recursive calls. This will print O's along the valid
        # path, but since we have already printed the solved maze in the check
        # for the exit method, we don't officially need this check. We could
        # leave the putting down of O's without the decision.
        # By having this check though, we could print the maze in the check
        # for exit, or after it backs all the way out.
        if not self._found_exit:
            self._maze[y][x] = "O"

    def _check_for_exit(self, x, y):
        """Give an X and Y coordinate, check if it is the exit"""
        if x == 0 or x == self.width - 1 or y == 0 or y == self.length - 1:
            # Flip class level found exit flag
            self._found_exit = True
            # Print the final solved maze solution
            self._print_solved_maze()

    def _print_solved_maze(self):
        """Print the solved maze"""

        print()
        print("-------------")
        print("Maze Solution")
        print("-------------")

        self._print_maze()

        print()
        print("-------------")
        print()

    def _print_maze(self, x=None, y=None):
        """Prints out the maze to the console"""

        if self._clear_screen:
            time.sleep(0.25)
            Style.CLEAR  # pylint:disable=W0104

        for i in range(self.width):
            for j in range(self.length):
                # Check if current spot
                is_current_spot = i == y and j == x
                # Set console color based on current character.
                self.set_console_color(self._maze[i][j], is_current_spot)
                # Print out the current character
                print(self._maze[i][j], end="")
            # Print a blank line
            print()
        # Reset color to ensure it isn't accidentally used when it should not be.
        Style.RESET  # pylint:disable=W0104
        # Couple of blank lines for spacing.
        print()
        print(flush=True)

    def set_console_color(self, character, is_current_spot):
        """Set what console color to use based on character"""
        if is_current_spot:
            Style.BLUE  # pylint:disable=W0104
        elif character == "X":
            Style.GREEN  # pylint:disable=W0104
        elif character == "O":
            Style.RED  # pylint:disable=W0104
        elif character == ".":
            Style.YELLOW  # pylint:disable=W0104
        else:
            Style.RESET  # pylint:disable=W0104
