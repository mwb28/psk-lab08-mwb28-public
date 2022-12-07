"""
Erzeuge eine Grafik eines Gänseblümchens
"""

from pytamaro.de import (
    Grafik,
    weiss, schwarz, rgb_farbe,gelb,
    ellipse, leere_grafik,
    fixiere, kombiniere, drehe,ueberlagere,
    zeige_grafik, speichere_grafik,
)

GELB = rgb_farbe(255, 206, 46)

def margritli(radius: float) -> Grafik:
    alle_blaetter= leere_grafik()
    for i in range(1,13):
        alle_blaetter = kombiniere(
                alle_blaetter,
                drehe(i*30,fixiere(
                    "mitte", "unten", 
                    ellipse(radius*2,radius*8,weiss)
                    )
                    )
                )
    bluete= ellipse(radius*4,radius*4,gelb)
    return ueberlagere(bluete,alle_blaetter)
            

     
zeige_grafik(margritli(40))

