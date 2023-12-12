"""
CS5001
mastermind_game.py
Kenneth Hopkins
"""
import turtle
import drawing_helpers
from Marble import Marble
from Button import Button
from Board import Board
import board_properties as b
import board_helpers
import datetime


COLORS = ["red", "blue", "green", "yellow", "purple", "black"]
game = None


class Game():
    """
    Manages the game of Mastermind.
    This class initializes the game, handles clicks from the user, user input,
    outputs messages to user and stores all the game data as the round progresses.

    Attributes:
        round (int): The current round of the game.
        secret_code (list): The secret code that the player is trying to guess.
        click_counter (int): A counter for tracking the number marbles clicked.
            no more than 4 marbles can be selected per round
        player_name (str): The name of the player.
        screen (turtle.Screen): The main screen where all the drawing happens
        main_board, guess_board, score_board (Board): Board objects
            representing boards in the game.
        pegs (list): List of pegs used to help player guess secret code.
        marbles (list): List of marbles. The scoreboard has clickable marbles
            for players to input their color guesses. The main board marbles
            are non-clickable and only display the player's guesses.
        buttons (list): List of buttons used in the game.
        game_over (bool): boolean indicating whether the game is over.

    Methods:
        increment_click_counter(): Increments click counter.
        get_click_counter(): Returns the value of the click counter.
        reset_click_counter(): Resets the click counter to zero.
        draw_boards(): Draws the main, guess, and score boards.
        create_marbles(): Creates and draws marbles on the main board.
        create_pegs(): Creates and draws pegs on the main board.
        create_buttons(): Creates and draws clickable buttons.
        update_peg_colors(user_guess): Updates peg colors based on user's guess
        check_win_condition(user_guess): Checks if the user guessed secret code
        print_message(image): Displays message on screen using a gif image
        end_game(): Marks game as over by triggering game_over flag.
        reveal_secret_code(): Reveals secret code to player using input box
        draw_arrow(): Draws arrow indicating the current round.
        advance_round(): Advance the game to the next round. updates variables.
        display_leaderboard(file): Displays leaderboard from a  file.
    """
    def __init__(self):
        self.round = 1
        self.secret_code = board_helpers.get_code(COLORS)
        self.click_counter = 0
        self.player_name = turtle.textinput("Enter Name:", "Please enter your name")
        self.screen = turtle.Screen()
        self.main_board, self.guess_board, self.score_board = get_boards()
        self.pegs = []
        self.marbles = []
        self.buttons = []
        self.game_over = False

    def increment_click_counter(self):
        self.click_counter += 1

    def get_click_counter(self):
        return self.click_counter

    def reset_click_counter(self):
        self.click_counter = 0

    # draws boards using draw_board method in Board Class
    def draw_boards(self):
        self.main_board.draw_board()
        self.guess_board.draw_board()
        self.score_board.draw_board()

    def create_marbles(self):
        empty = True
        # draws empty marbles on main_board starting at row 1, column 1
        main_starting_cell = (1,1)
        for row in range(b.NUM_MARBLE_ROWS):
            for column in range(b.NUM_MARBLE_COLUMNS):
                new_marble = self.main_board.draw_marble(row + main_starting_cell[0], column + main_starting_cell[1], 15, empty, "black" )
                self.marbles.append(new_marble)

    def create_pegs(self):
        empty = True
        # draws empty pegs in the 6th column of each row
        for row in range(b.NUM_MARBLE_ROWS):
            column = 5
            current_position = self.main_board.get_position(row + 1, column)
            centers = board_helpers.divide_position(self.main_board, current_position)
            for center in centers:
                marble_1 = Marble((center[0],center[1]),"black", 4)
                marble_1.draw_empty()
                self.pegs.append(marble_1)

    def create_buttons(self):

        # first 6 buttons resemble clickable colored marbles
        empty = False
        starting_row = 1
        size = 15
        for starting_column in range(6):
            color = COLORS[starting_column]
            marble_button = self.guess_board.draw_marble(starting_row, starting_column, size, empty, color)
            self.buttons.append(marble_button)

        # draws check button at row 1, column 6
        check_center = self.guess_board.get_position(1,6)
        check_length, check_height = 50, 50
        check_button = Button((check_center[0],check_center[1]),check_length, check_height, "checkbutton.gif")
        check_button.draw()
        self.buttons.append(check_button)

        # offsets position to make room for quit button's non-standard size
        QUIT_BUTTON_OFFSET = -10

        # draws xbutton at row 1, column 7.
        x_center = self.guess_board.get_position(1,7)
        x_length, x_height = 50, 50
        x_button = Button((x_center[0] + QUIT_BUTTON_OFFSET,x_center[1]),x_length, x_height, "xbutton.gif")
        x_button.draw()
        self.buttons.append(x_button)

        # draws quit button at row 1, column 8. moves 10 to the left to make room for larger quit button
        quit_center = self.guess_board.get_position(1,8)
        quit_length, quit_height = 70, 39
        quit_button = Button((quit_center[0] + QUIT_BUTTON_OFFSET,quit_center[1]),quit_length, quit_height, "quit.gif")
        quit_button.draw()
        self.buttons.append(quit_button)

    # fills in peg to let user know how correct their guess is
    def update_peg_colors(self, user_guess):
        peg_index = 0
        for index, color in enumerate(user_guess):
            if color == self.secret_code[index]:
                self.pegs[peg_index].set_color("black")
                self.pegs[peg_index].draw()
                peg_index += 1

            elif color in self.secret_code:
                self.pegs[peg_index].set_color("red")
                self.pegs[peg_index].draw()
                peg_index += 1

        # remove pegs from list at the end of each round
        for i in range(4):
            self.pegs.pop(0)

    # checks if user guessed the secret code
    def check_win_condition(self, user_guess):
        correct_guesses = 0

        for index, color in enumerate(user_guess):
            if color == self.secret_code[index]:
                correct_guesses += 1

        if correct_guesses == 4:
            return True

    # prints a gif message to screen (error, win, lose, quit etc)
    def print_message(self, image):
        screen = turtle.Screen()
        screen.addshape(image)
        turtle.penup()
        turtle.setposition(0,0)
        turtle.shape(image)
        turtle.stamp()

    def end_game(self):
        self.game_over = True

    def reveal_secret_code(self):
        code_string = " ".join(self.secret_code)
        turtle.textinput("Secret Code", f"the Secret Code was: {code_string}")

    def draw_arrow(self):
        center = self.main_board.get_position(self.round, 0)
        drawing_helpers.draw_triangle(15, center, "blue")

    def advance_round(self):
        self.click_counter = 0
        self.round += 1
        self.draw_arrow()

    def display_leaderboard(self, file):
        try:
            i = 1
            with open(file, mode = 'r') as leaderboard_file:
                for line in leaderboard_file:
                    turtle.up()
                    turtle.setposition(self.score_board.get_position(i,0))
                    turtle.write(f"{line}",font = ("Verdana", 20, "normal"))
                    i += 1


        except FileNotFoundError:
            game.print_message("leader_board_error.gif")



