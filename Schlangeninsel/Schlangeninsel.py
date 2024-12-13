import lib.abstractions as a
import lib.animations as ani
import lib.utils as u

#########
# Start #
#########

if __name__ == "__main__":
    ani.title_animation()

#########
# Start #
#########

print("Wie lautet dein Name?")

while True:
    first_enter = False
    user_name = input("")
    if user_name == "" and first_enter == False:
        # ugly hack to avoid complexity in ani.title_animation()
        first_enter = True
        continue
    elif not user_name.isalpha():
        u.clear_screen()
        u.text_red("Bitte nur Buchstaben eingeben.")
        print("Wie lautet dein Name?")
        continue
    else:
        u.clear_screen()
        break

##############
# New Screen #
##############

print(f"Hallo, {user_name}.")
print("Wie alt bist du?")

while True:
    user_age = input("\n> ")
    if not user_age.isdigit():
        u.clear_screen()
        u.text_red("Bitte nur Zahlen eingeben.")
        print("Wie alt bist du?")
        continue
    else:
        u.clear_screen()
        break

##############
# New Screen #
##############

print(f"Du bist zwar erst {user_age} Jahre alt,")
print("aber seitdem du hier auf der Insel aufgewacht bist, fühlst du dich mindestens 20 Jahre älter.\n")

print("Es hilft ja doch alles nichts. Du musst Schutz und nützliche Gegenstände finden.")
print("Vor dir liegt der dunkle Dschungel. In der Ferne ragt ein gewaltiger Berg in den Himmel.")
print("Du gehst direkt darauf zu und tief in den Dschungel hinein.")

u.text_grey("\nBestätige mit [ENTER], um fortzufahren.")
u.press_enter()

##############
# New Screen #
##############

print("Nach einer Weile befindest du dich tief im Dschungel.")
print("Vor dir befindet sich der Eingang zu einer Höhle. Hinter dir liegt der Strand.")

a.nosw_text()

while True:
    direction_01 = input("\n> ").lower()
    if direction_01 not in ["n", "o", "s", "w"]:
        u.clear_screen()
        u.text_red('Bitte nur die Buchstaben "n", "o", "s", "w" verwenden.')
        a.nosw_text()
        continue
    if direction_01 == "o":
        u.clear_screen()
        u.text_red("Der Weg nach Osten ist versperrt!")
        a.nosw_text()
        continue
    if direction_01 == "w":
        u.clear_screen()
        u.text_red("Der Weg nach Westen ist versperrt!")
        a.nosw_text()
        continue
    if direction_01 == "s":
        u.clear_screen()
        u.text_red("Zurück zum Strand macht keinen Sinn.")
        a.nosw_text()
        continue
    if direction_01 == "n":
        u.clear_screen()
        break

##############
# New Screen #
##############

print("Du gehst nach Norden in die Höhle.\n")
print("Aus dem Augenwinkel bemerkst du eine Silhouette in der dunklen Ecke.")
print("Es handelt sich um ein Skelett.")
print("Um die Schulter hat es einen Beutel, und daneben liegt eine alte Öllampe und Streichhölzer.")

u.text_grey("\nBestätige mit [ENTER], um fortzufahren.")
u.press_enter()

##############
# New Screen #
##############

weapons = {
    0: ["(1)", "Eine Axt", "Die Axt"],
    1: ["(2)", "Eine Machete", "Die Machete"],
    2: ["(3)", "Einen Hammer", "Den Hammer"],
}
user_inventory = ["Einen Beutel", "Eine Lampe", "Streichhölzer"]

print("Was hält das Skelett da in der Hand? Ist das etwa eine Waffe?\n")
for weapon in weapons.values():
    print(f"{weapon[0]} {weapon[1]}")

u.text_grey("\nTippe 1, 2 oder 3 und bestätige mit [ENTER], um fortzufahren.")

while True:
    weapon_index = input("\n> ")
    try:
        weapon_index = int(weapon_index)
        if weapon_index not in range(1, len(weapons) + 1):
            # Handle error: Numbers out of range 1–3
            u.clear_screen()
            u.text_red("Bitte nur Zahlen von 1 bis 3 eingeben.")
            
            print(f"\nWas hält das Skelett da in der Hand?\n")
            for weapon in weapons.values():
                print(weapon[0], weapon[1])
            
            u.text_grey("\nTippe 1, 2 oder 3 und bestätige mit [ENTER], um fortzufahren.")
            continue
        else:
            u.clear_screen()
            a.weapons_text(weapon_index - 1, user_inventory, weapons)
            u.press_enter()
            break
    except ValueError:
        # Handle error: Input is no number
        u.clear_screen()
        u.text_red("Bitte nur Zahlen von 1 bis 3 eingeben.")
        
        print(f"\nWas hält das Skelett da in der Hand?\n")
        for weapon in weapons.values():
            print(weapon[0], weapon[2])
        
        u.text_grey("\nTippe 1, 2 oder 3 und bestätige mit [ENTER], um fortzufahren.")
        continue

##############
# New Screen #
##############

print(f"In deinem Beutel befindet sich dein Inventar.\n")
print(f"Momentan besitzt du:")

for index, item in enumerate(user_inventory):
    print(f"({index+1}) {item}")

u.text_grey("\nBestätige mit [ENTER], um fortzufahren.")
u.press_enter()


#######
# END #
#######

u.clear_screen()
if __name__ == "__main__":
    ani.end_animation()

#######
# END #
#######
