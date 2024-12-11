# Spielwiese für versch. Datentypen (Duck-Typing)

##### Zuweisung/Initiierung

# String
x = "Hallo Python"
x = 'Hallo \"Python'

# Integer
x = 200

# Float
x =  20.5

# List (Container, der mehrere Elemente aufnahmen kann)
x = ["hallo", "ballo", "1", 2, 3]
x.append("Arthur")

# Tupel (Wie eine Liste aber in runde Klammern and it"s fucking immutable)
x = ("hallo", "ballo", "1", 2, 3)

# Range
x = range(2,12,2) # erzeugt [2,4,6,8,10,12] => x.[2] = 6

# Dictionary
x = {"key1": "value1"}

# Bool
x = True

# Set (Reihenfolge ist randomisiert, es gibt keine Dopplungen)
x = {"Berlin", "Hamburg", "Frankfurt"}
x.add("Bonn")
x.add("Berlin")



##### Ausgabe

print("\n")
print(f"This is: {x}")

print("\n")
print(f"This type is: {type(x)}")

# Index des 1. Listen Elements
# print("\n")
# print(f"This is: {x[0]}")

# Liste Erweitern durch "Methoden" 
# print("\n")
# print(f"This is: {x[-1]}") # nur für Listen

# Range auslesen => Erst in Liste konvertieren
# print("\n")
# print(f"This is: {list(x)}") # nur für Listen

# Dict auslesen durch key
# print("\n")
# print(f"This is: {x["key1"]}")
