import os
from getkey import getkey, keys
from termcolor import colored
import random


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





def random_number(chance = 1.00):
    """
    chance = 0.65 => is unlikely
    chance = 1.00 => is neutral
    chance = 1.35 => is likely
    """

    ran_ranges = []
    for i in range(1, 20):
        ran_ranges.append(random.randrange(0, 100) / 100)
    return round(random.choice(ran_ranges) * chance, 2)

# Wie häufig bei chance 0.75 sind zahlen über 0,5
# 0.65 => ca 1/3 der zahlen sind über 0,5
# 1 => ca 1/2 der zahlen sind über 0,5
# 1.35 => ca 2/3 der zahlen sind über 0,5
# zahlen = []
# for i in range(1, 1000):
#     if random_number(1.35) >= 0.5:
#         zahlen.append(random_number())
# print(f" {len(zahlen)} von 1000")