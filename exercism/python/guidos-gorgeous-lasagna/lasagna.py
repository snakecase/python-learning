"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2 # Time in minutes required to prepare a layer before cooking.

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time before baking based on the number of lasagna layers.
    
    Parameters:
        number_of_layers (int): The number of lasagna layers desired to be in the dish.
        
    Returns:
        int: Time (in minutes) required for preparation before cooking dreived from 'PREPARATION_TIME'.
    """
    
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate total time spent on cooking.
    
    Parameters:
        number_of_layers (int): The number of lasagna layers desired to be in the dish.
        elapsed_bake_time (int): Time (in minutes) spent baking so far.

    Returns:
        int: The total time (in minutes) spent on preparing and baking
    """
    
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time