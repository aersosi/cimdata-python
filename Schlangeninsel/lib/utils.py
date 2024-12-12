import os
import sys
from getkey import getkey, keys
from termcolor import colored

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def press_enter():
    while True:
        key = getkey()
        if key == keys.ENTER:
            clear_screen()
            break
        else:
            clear_screen()
            text_red("Drücke [ENTER] zum fortfahren")
            continue
    
    
    
def text_red(text):
    """Prints the given text in red color.

    Args:
        text: The text to be printed in red.
    """
    print(colored(text, "red"))



def text_grey(text):
    """Prints the given text in grey color.

    Args:
        text: The text to be printed in grey.
    """
    print(colored(text, "light_grey"))
    
    
    
def first_lower(string):
    """Converts the first letter of a string to lowercase.

    Args:
        string: The input string.

    Returns:
        The string with the first letter converted to lowercase.
        
    # Example usage:
    text = "Hello, World!"
    result = first_lower(text)
    print(result)  # Output: "hello, World!"
        
    """

    if string:
        return string[0].lower() + string[1:]
    else:
        return string




