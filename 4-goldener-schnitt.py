"""
Erzeuge Grafiken von Blütenstand und Blätterrosette
"""
from math import sqrt
from pytamaro.de import (
    Grafik, Farbe,
    weiss, schwarz, rgb_farbe,hsl_farbe, transparent,
    kreis_sektor, rechteck, ellipse, leere_grafik,
    ueberlagere, ueber, neben, fixiere, kombiniere, drehe,
    zeige_grafik, speichere_grafik, speichere_gif,
)

GRUEN = rgb_farbe(0, 161, 110)
GELB = rgb_farbe(255, 206, 46)

GOLDENER_SCHNITT = (sqrt(5) - 1) / 2
def bluetenstand(drehung: float, anzahl: int) -> Grafik:
    zeichne_blueten = leere_grafik()
    
    drehung = 360*drehung
    for i in range(anzahl):
        kreis = ellipse(180,180,hsl_farbe(i*(360/anzahl),1,0.5,0.5))
        abstand = sqrt(i)*80+20
        blueten_mit_abstand = kombiniere(
                            fixiere("rechts","mitte",rechteck(abstand,1,transparent)),
                            fixiere("links","mitte",kreis))
        zeichne_blueten = ueberlagere(drehe(drehung*i+1,blueten_mit_abstand),zeichne_blueten) 
    hintergrund = rechteck(1800,1800,schwarz)
    return ueberlagere(zeichne_blueten,hintergrund)

zeige_grafik(bluetenstand(GOLDENER_SCHNITT,400))

# speichere_gif("bluetenstand",[bluetenstand(GOLDENER_SCHNITT + schritt*0.00001, 400) for schritt in range(200)],100)