# creates and returns board objects with the properties in the board properties file
def get_boards():

    main_board = Board(b.BOARD_LENGTH,b.BOARD_HEIGHT,(b.MAIN_BOARD_X,b.MAIN_BOARD_Y),"black", b.MAIN_BOARD_ROWS ,b.MAIN_BOARD_COLUMNS)
    guess_board = Board(b.GUESS_BOARD_LENGTH,b.GUESS_BOARD_HEIGHT,(b.GUESS_BOARD_X, b.GUESS_BOARD_Y),"black",b.GUESS_BOARD_ROWS, b.GUESS_BOARD_COLUMN)
    score_board = Board(b.SCORE_BOARD_LENGTH,b.SCORE_BOARD_HEIGHT,(b.SCORE_BOARD_X,b.SCORE_BOARD_Y),"blue",b.SCORE_BOARD_ROWS,b.SCORE_BOARD_COLUMNS)
    return main_board, guess_board, score_board

def update_leaderboard(file = "leaderboard.txt"):
    """
    Updates the leaderboard file.

    Reads current high scores from the file, adds the current player's score,
    sorts the high scores and only keeps top 10 in leaderboard file. If the file does not exist, it creates a
    new one.

    Parameters:
        file (str, optional): The file name of leaderboard file.

    Returns:
        None
    """
    high_scores = []

    try:
        with open(file, mode = 'r') as leaderboard_file:
            for line in leaderboard_file:
                score, name = line.split(" : ")
                name = name.strip(" \n")
                score = int(score)
                high_scores.append([score,name])

        high_scores.append([game.round, game.player_name])
        high_scores.sort(key = lambda x: x[0])

        with open(file, mode = 'w') as leaderboard_file:
            for i in range(min(10,len(high_scores))):
                leaderboard_file.write(f"{high_scores[i][0]} " +
                                       f": {high_scores[i][1]}\n")
        if len(high_scores) > 10:
            turtle.textinput("Congratulations!",
                "New High Score! Play again to see your name on the leaderboard!")

    except FileNotFoundError:
        with open(file, mode = 'w') as leaderboard_file:
            leaderboard_file.write(f"{game.round} " + f": {game.player_name}\n")
        game.print_message("leader_board_error.gif")
        log_error(FileNotFoundError)

