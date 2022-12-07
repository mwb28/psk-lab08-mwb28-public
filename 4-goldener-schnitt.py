"""
Erzeuge Grafiken von Blütenstand und Blätterrosette
"""
from math import sqrt
from pytamaro.de import (
    Grafik, Farbe,
    weiss, schwarz, rgb_farbe, transparent,
    kreis_sektor, rechteck, ellipse, leere_grafik,
    ueberlagere, ueber, neben, fixiere, kombiniere, drehe,
    zeige_grafik, speichere_grafik, speichere_gif,
)

GRUEN = rgb_farbe(0, 161, 110)
GELB = rgb_farbe(255, 206, 46)

GOLDENER_SCHNITT = (sqrt(5) - 1) / 2
