from turtle import *


def move_left(x):
    """
    FUNCTION: move_left
        moves turtle left by x units

    """
    setheading(180)
    forward(x)

def move_right(x):
    """
    FUNCTION: move_right
        moves turtle right by x units
    """
    setheading(0)
    forward(x)

def move_up(x):
    """
    FUNCTION: move_up
        moves turtle up by x units
    """
    setheading(90)
    forward(x)


def move_down(x):
    """
    FUNCTION: move_down
        moves turtle down by x units
    """
    setheading(270)
    forward(x)

def draw_triangle(length, position, shape_color):
    """
    FUNCTION: draw_triangle
        draws shaded equilateral triangle of length x
    PARAMETERS:
        length - length of the triangle
        position - int - starting (x,y) coordinate of the center of the triangle
        shape_color - string - the desired color of the triangle

    RETURN:
        none
    """
    up()
    speed(0)
    pensize(1)
    setposition(position[0],position[1])

    move_left(length/2)
    color(shape_color)
    begin_fill()
    down()
    move_up(length/2)
    setheading(315)
    forward(length)
    setheading(225)
    forward(length)
    move_up(length/2)
    hideturtle()
    end_fill()


def draw_rectangle(x_coord,y_coord, shape_color, length, height, pen_size):
    """
    FUNCTION: draw_square
        draws unshaded square of length x
    PARAMETERS:
        x_coord - int - starting x coordinate of the center of the square
        y_coord - int - starting y coordinate of the center of the square
        shape_color - string - the desired color of the square
        length - int - the length of the square to be drawn
    RETURN:
        none
    """

    #lift pen
    up()
    speed(0)
    pensize(pen_size)
    setposition(x_coord,y_coord)

    #moves turtle so that (x,y) is at center of square
    move_left(length/2)
    move_up(height/2)

    color(shape_color)

    #draws each side of square

    down()

    move_down(height)
    move_right(length)
    move_up(height)
    move_left(length)

    up()

def draw_grid(Board):
    """
    FUNCTION: draw_grid
        draws grid in board object to help with visualization. Used for testing
    PARAMETERS:
        Board (Board) - Board object where grids will be drawn
    RETURN:
        none
    """
    row_height = Board.height / Board.num_rows
    column_length = Board.length / Board.num_columns

    top_left_x = Board.center[0] - Board.length/2
    top_left_y = Board.center[1] + Board.height/2

    up()
    speed(0)
    pensize(1)
    for column in range(Board.num_columns - 1):
        setposition(top_left_x, top_left_y)
        move_right(column_length * (column + 1))
        down()
        move_down(Board.height)
        up()

    for row in range(Board.num_rows - 1):
        setposition(top_left_x, top_left_y)
        move_down(row_height * (row + 1))
        down()
        move_right(Board.length)
        up()
