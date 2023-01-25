import time
import random
import pygame
from pygame.locals import *
import datetime
import pygame
from datetime import date
import sys

Schwarz = (0, 0, 0)
Grau = (127, 127, 127)
Weiß = (255, 255, 255)
P = 100  # Parkplatzanzahl
breite_screen = 1250
hohe_screen = 530

pygame.init()
screen = pygame.display.set_mode((breite_screen, hohe_screen))
screen.fill(Grau)

# Koordinaten Anzeigefenster
x_anzeigefenster = 970
y_anzeigefenster = 0
breite_anzeigefenster = 300
hohe_anzeigefenster = 410

# Koordinaten Zurückfenster
x_zurückfenster = 970
y_zurückfenster = 470
breite_zurückfenster = 300
hohe_zurückfenster = 130

# Koordinaten Rand Links
x_Rand1 = 0
y_Rand1 = 0
breite_Rand1 = 40
hohe_Rand1 = 300
x_Rand2 = 0
y_Rand2 = 350
breite_Rand2 = 40
hohe_Rand2 = 250

date = str(date.today())

# Parkplatz maße
hohe_Parkplatz = 60
breite_Parkplatz = 40
breite_Straße = 50
x_Parkplatz1 = breite_Straße + breite_Rand1
y_Parkplatz1 = 240

#variable auto
carspawntime = random.randint(3, 5)
carsinlot = []
starttime = time.time()
carcolours =[]
extras = ['family', 'handycaped']
carcounter = 1
carsize = (60, 30)
#variable bezahlung
price = 8 # Preis pro h in €
revenue = 0
#variable parkdauer
hins = 3600 #StundeinSekunde(3600)
minparkdauer = 10 #900 = 15 min in s
maxparkdauer = 30 #43200 = 12h in s

#variable parken
maxplaetze_pro_reihe = 20
einfahrtslaenge = breite_Rand1
xeinfahrt = 0
yeinfahrt = (y_Rand1 + hohe_Rand1) + (y_Rand2 - (y_Rand1 + hohe_Rand1))/4
xausfahrt = 600
yausfahrt = 300

#bildeinstellungen
whitecar = pygame.image.load('redcar.png')
whitecar = pygame.transform.scale(whitecar, carsize)
whitecar = pygame.transform.rotate(whitecar, 180)
whitecar.set_colorkey((255, 255, 255))
carcolours.append(whitecar)

def datum(msg='Datum: ' + date):
    my_font = pygame.font.Font(None, 40)
    text_surface = my_font.render(msg, True, Weiß)
    text_rect = text_surface.get_rect()
    text_rect.center = (1200, 15)
    screen.blit(text_surface, text_rect)
class cars:
    def __init__(self, cartimer, entrietime, exittime, lotnumber, carpos, colour, extra):
        self.cartimer = cartimer
        self.entrietime = entrietime
        self.exittime = exittime
        self.lotnumber = lotnumber
        self.carpos = carpos
        self.colour = colour
        self.extra = extra
def spawncar():
    timer = random.randint(minparkdauer, maxparkdauer)
    starttime = time.time() # Zeitpunkt einfahrt
    endtime = starttime + timer # Zeitpunkt ausfahrt
    carcolour = random.choice(carcolours)  # zufällige autofarbe
    extra = situation()  # anspruch auf sonderparkplatz
    car = cars(timer, starttime, endtime, 0, (0, 0), carcolour, extra)
    if car.extra in extras:
        getextralot(car)
    else:
        car.lotnumber = random.randint(0, P)
    carsinlot.append(car)
    print(carsinlot)
    return
def situation():
    x = random.randint(0, 10) # je 10% chance auf anspruch für fimilien oder behinderten parkplatz
    if x == 0 or x == 1:
        extra = extras[x]
    else:
        extra = 'none'
    return extra
def getextralot(car):
    print('tbd', car)
    car.lotnumber = random.randint(0, P)
    return
