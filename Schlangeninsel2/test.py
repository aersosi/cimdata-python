character = {
    "name": "Arthur",
    "inventory": ["Kompass", "Taschenlampe", "Dosenbohnen"],
    "weapon": {"attack": 1, "luck": 1},
    "current_location": 0,
    "health": 0.25,
    "orientation": 1,

}

no_action = 0
unlikely_action = 0.65
neutral_action = 1
likely_action = 1.35

locations = {
    0: {
        "name": "Strand",
        "story": "Du befindest dich am Strand.",
        "action": {
            "names": ["(w)eiter", "(s)chlafen", "(e)ssen"],
            "keys": ["w", "s", "e"]
        },
        "fight_chance": no_action,
        "stray_chance": no_action,
        "eat_chance": no_action,
        "info": "Drücke [ENTER], um fortzufahren."
    },
    1: {
        "name": "Wald",
        "story": "Du befindest dich im Wald.",
        "action": {
            "names": ["(w)eiter", "(z)urück", "(s)chlafen", "(e)ssen"],
            "keys": ["w", "z", "s", "e"]
        },
        "fight_chance": unlikely_action,
        "stray_chance": neutral_action,
        "eat_chance": likely_action,
        "info": "Drücke [ENTER], um fortzufahren."
    }
}
import utils as u




char_location = 1

# Name des Ortes
print(
    f"\n[{locations[char_location]['name']}] fight_chance[{locations[char_location]['fight_chance']}] stray_chance[{locations[char_location]['stray_chance']}] eat_chance[{locations[char_location]['eat_chance']}]\n")


fight_dice = u.random_number(locations[char_location]['fight_chance'])
fight_message = "=> Ein Gegner erscheint!"

stray_dice = u.random_number(locations[char_location]['stray_chance'])
stray_message = "=> Du hast dich verlaufen!"

eat_dice = u.random_number(locations[char_location]['eat_chance'])
eat_message = "=> Du hast etwas zu essen gefunden!"

def dice_story(dice, message = "=> nichts passiert"):
    if dice > 0.5:
        u.text_red(f"{dice} {message}")

dice_story(fight_dice, fight_message)
dice_story(stray_dice, stray_message)
dice_story(eat_dice, eat_message)


# if fight_dice > 0.5:
#     u.text_red(f"{fight_dice} => Ein Gegner erscheint!")
# else:
#     print(f"{fight_dice}")
#
#
# if stray_dice > 0.5:
#     u.text_red(f"{stray_dice} => Du hast dich verlaufen!")
# else:
#     print(f"{stray_dice}")
#
#
# if eat_dice > 0.5:
#     u.text_red(f"{eat_dice} => Etwas zu essen gefunden!")
# else:
#     print(f"{eat_dice}")