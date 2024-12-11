# Spielwiese als Einführung in Python zB print(), input(), Variablen, Datentypen

print("Hallo Python") # OHNE Semikolon ; am Ende
print('Bye') # auch mit einfachen Anführungszeichen möglich

# einzeiliger Kommentar

#
# mehrzeiliger Kommentar (Variante 1)
#

"""
mehrzeiliger Kommentar (Variante 2)
"""

'''
mehrzeiliger Kommentar (Variante 3)
'''

# Variablen
# (Container, um bestimmte Werte wie zB Zahlen oder Zeichenketten abzulegen)
vorname = "Peter"
nachname = 'Schmitz'
print("Hallo",    "Peter")
print("Hallo",vorname) # Hallo Peter # sep als Default " " (also ein Leerzeichen)
print("Hallo", vorname, sep="*") # Hallo*Peter
# alternative Schreibweise per String-Verknüpfung (+)
print("Guten Tag " + vorname + " " + nachname) # Guten Tag Peter Schmitz
print("Guten Tag",vorname,nachname) # Guten Tag Peter Schmitz

# Usereingaben verarbeiten
# per input() - Read a string from standard input.
# Ziel: Namen eines user abfragen und weiterverarbeiten
# User trägt Namen einen per Tastatur ein bestätigt mit Enter
eingabe = input("Wie heißt Du denn?")
print("Hallo", eingabe)

# Ziel: Alter vom User abfragen
alter = int(input("Wie alt bist Du?")) # str -> int
# danach das Alter um 1 erhöhen und nochmal das neue Alter anzeigen
#alter = alter + 1 # Error: can only concatenate str (not "int") to str

# alternative Kurzform
alter += 1

print("Du bist jetzt so alt:", alter)
# Info: User-Input ist IMMER ein String!!!
# daher bei Berechnungen konvertieren, hier zB von einem String in einen int (Casting)

# Datentyp auslesen per type()
print(type(vorname)) # <class 'str'>
print(type(alter)) # <class 'int'>

# Datentypen:
# https://www.w3schools.com/python/python_datatypes.asp