def parkcar(car): # das auto parken
    maxParkplaetze = P
    reihe = car.lotnumber // maxplaetze_pro_reihe
    spalte = car.lotnumber & maxplaetze_pro_reihe
    if spalte == 0:
        spalte = 20
    else:
        reihe +=1
    #maxreihen = maxParkplaetze // maxplaetze_pro_reihe
    fahrrichtung = 1
    if reihe == 1:
        meinestrase = 2
        fahrrichtung = -1
        parkrichtung = -1
    elif reihe == 2:
        meinestrase = 1
        fahrrichtung = -1
        parkrichtung = 1
    elif reihe == 3:
        meinestrase = 1
        fahrrichtung = -1
        parkrichtung = 1
    elif reihe == 4:
        meinestrase = 0
        fahrrichtung = 0
        parkrichtung = 1
    elif reihe == 5:
        meinestrase = 1
        fahrrichtung = 1
        parkrichtung = 1
    x = xeinfahrt
    y = yeinfahrt
    thiscar = car.colour
    screen.blit(thiscar, (x, y))
    x += breite_Rand1
    screen.blit(thiscar, (x, y))
    pygame.transform.rotate(thiscar, -90 * fahrrichtung)
    ydrive = y + (breite_Straße + hohe_Parkplatz) * meinestrase * fahrrichtung
    xdrive = breite_Straße + breite_Rand1 + (breite_Parkplatz * spalte)
    while y != ydrive:
        y += fahrrichtung
        screen.blit(thiscar, (x, y))
    thiscar = pygame.transform.rotate(thiscar.convert_alpha(), 90 * fahrrichtung)
    while x != xdrive:
        x += 1
        screen.blit(thiscar, (x, y))
        whitecar.set_colorkey((255, 255, 255))
    thiscar = pygame.transform.rotate(thiscar, -90)
    y += hohe_Parkplatz * parkrichtung
    screen.blit(thiscar, (x, y))
    car.colour = thiscar
    car.carpos = (x, y)
    return car.carpos
def getcarout(car):
    reihe, spalte = Parkplatz_list[car.lotnumber]
    thiscar = car.colour
    y = breite_Straße * reihe + yeinfahrt
    x = breite_Parkplatz * spalte + xeinfahrt + einfahrtslaenge
    screen.blit(thiscar, (x, y))
    y -= hohe_Parkplatz
    screen.blit(thiscar, (x, y))
    thiscar = pygame.transform.rotate(thiscar, 90)
    screen.blit(thiscar, (x, y))
    while x < xausfahrt:
        x += 1
        screen.blit(thiscar, (x, y))
    while y > yausfahrt:
        y -= 1
        screen.blit(thiscar, (x, y))
    thiscar = pygame.transform.rotate(thiscar, 90)
    x += einfahrtslaenge
    screen.blit(thiscar, (x, y))
    car.carpos = (x, y)
    return car.carpos
def pay(car, oldrevenue):
    hours = car.cartimer//hins
    if hours < car.cartimer/hins:
        hours +=1
    amounttopay = hours * price
    print(f'You have to pay: {amounttopay} €')
    newrevenue = oldrevenue + amounttopay
    print(f'Your revenue is: {newrevenue} €')
    return newrevenue
def deletecar(car):
    carsinlot.remove(car)
    print('tbd', car)
    return

