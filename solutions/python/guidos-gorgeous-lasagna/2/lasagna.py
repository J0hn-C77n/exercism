"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40

def bake_time_remaining(spent):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    left_in_oven = EXPECTED_BAKE_TIME - spent
    return left_in_oven

PREPARATION_TIME = 2

def preparation_time_in_minutes(number_of_layers):
    """Calculate the time needed for prepairing given number of layers

    :param number_of_layers: int - the number of layers in the lasagna.
    :param PREPARATION_TIME: int - the number of time it takes to prepare one layer.
    :return: int - total time elapsed (in minutes) preparing lasagna.
    """
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapased_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    this function takes two integers representing the number of lasagna layers and and the time already spent baking and calculates the total elapsed minutes spent cooking the lasagna.    
    """
    return number_of_layers * PREPARATION_TIME + elapsed_bake_time
