"""
Erzeuge Grafik eines Balkendiagramms der animals Daten
"""
from pytamaro.de import (
    Grafik,
    magenta, rot, blau,
    text, rechteck, ellipse, leere_grafik,
    grafik_breite, grafik_hoehe,
    neben, fixiere, kombiniere,
    zeige_grafik, speichere_grafik,
)
from csv import DictReader

GESCHLECHTS_FARBEN = {"female": rot, "male": blau, "hermaphrodite": magenta}

def balken_diagramm(balken_hoehe: float) -> Grafik:
    # öffne die Datei zum Lesen (read, r)
    file = open("animals.csv", "r")
    # erzeuge einen CSV Dictionary Reader, der die Datei einliest und durch die Zeilen iterieren kann
    leser = DictReader(file, delimiter=",")
    #...
    return neben(label_spalte, balken_spalte)
