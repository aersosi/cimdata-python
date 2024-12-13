##############
# New Screen #
##############

import utils as u
from termcolor import colored
from time import sleep
import random


# [ ] todo: verloren function: character["inventory"].remove(random.choice(character["inventory"]))
# [ ] todo: kompass weg = locations["name"] verschwindet, location wird um 1 zurück gesetzt, orientation = 0.5
# [ ] todo: Taschenlampe weg = interface farben schwer zu lesen, attack * 0.5, luck * 0.5
# [ ] todo: waffe weg = attack * 0.5, luck * 0.5
# [X] todo: verlaufen implementieren (chance, dass die gleiche location nochmal erscheint bei weiter oder zurück)

# [ ] todo: essen finden: wenn essen gefunden, item nahrung zum inventar hinzufügen

nahrung = ["Apfel", "Banane", "Kiwi"]

character = {
    "name": "Arthur",
    "inventory": ["Kompass", "Taschenlampe"],
    "weapon": {"attack": 1, "luck": 1},
    "health": 0.25,
    "current_location": 0,
    "orientation": 1,
}

no_action = 0
unlikely_action = 0.65
neutral_action = 1
likely_action = 1.35

locations = {
    0: {
        "name": "Strand",
        "fight_chance": no_action,
        "stray_chance": no_action,
        "eat_chance": no_action,
        "story": "Du befindest dich am Strand.",
        "action": {
            "names": ["(w)eiter", "(s)chlafen", "(e)ssen"],
            "keys": ["w", "s", "e"]
        },
        "info": "Drücke [ENTER], um fortzufahren."
    },
    1: {
        "name": "Wald",
        "fight_chance": likely_action,
        "stray_chance": neutral_action,
        "eat_chance": unlikely_action,
        "story": "Du befindest dich im Wald.",
        "action": {
            "names": ["(w)eiter", "(z)urück", "(s)chlafen", "(e)ssen"],
            "keys": ["w", "z", "s", "e"]
        },
        "info": "Drücke [ENTER], um fortzufahren."
    },
    2: {
        "name": "Vor der Höhle",
        "fight_chance": unlikely_action,
        "stray_chance": no_action,
        "eat_chance": likely_action,
        "story": "Du befindest vor einer Höhle.",
        "action": {
            "names": ["(w)eiter", "(z)urück", "(s)chlafen", "(e)ssen"],
            "keys": ["w", "z", "s", "e"]
        },
        "info": "Drücke [ENTER], um fortzufahren."
    },
    3: {
        "name": "Höhleneingang",
        "fight_chance": no_action,
        "stray_chance": no_action,
        "eat_chance": no_action,
        "story": "Du befindest dich im Höhleneingang.",
        "action": {
            "names": ["(w)eiter", "(z)urück", "(s)chlafen", "(e)ssen"],
            "keys": ["w", "z", "s", "e"]
        },
        "info": "Drücke [ENTER], um fortzufahren."
    },
    4: {
        "name": "Tief in der Höhle",
        "fight_chance": unlikely_action,
        "stray_chance": likely_action,
        "eat_chance": unlikely_action,
        "story": "Du befindest dich tief in der Höhle.",
        "action": {
            "names": ["(w)eiter", "(z)urück", "(s)chlafen", "(e)ssen"],
            "keys": ["w", "z", "s", "e"]
        },
        "info": "Drücke [ENTER], um fortzufahren."
    },
    5: {
        "name": "Quelle",
        "fight_chance": likely_action,
        "stray_chance": no_action,
        "eat_chance": likely_action,
        "story": "Du befindest dich an einer Quelle.",
        "action": {
            "names": ["(w)eiter", "(z)urück", "(s)chlafen", "(e)ssen"],
            "keys": ["w", "z", "s", "e"]
        },
        "info": "Drücke [ENTER], um fortzufahren."
    },
    6: {
        "name": "Traum",
        "fight_chance": no_action,
        "stray_chance": no_action,
        "eat_chance": no_action,
        "story": "Du bist aufgewacht. Was für ein kurioser Traum!",
        "action": {
            "names": [],
            "keys": []
        },
        "info": "Drücke [ENTER], um fortzufahren."
    },
    7: {
        "name": "Trauma",
        "fight_chance": no_action,
        "stray_chance": no_action,
        "eat_chance": no_action,
        "story": "Du bist gestorben. Was für ein kurioser Traum!",
        "action": {
            "names": [],
            "keys": []
        },
        "info": "Drücke [ENTER], um fortzufahren."
    },
}

