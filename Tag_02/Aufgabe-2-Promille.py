# Promillerechner (BAK: Blutalkoholkonzentration)

# https://de.wikipedia.org/wiki/Blutalkoholkonzentration#Widmark-Formel

# Bsp: 80kg schwerer Mann trinkt 0,5 Liter Bier (5% = 25g)
# Frage: wie hoch ist sein Promillewert im Blut?
# Antwort: ca. 0,36 Promille

# w der Massenanteil des Alkohols im Körper in ‰
# A die aufgenommene Masse des Alkohols in Gramm (g)
# m die Masse der Person in Kilogramm (kg)
# r der Reduktions- oder Verteilungsfaktor im Körper:
#   - Männer: 0,68–0,7
#   - Frauen/Jugendliche: 0,55–0,60
#   - Säuglinge/Kleinkinder: 0,75–0,80

# Formeln:
# W = A / (m * r) => Promille Formel
# A = V * e * 0.8

# m = 80.0 # Gewicht der Person in kg
# r = 0.7 # Verteilungsfaktor Mann: 0.7, Frau: 0.6
# V = 500.0 # Menge getrunken in ml
# e = 0.05 # Prozentgehalt des Getränks

# Ad = 0.8 # Alkoholdichte, fest definiert mit 0.8
# A = V * e * Ad # masse des Alkohols

# W = A / (m * r) # Promille ungerundet
# print(W)

# def red(text):
#     print(colored(text, "red"))


def promille(m = 80.0, V = 500.0, e = 0.05, male = True, roundResult = True):
    if (male == True):
        r = 0.7 # Verteilungsfaktor Mann: 0.7
    else:
        r = 0.6 # Verteilungsfaktor Frau: 0.6
        
    Ad = 0.8 # Alkoholdichte, fest definiert mit 0.8
    A = V * e * Ad # masse des Alkohols
    W = A / (m * r) # Promille ungerundet

    if (roundResult == True):
        W = round(W, 2) # gerundet
    else:
        W = W
    # print(W)
    return W
    
    
    
wert = promille(80.0, 500.0, 0.05) # Mann + ein Bier
print ("\n", wert)

wert = promille(80.0, 500.0, 0.0) # Alkoholfrei
print ("\n", wert)

wert = promille(65.0, 50.0, 0.4) # Mann 2 Shots
print ("\n", wert)

wert = promille(65.0, 40.0, 0.4, False) # Frau 2 Shots
print ("\n", wert)

wert = promille(roundResult = False)
print ("\n", wert)

name = "Arthur"
ort = "Hamburg"
wert = promille()

# oldschool interpolieren in den String
loremIpsum = "{} aus {} hat {} Promille".format(name, ort, wert)
print("\n", loremIpsum)

# modernes interpolieren in den String
loremfstring = f"{name} aus {ort} hat {wert} Promille"
print("\n", loremfstring)

# runden ohne round(), syntax aus C
wert = 0.35714285714285715
print(f"1. Testfall: {wert:.2f}")

