# Übungsaufgabe(n) (gerne gemeinsam in Gruppe):

# wie Promillerechner heute, aber:

# - mindestens eine eigens recherchierte Formel, u.a.
# - BMI (Body-Mass-Index)
# - Stoffwechselrate
# - Baumstammvolumen
# - Körperoberfläche
# - irgendeine andere Formel je nach Interesse/Recherche
# - oder auch gerne Promillerechner aber mit anderer Formel STATT Widmark, siehe Wikipedia

# BONUS:
# Gerne mit User-Input verknüpfen für die Datenübermittlung

# BONUS:
# die eigene Formel oder den Promillerechner in euer Text-Adventure-Grundgerüst integrieren
# zB in dem Adventure Bier/Wein o.ä. trinken und den Promillewert checken, hier könnte dann in zukünftigen Versionen der Spieler
# aufgrund hohen Alkoholpegel eingschränkt sein, zB in einem Duell/bei einem Überfall bzw. in eine Polizeikontrolle geraten etc.

# Viel Spaß und Erfolg! Gemeinsame Besprechung dazu morgen Vomittag - bei Rückfragen vorab im Chat

# Die aktuellen Stände dann nachher bitte hier als Kommentar posten mit Quellcode - Merci!

from termcolor import colored

# Frage: was kostet es mich mein Eiweiß aus einem bestimmten Lebensmittel zu beziehen?

# Wie viel Eiweiß möchte ich pro Tag zu mir nehmen?
# Wie viel Prozent Eiweiß enthält das Lebensmittel?
# Wie teuer ist das Lebensmittel pro Kilo?
# Auf wie viele Tage sollte das hochgerechnet werden?

def howMuchIsTheWHEY(wunschProteinGrammProTag, lebensmittelProteinProzent, preisProKilo, xTage = 1, rundenAuf = 2):
    # Berechnet die Menge und die Kosten
    erforderlicheMenge = wunschProteinGrammProTag / (lebensmittelProteinProzent / 100)
    erforderlicheMenge = round(erforderlicheMenge * xTage, rundenAuf)
    
    kosten = (erforderlicheMenge / 100) * (preisProKilo / 10)
    kosten = round(kosten, rundenAuf)
        
    resultText = [
        "", # leerzeile
        f"Du benötigst {colored(f'{erforderlicheMenge} g', 'red')} des Lebensmittels pro {xTage} Tag(e).",
        f"Die Kosten dafür betragen {colored(f'{kosten} €', 'red')}.",
        "", # leerzeile
    ]
        
    for text in resultText:
        print(text)

howMuchIsTheWHEY(180,72,18, 30)

