import sys
import select
from time import sleep
from getkey import getkey, keys

import lib.utils as u
import lib.ascii_art as ascii

def title_animation():
    animation(ascii.title_screen_1, ascii.title_screen_2)

def animation(ani1, ani2):
    try:
        while True:
            # Prüfe auf Benutzer-Eingabe (nicht blockierend)
            if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
#                 key = getkey()  # Wait for user input
#                 if key == keys.ENTER:  # Exit on Enter key
                u.clear_screen()
                break

            # Title Screen
            u.clear_screen()
            for row in ani1:
                print(row)
            sleep(0.5)

            # End Screen
            u.clear_screen()
            for row in ani2:
                print(row)
            sleep(0.5)
    except KeyboardInterrupt:
        pass  # Handle exit with Ctrl+C