enemies_1 = {
    0: {
        "name": "Schlange",
        "health": 0.5,
        "attack": 1.5,
        "luck": 1.5
    },
    2: {
        "name": "Wildschwein",
        "health": 1.5,
        "attack": 1,
        "luck": 0.5
    },
    3: {
        "name": "Raubkatze",
        "health": 1,
        "attack": 0.5,
        "luck": 1
    },
}


# setup
stray_message = "=> Du hast dich verlaufen und bist wieder genau am gleichen Ort wie vorher!"
eat_message = "=> Du hast etwas zu essen gefunden!"
fight_message = "=> Ein Gegner erscheint!"

max_sleep_times = 2
sleep_below_percent = 0.4
sleep_health_increase = 0.1

max_food = 3
eat_health_increase = 0.1

user_wait_time = 3


# Initialize global variables
sleep_counter = 0  # Persistent variable for sleep tracking
dice_values = {"stray_dice": 0, "eat_dice": 0, "fight_dice": 0}


def calculate_dices():
    """Berechnet die Würfelwerte basierend auf der aktuellen Location"""
    current_location = character["current_location"]
    dice_values["stray_dice"] = u.random_number(locations[current_location]['stray_chance'])
    dice_values["eat_dice"] = u.random_number(locations[current_location]['eat_chance'])
    dice_values["fight_dice"] = u.random_number(locations[current_location]['fight_chance'])


def dice_story(dice, message="=> nichts passiert"):
    if dice > 0.5:
        u.text_red(f"{dice} {message}")


theme_box = {
    'topLeft': '╔',
    'topRight': '╗',
    'bottomRight': '╝',
    'bottomLeft': '╚',
    'vertical': '║',
    'centerLeft': '╠',
    'horizontal': '═',
    'centerRight': '╣',
    'empty': ' ',
}


def print_box(top_bottom="top", color="white", width=50):
    if color:
        print(colored(
            theme_box[f'{top_bottom}Left'] + theme_box['horizontal'] * (width - 2) + theme_box[f'{top_bottom}Right'],
            color))
    else:
        print(theme_box[f'{top_bottom}Left'] + theme_box['horizontal'] * (width - 2) + theme_box[f'{top_bottom}Right'])


def print_interface(character):
    char_location = character["current_location"]

    # Name des Ortes
    print(
        f"\n{theme_box['vertical']} {locations[char_location]['name']} fight_chance {locations[char_location]['fight_chance']} | stray_chance {locations[char_location]['stray_chance']} | eat_chance {locations[char_location]['eat_chance']} {theme_box['vertical']}\n")

    # Charakter-Status
    if locations[char_location]['action']['names']:
        character_status_string = f"{theme_box['vertical']} Gesundheit {int(character['health'] * 100)}% {theme_box['vertical']} Angriff {character['weapon']['attack'] * 100}% {theme_box['vertical']} Glück {character['weapon']['luck'] * 100}% {theme_box['vertical']}"
        character_status_length = len(character_status_string)
        print_box("top", "green", character_status_length)
        print(colored(character_status_string, "green"))
        print_box("bottom", "green", character_status_length)

    # Inventar
    if locations[char_location]['action']['names']:
        inventory_string = f"{theme_box['vertical']} " + " ".join(
            [f"{item} {theme_box['vertical']}" for item in
             character["inventory"][:-1]]) + f" {character['inventory'][-1]} {theme_box['vertical']}"
        inventory_length = len(inventory_string)

        print_box("top", "blue", inventory_length)
        print(colored(inventory_string, "blue"))
        print_box("bottom", "blue", inventory_length)

    # Story des Ortes
    print(f"\n\n{locations[char_location]['story']}\n\n")

    # Events des Ortes
    dice_story(dice_values["stray_dice"], stray_message)
    dice_story(dice_values["eat_dice"], eat_message)
    dice_story(dice_values["fight_dice"], fight_message)

    # Aktionen am Ort
    if locations[char_location]['action']['names']:
        actions_string = f"{theme_box['vertical']} " + " ".join(
            [f"{item} {theme_box['vertical']}" for item in
             locations[char_location]['action']['names'][:-1]]) + f" {locations[char_location]['action']['names'][-1]} {theme_box['vertical']}"
        actions_length = len(actions_string)


        print(colored("Was möchtest du tun?", "light_grey"))
        print_box("top", "", actions_length)
        print(actions_string)
        print_box("bottom", "", actions_length)

    # Informationen zu Aktionen
    print(colored(locations[char_location]["info"], "light_grey") + "\n")


