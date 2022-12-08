"""
Erzeuge eine Grafik einer bunten Blume
"""

from pytamaro.de import (
    Grafik,
    hsl_farbe,weiss,
    ellipse, leere_grafik,
    fixiere, kombiniere, drehe,
    zeige_grafik, speichere_grafik,
)

def reduziere(elemente: list, neutrales_element, f):
    resultat = neutrales_element
    for element in elemente:
        resultat = f(resultat, element)
    return resultat

# Kannst Du die Repetition mit Hilfe der obigen Funktion ausdrücken?

def zeichne_blaetter(anzahl_blaetter: int, radius: int)->list[Grafik]:
    alle_blaetter = []
    for i in range(1,anzahl_blaetter+1):
        alle_blaetter.append(drehe(i*(360/anzahl_blaetter),
        fixiere("mitte","unten",
            ellipse(radius*2,radius*8,
                hsl_farbe(i*(360/anzahl_blaetter),1,0.5,0.5)))))
    return alle_blaetter

def kombinere_blaetter(blaetter : list[Grafik])-> Grafik:
    return reduziere(blaetter,leere_grafik(),lambda x , y: kombiniere(x,y))

zeige_grafik(kombinere_blaetter(zeichne_blaetter(65,30)))


