"""
Board Class
"""
from Marble import Marble
import drawing_helpers

class Board():
    """
    This class represents a game board in a Mastermind game.
    Used for the scoreboard, game board and leaderboard.

    The board class divides each board into a grid based on the number of
    rows and columns. The x,y coordinate of each cell in this invisible grid
    is stored in the board class and used to help draw the board,
    place marbles, pegs, buttons etc.

    Attributes:
        border_thickness (int): Thickness of the board's border.
        length (int): The length of the board, adjusted for border thickness.
        height (int): The height of the board, adjusted for border thickness.
        center (tuple): The (x, y) coordinates of the board's center.
        color (str): The color of board borders.
        num_rows (int): Number of rows in the board.
        num_columns (int): Number of columns in the board.

        cell_positions (list): List of positions for each cell, each position
            is a tuple (x, y). The list of cell positions is nested so that any
            cell in the grid can be accessesed by indexing [row][column]

        marbles (list): A list to store marble objects.
        pegs (list): A list to store peg objects.
        buttons (list): A list to store button objects.

    Methods:
        draw_board(): Draws the board on the screen.
        add_cells(): Populates cell_positions list with coordinates for each
            cell.
        get_position(row, column): Returns the (x, y) coordinates of
            the cell in specficic row,column. eg. row 5, column 6
        draw_marble(row, column, marble_size, empty, marble_color):
            Draws a marble  on the board in specific row, column.
            Marble size and color determined by parameters. "Empty" parameter
            is a boolean. If true, empty marble is drawn, else a colored
            marble is drawn
    """
    def __init__(self, length, height, center,
                 color, num_rows, num_columns):

        self.border_thickness = 8
        self.length = length - self.border_thickness * 2
        self.height = height - self.border_thickness * 2
        self.center = center
        self.color = color

        self.num_rows = num_rows
        self.num_columns = num_columns

        self.cell_positions = []
        self.add_cells()

        self.marbles = []
        self.pegs = []
        self.buttons = []

    def draw_board(self):
        drawing_helpers.draw_rectangle(self.center[0],self.center[1], self.color, self.length, self.height, self.border_thickness)

    def add_cells(self):
        row_height = self.height / self.num_rows
        column_length = self.length / self.num_columns

        top_left_x = self.center[0] - self.length/2 + column_length/2
        top_left_y = self.center[1] + self.height/2 - row_height/2

        for row in range(self.num_rows):
            cells = []
            position_y = top_left_y - row * row_height
            for column in range(self.num_columns):
                position_x = top_left_x + column * column_length
                cells.append([position_x, position_y])
            # appends row of cells to board
            self.cell_positions.append(cells)
            cells = []

    def get_position(self, row, column):
        return self.cell_positions[row][column]

    def draw_marble(self, row, column, marble_size, empty, marble_color):
        center = self.cell_positions[row][column]
        new_marble = Marble(center, marble_color)
        if empty:
            new_marble.draw_empty()
        else:
            new_marble.draw()
        return new_marble