def action_info(info_text):
    u.clear_screen()
    u.text_red(info_text)
    print(f"\nWarte {user_wait_time} Sekunden, dann geht es weiter.")
    sleep(user_wait_time)  # Simulate wait time
    u.clear_screen()


def action_move(direction):
    """Handles movement (forward and backward)"""

    # Move forward
    if direction == "w":
        if character["current_location"] < len(locations) - 1:

            if dice_values["stray_dice"] > 0.5:
                character["current_location"] = character["current_location"]

            if dice_values["eat_dice"] > 0.5:
                if len(character["inventory"]) <= max_food:
                    character["inventory"].append(random.choice(nahrung))
                else:
                    print("Du kannst nicht mehr tragen.")

            else:
                character["current_location"] += 1
            u.clear_screen()
        else:
            action_info("Du kannst nicht weiter gehen!")

    # Move backward
    elif direction == "z":
        if character["current_location"] > 0:

            if dice_values["stray_dice"] > 0.5:
                character["current_location"] = character["current_location"]

            if dice_values["eat_dice"] > 0.5:
                if len(character["inventory"]) <= max_food:
                    character["inventory"].append(random.choice(nahrung))
                else:
                    print("Du kannst nicht mehr tragen.")

            else:
                character["current_location"] -= 1
            u.clear_screen()
        else:
            action_info("Du kannst nicht weiter zurückgehen!")


def action_eat():
    """Handles eating"""

    #todo: Inventory nach apfel, kiwi, banane durchsuchen
    #todo: Wenn kein Apfel, Kiwi oder Banane im Inventar, dann "leider nichts mehr zu Essen!"
    #todo: else: aus dem inventory eines der items die = apfel, kiwi oder babane sind entfernen


    if "Dosenbohnen" not in character["inventory"]:
        action_info("Du hast leider nichts mehr zu Essen!")
    else:
        character["inventory"].remove("Dosenbohnen")
        character["health"] += eat_health_increase
        character["health"] = round(character["health"], 1)
        action_info(f"Du hast etwas gegessen und {int(eat_health_increase * 100)}% deiner Gesundheit wiederhergestellt.")


def action_sleep():
    """Handles sleeping"""

    global sleep_counter  # Ensure sleep_counter persists
    if sleep_counter >= max_sleep_times:
        action_info("Du kannst nicht mehr schlafen!")
        return
    if character["health"] <= sleep_below_percent:  # Allow sleep only if health is below or equal to 40%
        character["health"] += sleep_health_increase
        character["health"] = round(character["health"], 1)
        sleep_counter += 1
        action_info(f"Du hast dich ausgeruht und {int(sleep_health_increase * 100)}% deiner Gesundheit wiederhergestellt.")
    else:
        action_info("Du brauchst keine Pause. Deine Gesundheit ist ausreichend.")


def action_attack():
    """Handles attacking"""
    # todo: implementieren


def actions():
    while True:
        user_action = input("\n> ").lower()

        # (w)eiter, (z)urück, (e)ssen, (s)chlafen, (a)ngreifen
        if user_action not in ["w", "z", "s", "e", "a"]:
            action_info('Bitte nur die Buchstaben "w", "z", "s", "e" und "a" verwenden.')
            continue

        if user_action in ["w", "z"]:  # (w)eiter, (z)urück
            action_move(user_action)
            break

        if user_action == "e":  # (e)ssen
            action_eat()
            break

        if user_action == "s":  # (s)chlafen
            action_sleep()
            break

        if user_action == "a":  # (a)ngreifen
            action_attack()
            break


# Main game loop
while True:
    calculate_dices()
    print_interface(character)
    actions()