# writes error to error log file
def log_error(error,file = "mastermind_errors.err.txt"):
    """
    Records the error message, its type, and time of error.
    Adds this information to an error log file.

    Parameters:
        error (Exception): The error to be logged.
        file (str): File name of where to write error log.

    Returns:
        None
    """
    time = datetime.datetime.now()
    time_string = time.strftime("%d/%m/%Y %H:%M:%S")
    with open(file, mode = 'a') as error_log:
        error_log.write(f"Error Message: {error} \t Error Type: {type(error)}\t Time: {time} \n")


def click(x,y):
    """
    Handles mouse clicks on screen. This function takes the x,y coordinates
    from a mouse click and does several things depending where the player
    clicked. It manages the marble selection, checking
    guesses, resetting the current guess, and quitting the game.

    The function handles the following:
    - handles guesses if player clicks on marble button
    - Checking the guess when the 'check' button is clicked, updating peg colors,
      and checking for win condition.
    - Clearing the current guess when the 'x' button is clicked.
    - Ending the game when the 'quit' button is clicked.

    Parameters:
        x (int): The x coordinate of mouse click.
        y (int): The y- oordinate of  mouse click.

    Returns:
        None
    """
    check_button = game.buttons[6]
    x_button = game.buttons[7]
    quit_button = game.buttons[8]

    if game.game_over == False:
        # first 6 buttons resemble marbles
        for marble_button in game.buttons[:6]:
            if marble_button.clicked_in_region(x,y) and \
                game.get_click_counter() <= 3 and not marble_button.get_empty_status():

                    marble_button.set_empty_status(True)
                    marble_button.draw_empty()
                    # changes marble color based on click_counter
                    current_marble = game.marbles[game.click_counter]
                    current_marble.set_color(marble_button.get_color())
                    current_marble.draw()

                    game.click_counter += 1

        # check button
        if check_button.clicked_in_region(x,y) and game.get_click_counter() > 3:
            user_guess = []
            for i in range(4):
                color = game.marbles.pop(0).get_color()
                user_guess.append(color)

            for marble_button in game.buttons[:6]:
                marble_button.draw()

            game.update_peg_colors(user_guess)

            if game.check_win_condition(user_guess):
                update_leaderboard()
                game.print_message("winner.gif")
                game.end_game()
                game.reveal_secret_code()

            elif game.round == 10:
                game.print_message("Lose.gif")
                game.reveal_secret_code()
                game.end_game()

            game.advance_round()


        # xbutton
        if x_button.clicked_in_region(x,y):
            for marble_button in game.buttons[:6]:
                marble_button.set_empty_status(False)
                marble_button.draw()

            for i in range(4):
                game.marbles[i].draw_empty()
            game.reset_click_counter()

        # quit button
        if quit_button.clicked_in_region(x,y):
            game.print_message("quitmsg.gif")
            game.end_game()
            game.reveal_secret_code()

def main():
    global game
    try:
        game = Game()
        game.screen.setup(b.SCREEN_LENGTH, b.SCREEN_HEIGHT)
        game.draw_boards()
        game.draw_arrow()
        game.create_marbles()
        game.create_pegs()
        game.create_buttons()
        game.display_leaderboard("leaderboard.txt")
        game.screen.onclick(click)

    except Exception as error:
        log_error(error)


    turtle.done()


main()
