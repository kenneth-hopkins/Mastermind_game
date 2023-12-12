"""
Button Class
"""
import turtle

class Button():
    """
    Represents a clickable button in the mastermind game. Used for the
    check button, quit button and x button

    Attributes:
        center (tuple): The (x, y) coordinates of the button's center.
        length (int): The length of the button.
        height (int): The height of the button.
        image (str): The name of the image used for the button's appearance.

    Methods:
        draw(): draws the button on the sceen using turtle functions.
        clicked_in_region(x, y): Determines looks at a pair of
            x,y coordinates and determins if button was clicked.
        """
    def __init__(self, center, length, height, image):
        self.center = center
        self.length = length
        self.height = height
        self.image = image


    def draw(self):
        screen = turtle.Screen()
        screen.addshape(self.image)
        button = turtle.Turtle()
        button.penup()
        button.setposition(self.center[0],self.center[1])
        button.shape(self.image)
        button.stamp()


    def clicked_in_region(self, x, y):
        if abs(x - self.center[0]) <= self.length/2 and \
           abs(y - self.center[1]) <= self.height/2:
            return True
        return False
