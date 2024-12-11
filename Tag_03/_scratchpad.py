cities = ["Berlin", "Hamburg", "Frankfurt"]

print(cities)
print(type(cities)) # <class 'list'>

# Bonn hinzufügen
cities.append("Bonn") # Append object to the end of the list.
print(cities)

# Frankfurt
print(cities[2])
print(cities[-2]) # alternativ

# auch andere Datentypen in einer Liste möglich, hier int:
zahlen = [1, 5, 10, 300, 22, 31]
print(zahlen)

# Anzahl der Elemente einer Liste per built-in len()-Funktion, also unabhängig vom Datentyp Liste
print(len(cities)) # 4



# Hinweis: auch ein String ist wie eine Art Liste (Auflistung von Zeichen)
#Index  0   1   2   3   4   5   6
#Ort    B   e   r   l   i   n   Error

ort = "Berlin"
print(type(ort)) # <class 'str'>
print(len(ort)) # 6

# B
print(ort[0])
#print(ort[6]) # IndexError: string index out of range

# Listen sind flexibel, d.h. wir können 1) Datentypen mischen und sind 2) bei der Anzahl uneingeswchränkt (wie zB bei Java Arrays)
person = ["Peter", "Schmitz", 33, True, "Berlin"] # Infos zu einer Peson

# Einkaufsliste erzeugen
einkaufsliste = ["Kiwi", "Nudeln", "Öl", "Taschentücher", "Schokolade"]