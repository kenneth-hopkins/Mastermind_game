"""
Kenneth Hopkins
board_helpers
"""
import random
import copy
import board_properties as b

# randomizes the secret code
def get_code(colors):
    """
    Takes in a list of strings and randomizes the list.

    Parameters:
        colors(list of strings): Colors available for secret code

    returns:
        randomized list of colors to be used as secret code
    """
    color_copy = copy.deepcopy(colors)
    secret_code = []

    for i in range(4):
        color = random.choice(color_copy)
        secret_code.append(color)
        color_copy.remove(color)

    return secret_code

def divide_position(Board, center):
    """
    divides a board cell into 4 equally small squares and returns positions of these squares

    parameters:
        center (int) - the x,y coordinates of the center of a cell in a board

    returns:
        a tuple of 4 (x,y) positions.
    """
    length = b.BOARD_LENGTH / b.MAIN_BOARD_COLUMNS / 4
    height = b.BOARD_HEIGHT / b.MAIN_BOARD_ROWS / 4

    center_1 = (center[0]-length, center[1] + height )
    center_2 = (center[0]+length, center[1] + height )
    center_3 = (center[0]-length, center[1] - height )
    center_4 = (center[0]+length, center[1] - height )
    return (center_1, center_2, center_3, center_4)

def verify_high_score(score, file):
    """
    Checks if the current score qualifies as a high score by comparing
    it to scores in leaderboard file. if no file exists, you are the first high
    score

    parameters:
        score (int): The current score to verify.
        file (str): The file name of the leaderboard.

    Returns:
        bool: True if the current score is a high score, False otherwise.
    """
    high_scores = []
    try:
        with open(file, mode = 'r') as leaderboard_file:
            for line in leaderboard_file:
                score, name = line.split(" : ")
                score = int(score)
                high_scores.append(score)

        if score <= min(high_scores):
            return True

        else:
            return False

    except FileNotFoundError:
        return True
