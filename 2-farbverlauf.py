"""
Erzeuge eine Grafik einer bunten Blume
"""

from pytamaro.de import (
    Grafik,
    hsl_farbe,
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

def farbige_blume(radius: float) -> Grafik:
    pass
