import lib.utils as u

def nosw_text():
    u.text_grey("\nDu kannst nach (N)orden, (O)sten, (S)üden, (W)esten gehen.")
    u.text_grey("Was möchtest du tun?")
    
def weapons_text(index, user_inventory, weapons):
    print(f"Das Skelett hält {u.first_lower(weapons[index][1])} in der Hand!")
    print(f"\nDu nimmst den Beutel, die Lampe und {u.first_lower(weapons[index][2])} an dich")
    print("... und gehst tiefer in die Höhle.")
    
    user_inventory.append(weapons[index][1])
    u.text_grey("\nBestätige mit [ENTER], um fortzufahren.")