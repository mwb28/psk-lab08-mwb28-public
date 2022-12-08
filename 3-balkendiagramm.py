"""
Erzeuge Grafik eines Balkendiagramms der animals Daten
"""
from pytamaro.de import (
    Grafik, Farbe,
    magenta, rot, blau,transparent,
    text, rechteck, ellipse, leere_grafik,
    grafik_breite, grafik_hoehe,
    neben, fixiere, kombiniere, ueber,
    zeige_grafik, speichere_grafik,
)
from csv import DictReader

GESCHLECHTS_FARBEN = {"female": rot, "male": blau, "hermaphrodite": magenta}

# def reduziere(elemente: list, neutrales_element, f):
#     resultat = neutrales_element
#     for element in elemente:
#         resultat = f(resultat, element)
#     return resultat

def balken_diagramm(balken_hoehe: float) -> Grafik:
    # öffne die Datei zum Lesen (read, r)
    file = open("animals.csv", "r")
    # erzeuge einen CSV Dictionary Reader, der die Datei einliest und durch die Zeilen iterieren kann
    leser = DictReader(file, delimiter=",")
    
    abstand_vertikal = rechteck(balken_hoehe,balken_hoehe/3,transparent)
    abstand_balken = rechteck(balken_hoehe,balken_hoehe/8,transparent)
    label_spalte = leere_grafik()
    balken_spalte = leere_grafik()
    farbe = magenta
    for tier in leser:
        if (tier["Sex"]== "female"):
            farbe = rot
        elif(tier["Sex"]== "male"):
            farbe = blau
        else: 
            farbe = magenta
        
        label_spalte= kombiniere(fixiere("rechts","unten",label_spalte),
                    fixiere("rechts","oben",
                    kombiniere(fixiere("rechts", "unten",abstand_vertikal),
                    fixiere("rechts", "oben",text(tier["Name"],"Arial",balken_hoehe,farbe))
                    )))
        balken_spalte = kombiniere(fixiere("links","unten",balken_spalte),
                        fixiere("links","oben",
                        kombiniere(fixiere("links","unten",abstand_balken),
                        fixiere("links","oben",zeichne_anzahl_kreise(int(tier["Legs"]),balken_hoehe,farbe))
                        )
                        )
        
        
        )
        
    return neben(label_spalte,neben(abstand_vertikal,balken_spalte))





def zeichne_anzahl_kreise(anzahl_kreise: int, balken_hoehe: float, farbe: Farbe)-> Grafik:

    abstand = rechteck(balken_hoehe/4,balken_hoehe/4,transparent)
    zeichne_kreise = leere_grafik()
    for i in range(anzahl_kreise):
        zeichne_kreise= neben(zeichne_kreise,neben(ellipse(balken_hoehe,balken_hoehe,farbe),abstand))
    if anzahl_kreise == 0:
        return rechteck(balken_hoehe,balken_hoehe,transparent)
    else: return zeichne_kreise


zeige_grafik(balken_diagramm(39))

