"""
test_mastermind.py
"""
def test_guess(secret_code, user_guess):
    """
    Compares user guess to a secret code. It evaluates the guess and tells
    the number of correct colors in correct position, correct colors in wrong position
    and incorrect colors included in the guess.

    Parameters:
        secret_code (list of strings): The secret list of colors the player is trying to guess.
        user_guess (list of strings): A list of colors representing the user's guess

    Returns:
        None. It prints out the number of correct colors in correct position, correct colors in wrong position
        and incorrect colors in the user's guess.


    """

    correct_color_and_placement = []
    correct_color_wrong_placement = []
    wrong = []

    for index, color in enumerate(user_guess):
        if color.lower() == secret_code[index].lower():
            correct_color_and_placement.append(color)
        elif color in secret_code:
            correct_color_wrong_placement.append(color)
        else:
            wrong.append(color)



    print(f"Secret code was: {secret_code} ")
    print(f"Your guess was: {user_guess} ")
    print(f"{len(correct_color_and_placement)} guesses with the correct color and placement: {correct_color_and_placement} ")
    print(f"{len(correct_color_wrong_placement)} guesses with the correct color but wrong placement: {correct_color_wrong_placement} ")
    print(f"Wrong guesses: {wrong}")


def main():
    secret_code = ["Blue", "Black", "Green","Red"]
    user_guess = ["Black","Blue","Green","Purple"]
    test_guess(secret_code,user_guess)

main()