Parkplatz_list = []
go = True
while go:
    pygame.draw.rect(screen, (Schwarz), (x_anzeigefenster, y_anzeigefenster, breite_anzeigefenster, hohe_anzeigefenster))  # Anzeigefenster
    pygame.draw.rect(screen, (Schwarz), (x_Rand1, y_Rand1, breite_Rand1, hohe_Rand1))  # Rand links oben
    pygame.draw.rect(screen, (Schwarz), (x_Rand2, y_Rand2, breite_Rand2, hohe_Rand2))  # Rand links unten
    pygame.draw.rect(screen, (Schwarz), (x_zurückfenster, y_zurückfenster, breite_zurückfenster, hohe_zurückfenster))

    # Datum

    #date = str(date.today())
    date = '24.02.2023'

    def datum(msg='Datum: ' + date):
        my_font = pygame.font.Font(None, 40)
        text_surface = my_font.render(msg, True, Weiß)
        text_rect = text_surface.get_rect()
        text_rect.center = (1000, 15)
        screen.blit(text_surface, text_rect)

    # 5 Parkplätze
    if P >= 5:
        P1 = pygame.draw.rect(screen, (Weiß), (x_Parkplatz1, y_Parkplatz1, breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P1)
        P2 = pygame.draw.rect(screen, (Weiß), (x_Parkplatz1 + (breite_Parkplatz * 1 + 1), y_Parkplatz1, breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P2)
        P3 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 2 + 2), y_Parkplatz1, breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P3)
        P4 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 3 + 3), y_Parkplatz1, breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P4)
        P5 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 4 + 4), y_Parkplatz1, breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P5)
    # 10 Parkplätze
    if P >= 10:
        P6 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 5 + 5), y_Parkplatz1, breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P6)
        P7 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 6 + 6), y_Parkplatz1, breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P7)
        P8 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 7 + 7), y_Parkplatz1, breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P8)
        P9 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 8 + 8), y_Parkplatz1, breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P9)
        P10 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 9 + 9), y_Parkplatz1, breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P10)
    # 15 Parkplätze
    if P >= 15:
        P11 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 10 + 10), y_Parkplatz1, breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P11)
        P12 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 11 + 11), y_Parkplatz1, breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P12)
        P13 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 12 + 12), y_Parkplatz1, breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P13)
        P14 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 13 + 13), y_Parkplatz1, breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P14)
        P15 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 14 + 14), y_Parkplatz1, breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P15)
    # 20 Parkplätze
    if P >= 20:
        P16 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 15 + 15), y_Parkplatz1, breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P16)
        P17 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 16 + 16), y_Parkplatz1, breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P17)
        P18 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 17 + 17), y_Parkplatz1, breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P18)
        P19 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 18 + 18), y_Parkplatz1, breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P19)
        P20 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 19 + 19), y_Parkplatz1, breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P20)
    # 25 Parkplätze
    if P >= 25:
        P21 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1, y_Parkplatz1 - (breite_Straße + hohe_Parkplatz), breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P21)
        P22 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 1 + 1), y_Parkplatz1 - (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        Parkplatz_list.append(P22)
        P23 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 2 + 2), y_Parkplatz1 - (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        Parkplatz_list.append(P23)
        P24 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 3 + 3), y_Parkplatz1 - (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        Parkplatz_list.append(P24)
        P25 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 4 + 4), y_Parkplatz1 - (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        Parkplatz_list.append(P25)
    # 30 Parkplätze
    if P >= 30:
        P26 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 5 + 5), y_Parkplatz1 - (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        Parkplatz_list.append(P26)
        P27 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 6 + 6), y_Parkplatz1 - (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        Parkplatz_list.append(P27)
        P28 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 7 + 7), y_Parkplatz1 - (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        Parkplatz_list.append(P28)
        P29 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 8 + 8), y_Parkplatz1 - (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        Parkplatz_list.append(P29)
        P30 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 9 + 9), y_Parkplatz1 - (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        Parkplatz_list.append(P30)
    # 35 Parkplätze
    if P >= 35:
        P31 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 10 + 10), y_Parkplatz1 - (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        Parkplatz_list.append(P31)
        P32 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 11 + 11), y_Parkplatz1 - (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        Parkplatz_list.append(P32)
        P33 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 12 + 12), y_Parkplatz1 - (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        Parkplatz_list.append(P33)
        P34 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 13 + 13), y_Parkplatz1 - (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        Parkplatz_list.append(P34)
        P35 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 14 + 14), y_Parkplatz1 - (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        Parkplatz_list.append(P35)
    # 40 Parkplätze
    if P >= 40:
        P36 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 15 + 15), y_Parkplatz1 - (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        Parkplatz_list.append(P36)
        P37 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 16 + 16), y_Parkplatz1 - (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        Parkplatz_list.append(P37)
        P38 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 17 + 17), y_Parkplatz1 - (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        Parkplatz_list.append(P38)
        P39 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 18 + 18), y_Parkplatz1 - (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        Parkplatz_list.append(P39)
        P40 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 19 + 19), y_Parkplatz1 - (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        Parkplatz_list.append(P40)
    # 45 Parkplätze
    if P >= 45:
        P41 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1, y_Parkplatz1 + (breite_Straße + hohe_Parkplatz), breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P41)
        P42 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz), y_Parkplatz1 + (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        Parkplatz_list.append(P42)
        P43 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 2 + 2), y_Parkplatz1 + (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        Parkplatz_list.append(P43)
        P44 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 3 + 3), y_Parkplatz1 + (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        Parkplatz_list.append(P44)
        P45 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 4 + 4), y_Parkplatz1 + (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        Parkplatz_list.append(P45)
    # 50 Parkplätze
    if P >= 50:
        P46 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 5 + 5), y_Parkplatz1 + (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        Parkplatz_list.append(P46)
        P47 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 6 + 6), y_Parkplatz1 + (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        Parkplatz_list.append(P47)
        P48 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 7 + 7), y_Parkplatz1 + (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        Parkplatz_list.append(P48)
        P49 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 8 + 8), y_Parkplatz1 + (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        Parkplatz_list.append(P49)
        P50 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 9 + 9), y_Parkplatz1 + (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        Parkplatz_list.append(P50)
    # 55 Parkplätze
    if P >= 55:
        P51 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 10 + 10), y_Parkplatz1 + (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        Parkplatz_list.append(P51)
        P52 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 11 + 11), y_Parkplatz1 + (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        Parkplatz_list.append(P52)
        P53 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 12 + 12), y_Parkplatz1 + (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        Parkplatz_list.append(P53)
        P54 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 13 + 13), y_Parkplatz1 + (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        Parkplatz_list.append(P54)
        P55 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 14 + 14), y_Parkplatz1 + (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        Parkplatz_list.append(P55)
    # 60 Parkplätze
    if P >= 60:
        P56 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 15 + 15), y_Parkplatz1 + (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        Parkplatz_list.append(P56)
        P57 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 16 + 16), y_Parkplatz1 + (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        Parkplatz_list.append(P57)
        P58 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 17 + 17), y_Parkplatz1 + (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        Parkplatz_list.append(P58)
        P59 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 18 + 18), y_Parkplatz1 + (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        Parkplatz_list.append(P59)
        P60 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 19 + 19), y_Parkplatz1 + (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        Parkplatz_list.append(P60)
    # 65 Parkplätze
    if P >= 65:
        P61 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1, y_Parkplatz1 + (breite_Straße * 2 + hohe_Parkplatz * 2), breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P61)
        P62 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz), y_Parkplatz1 + (breite_Straße * 2 + hohe_Parkplatz * 2), breite_Parkplatz,
        hohe_Parkplatz), 2)
        Parkplatz_list.append(P62)
        P63 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 2 + 2), y_Parkplatz1 + (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P63)
        P64 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 3 + 3), y_Parkplatz1 + (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P64)
        P65 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 4 + 4), y_Parkplatz1 + (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P65)
    # 70 Parkplätze
    if P >= 70:
        P66 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 5 + 5), y_Parkplatz1 + (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P66)
        P67 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 6 + 6), y_Parkplatz1 + (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P67)
        P68 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 7 + 7), y_Parkplatz1 + (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P68)
        P69 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 8 + 8), y_Parkplatz1 + (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P69)
        P70 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 9 + 9), y_Parkplatz1 + (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P70)
    # 75 Parkplätze
    if P >= 75:
        P71 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 10 + 10), y_Parkplatz1 + (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P71)
        P72 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 11 + 11), y_Parkplatz1 + (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P72)
        P73 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 12 + 12), y_Parkplatz1 + (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P73)
        P74 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 13 + 13), y_Parkplatz1 + (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P74)
        P75 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 14 + 14), y_Parkplatz1 + (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P75)
    # 80 Parkplätze
    if P >= 80:
        P76 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 15 + 15), y_Parkplatz1 + (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P76)
        P77 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 16 + 16), y_Parkplatz1 + (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P77)
        P78 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 17 + 17), y_Parkplatz1 + (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P78)
        P79 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 18 + 18), y_Parkplatz1 + (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P79)
        P80 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 19 + 19), y_Parkplatz1 + (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P80)
    # 85 Parkplätze
    if P >= 85:
        P81 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1, y_Parkplatz1 - (breite_Straße * 2 + hohe_Parkplatz * 2), breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P81)
        P82 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz), y_Parkplatz1 - (breite_Straße * 2 + hohe_Parkplatz * 2), breite_Parkplatz,
        hohe_Parkplatz), 2)
        Parkplatz_list.append(P82)
        P83 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 2 + 2), y_Parkplatz1 - (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P83)
        P84 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 3 + 3), y_Parkplatz1 - (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P84)
        P85 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 4 + 4), y_Parkplatz1 - (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P85)
    # 90 Parkplätze
    if P >= 90:
        P86 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 5 + 5), y_Parkplatz1 - (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P86)
        P87 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 6 + 6), y_Parkplatz1 - (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P87)
        P88 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 7 + 7), y_Parkplatz1 - (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P88)
        P89 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 8 + 8), y_Parkplatz1 - (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P89)
        P90 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 9 + 9), y_Parkplatz1 - (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P90)
    # 95 Parkplätze
    if P >= 95:
        P91 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 10 + 10), y_Parkplatz1 - (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P91)
        P92 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 11 + 11), y_Parkplatz1 - (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P92)
        P93 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 12 + 12), y_Parkplatz1 - (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P93)
        P94 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 13 + 13), y_Parkplatz1 - (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P94)
        P95 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 14 + 14), y_Parkplatz1 - (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P95)
    # 100 Parkplätze
    if P >= 100:
        P96 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 15 + 15), y_Parkplatz1 - (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P96)
        P97 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 16 + 16), y_Parkplatz1 - (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P97)
        P98 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 17 + 17), y_Parkplatz1 - (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P98)
        P99 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 18 + 18), y_Parkplatz1 - (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P99)
        P100 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 19 + 19), y_Parkplatz1 - (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(P100)
    go = False
    pygame.display.update()

running = True
while running == True:
    now = time.time()
    secounds = now - starttime
    if len(carsinlot) == P:
        print('The parkinglot is full!')
    else:
        if secounds > carspawntime:
            carspawntime = random.randint(3, 8)
            starttime = time.time()
            spawncar()
            carcounter += 1
            car = carsinlot[-1]
            screen.blit(car.colour, parkcar(car))
    for i in carsinlot:
        print(i.cartimer, i.lotnumber, i.carpos, i.colour, i.extra)
        currenttime = time.time()
        screen.blit(i.colour, i.carpos)
        if currenttime > i.exittime:
            screen.blit(i.colour, getcarout(i))
            pay(i, revenue)
            deletecar(i)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    pygame.display.update()