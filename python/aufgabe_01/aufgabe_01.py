import math

breite = float(input('Breite: '))
laenge = float(input('Länge: '))
hoehe = float(input('Höhe: '))

# Volumen
volumen = breite * laenge * hoehe
print('Volumen: ' + str(volumen))

# Oberfläche
oberflaecheninhalt = 2 * ((breite * laenge) + (breite * hoehe) + (laenge * hoehe))
print('Oberflächeninhalt: ' + str(oberflaecheninhalt))

# Raumdiagonale
raumdiagonale = math.sqrt(breite**2 + laenge**2 + hoehe**2)
print('Raumdiagonale: ' + str(raumdiagonale))