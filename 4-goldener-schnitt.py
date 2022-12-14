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


def reduziere(elemente: list, neutrales_element, f):
    resultat = neutrales_element
    for element in elemente:
        resultat = f(resultat, element)
    return resultat

def bluetenstand(drehung: float, anzahl : int, farbe : Farbe, groesse_bluete : float)-> Grafik:
    drehung = 360*drehung
    blueten = [drehe(drehung*i,kombiniere(
                fixiere("rechts","mitte",rechteck(sqrt(i)*80 +100 ,1,transparent)),
                fixiere("links","mitte",ellipse(groesse_bluete,groesse_bluete,farbe))))
                for i in range(anzahl)]
    return reduziere(blueten,leere_grafik(),lambda x,y: ueberlagere(x,y))        

# zeige_grafik(bluetenstand2(GOLDENER_SCHNITT,400))+



def bluetenstand_farbig(drehung: float, anzahl: int, groesse_bluete : float) -> Grafik:
    zeichne_blueten = leere_grafik()
    
    drehung = 360*drehung
    for i in range(anzahl):
        kreis = ellipse(groesse_bluete,groesse_bluete,hsl_farbe(i*(60/anzahl),1,0.5,1))
        blueten_mit_abstand = kombiniere(
                            fixiere("rechts","mitte",rechteck(sqrt(i)*10+10,1,transparent)),
                            fixiere("links","mitte",kreis))
        zeichne_blueten = ueberlagere(drehe(drehung*i+1,blueten_mit_abstand),zeichne_blueten) 
    # hintergrund = rechteck(1800,1800,schwarz)
    return zeichne_blueten

# zeige_grafik(bluetenstand(GOLDENER_SCHNITT,400))




def zeichne_blatt(blattradius: float, farbe : Farbe)-> Grafik:
    blattteil_vorne = ueberlagere(drehe(150,kreis_sektor(blattradius,120,farbe)),
                        drehe(330,kreis_sektor(blattradius,120,farbe)) ) 
    blatteil_hinten = ueberlagere(drehe(150,kreis_sektor(blattradius+5,120,schwarz)),
                        drehe(330,kreis_sektor(blattradius+5,120,schwarz))  ) 
  
    return ueberlagere(blattteil_vorne,blatteil_hinten)

 
   
def blaetter_rosette(drehung: float, anzahl : int, blattradius : float)-> Grafik:
    drehung = 360*drehung
    blaetter = [drehe(drehung*i,kombiniere(
                fixiere("rechts","mitte",rechteck(sqrt(i)*58+125,1,transparent)),
                fixiere("links","mitte",zeichne_blatt(blattradius,hsl_farbe(i*(120/anzahl),0.5,0.5,1)))))
                for i in range(anzahl)]
    return reduziere(blaetter,leere_grafik(),lambda x,y: ueberlagere(x,y))  

speichere_grafik("wettbewerbsblume", ueberlagere(bluetenstand_farbig(GOLDENER_SCHNITT,400,20),blaetter_rosette(GOLDENER_SCHNITT,30,90)))

# speichere_gif("bluetenstand",[bluetenstand(GOLDENER_SCHNITT + schritt*0.00001, 400) for schritt in range(200)],100)
