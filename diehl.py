import time
import random
import pygame
from pygame.locals import *
import datetime
import pygame
from datetime import date
import sys
pygame.init()

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

reihenabstand = breite_Straße
platzabstand = breite_Parkplatz
parkplatzlaenge = hohe_Parkplatz
einfahrtslaenge = 40
xeinfahrt = 50
yeinfahrt = 300
xausfahrt = 600
yausfahrt = 300

#bildeinstellungen
whitecar = pygame.image.load('whitecar.jpg')
whitecar = pygame.transform.scale(whitecar, carsize)
whitecar = pygame.transform.rotate(whitecar, 180)
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
        car.lotnumber = random.randint(0, lotcount)
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
    car.lotnumber = random.randint(0, lotcount)
    return
def parkcar(car): # das auto parken
    pygame.display.update()
    reihe = car.lotnumber// 15
    spalte = car.lotnumber - reihe * 15
    x = xeinfahrt
    y = yeinfahrt
    thiscar = car.colour
    screen.blit(thiscar, (x, y))
    x += einfahrtslaenge
    screen.blit(thiscar, (x, y))
    thiscar = pygame.transform.rotate(thiscar, -90)
    ydrive = reihenabstand * reihe + y
    xdrive = platzabstand * spalte + x
    while y < ydrive:
        y += 1
        screen.blit(thiscar, (x, y))
        pygame.display.update()
    thiscar = pygame.transform.rotate(thiscar, 90)
    while x < xdrive:
        x += 1
        screen.blit(thiscar, (x, y))
        pygame.display.update()
    thiscar = pygame.transform.rotate(thiscar, -90)
    y += parkplatzlaenge
    screen.blit(thiscar, (x, y))
    pygame.display.update()
    car.colour = thiscar
    car.carpos = (x, y)
    return car.carpos

def getcarout(car):
    reihe, spalte = Parkplatz_list[car.lotnumber]
    thiscar = car.colour
    y = reihenabstand * reihe + yeinfahrt
    x = platzabstand * spalte + xeinfahrt + einfahrtslaenge
    screen.blit(thiscar, (x, y))
    pygame.display.update()
    y -= parkplatzlaenge
    screen.blit(thiscar, (x, y))
    pygame.display.update()
    thiscar = pygame.transform.rotate(thiscar, 90)
    screen.blit(thiscar, (x, y))
    pygame.display.update()
    while x < xausfahrt:
        x += 1
        screen.blit(thiscar, (x, y))
        pygame.display.update()
    while y > yausfahrt:
        y -= 1
        screen.blit(thiscar, (x, y))
        pygame.display.update()
    thiscar = pygame.transform.rotate(thiscar, 90)
    x += einfahrtslaenge
    screen.blit(thiscar, (x, y))
    pygame.display.update()
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
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    pygame.draw.rect(screen, (Schwarz),
                     (x_anzeigefenster, y_anzeigefenster, breite_anzeigefenster, hohe_anzeigefenster))  # Anzeigefenster
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
        P2 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 1 + 1), y_Parkplatz1, breite_Parkplatz, hohe_Parkplatz), 2)
        P3 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 2 + 2), y_Parkplatz1, breite_Parkplatz, hohe_Parkplatz), 2)
        P4 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 3 + 3), y_Parkplatz1, breite_Parkplatz, hohe_Parkplatz), 2)
        P5 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 4 + 4), y_Parkplatz1, breite_Parkplatz, hohe_Parkplatz), 2)

    # 10 Parkplätze
    if P >= 10:
        P6 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 5 + 5), y_Parkplatz1, breite_Parkplatz, hohe_Parkplatz), 2)
        P7 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 6 + 6), y_Parkplatz1, breite_Parkplatz, hohe_Parkplatz), 2)
        P8 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 7 + 7), y_Parkplatz1, breite_Parkplatz, hohe_Parkplatz), 2)
        P9 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 8 + 8), y_Parkplatz1, breite_Parkplatz, hohe_Parkplatz), 2)
        P10 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 9 + 9), y_Parkplatz1, breite_Parkplatz, hohe_Parkplatz), 2)

    # 15 Parkplätze
    if P >= 15:
        P11 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 10 + 10), y_Parkplatz1, breite_Parkplatz, hohe_Parkplatz), 2)
        P12 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 11 + 11), y_Parkplatz1, breite_Parkplatz, hohe_Parkplatz), 2)
        P13 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 12 + 12), y_Parkplatz1, breite_Parkplatz, hohe_Parkplatz), 2)
        P14 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 13 + 13), y_Parkplatz1, breite_Parkplatz, hohe_Parkplatz), 2)
        P15 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 14 + 14), y_Parkplatz1, breite_Parkplatz, hohe_Parkplatz), 2)

    # 20 Parkplätze
    if P >= 20:
        P16 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 15 + 15), y_Parkplatz1, breite_Parkplatz, hohe_Parkplatz), 2)
        P17 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 16 + 16), y_Parkplatz1, breite_Parkplatz, hohe_Parkplatz), 2)
        P18 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 17 + 17), y_Parkplatz1, breite_Parkplatz, hohe_Parkplatz), 2)
        P19 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 18 + 18), y_Parkplatz1, breite_Parkplatz, hohe_Parkplatz), 2)
        P20 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 19 + 19), y_Parkplatz1, breite_Parkplatz, hohe_Parkplatz), 2)

    # 25 Parkplätze
    if P >= 25:
        P21 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1, y_Parkplatz1 - (breite_Straße + hohe_Parkplatz), breite_Parkplatz, hohe_Parkplatz), 2)
        P22 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 1 + 1), y_Parkplatz1 - (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        P23 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 2 + 2), y_Parkplatz1 - (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        P24 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 3 + 3), y_Parkplatz1 - (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        P25 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 4 + 4), y_Parkplatz1 - (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)

    # 30 Parkplätze
    if P >= 30:
        P26 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 5 + 5), y_Parkplatz1 - (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        P27 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 6 + 6), y_Parkplatz1 - (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        P28 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 7 + 7), y_Parkplatz1 - (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        P29 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 8 + 8), y_Parkplatz1 - (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        P30 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 9 + 9), y_Parkplatz1 - (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)

    # 35 Parkplätze
    if P >= 35:
        P31 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 10 + 10), y_Parkplatz1 - (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        P32 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 11 + 11), y_Parkplatz1 - (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        P33 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 12 + 12), y_Parkplatz1 - (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        P34 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 13 + 13), y_Parkplatz1 - (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        P35 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 14 + 14), y_Parkplatz1 - (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)

    # 40 Parkplätze
    if P >= 40:
        P36 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 15 + 15), y_Parkplatz1 - (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        P37 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 16 + 16), y_Parkplatz1 - (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        P38 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 17 + 17), y_Parkplatz1 - (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        P39 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 18 + 18), y_Parkplatz1 - (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        P40 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 19 + 19), y_Parkplatz1 - (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)

    # 45 Parkplätze
    if P >= 45:
        P41 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1, y_Parkplatz1 + (breite_Straße + hohe_Parkplatz), breite_Parkplatz, hohe_Parkplatz), 2)
        P42 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz), y_Parkplatz1 + (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        P43 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 2 + 2), y_Parkplatz1 + (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        P44 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 3 + 3), y_Parkplatz1 + (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        P45 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 4 + 4), y_Parkplatz1 + (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)

    # 50 Parkplätze
    if P >= 50:
        P46 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 5 + 5), y_Parkplatz1 + (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        P47 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 6 + 6), y_Parkplatz1 + (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        P48 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 7 + 7), y_Parkplatz1 + (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        P49 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 8 + 8), y_Parkplatz1 + (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        P50 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 9 + 9), y_Parkplatz1 + (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)

    # 55 Parkplätze
    if P >= 55:
        P51 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 10 + 10), y_Parkplatz1 + (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        P52 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 11 + 11), y_Parkplatz1 + (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        P53 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 12 + 12), y_Parkplatz1 + (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        P54 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 13 + 13), y_Parkplatz1 + (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        P55 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 14 + 14), y_Parkplatz1 + (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)

    # 60 Parkplätze
    if P >= 60:
        P56 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 15 + 15), y_Parkplatz1 + (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        P57 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 16 + 16), y_Parkplatz1 + (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        P58 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 17 + 17), y_Parkplatz1 + (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        P59 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 18 + 18), y_Parkplatz1 + (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)
        P60 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 19 + 19), y_Parkplatz1 + (breite_Straße + hohe_Parkplatz), breite_Parkplatz,
        hohe_Parkplatz), 2)

    # 65 Parkplätze
    if P >= 65:
        P61 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1, y_Parkplatz1 + (breite_Straße * 2 + hohe_Parkplatz * 2), breite_Parkplatz, hohe_Parkplatz), 2)
        P62 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz), y_Parkplatz1 + (breite_Straße * 2 + hohe_Parkplatz * 2), breite_Parkplatz,
        hohe_Parkplatz), 2)
        P63 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 2 + 2), y_Parkplatz1 + (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        P64 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 3 + 3), y_Parkplatz1 + (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        P65 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 4 + 4), y_Parkplatz1 + (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)

    # 70 Parkplätze
    if P >= 70:
        P66 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 5 + 5), y_Parkplatz1 + (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        P67 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 6 + 6), y_Parkplatz1 + (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        P68 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 7 + 7), y_Parkplatz1 + (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        P69 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 8 + 8), y_Parkplatz1 + (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        P70 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 9 + 9), y_Parkplatz1 + (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)

    # 75 Parkplätze
    if P >= 75:
        P71 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 10 + 10), y_Parkplatz1 + (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        P72 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 11 + 11), y_Parkplatz1 + (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        P73 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 12 + 12), y_Parkplatz1 + (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        P74 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 13 + 13), y_Parkplatz1 + (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        P75 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 14 + 14), y_Parkplatz1 + (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)

    # 80 Parkplätze
    if P >= 80:
        P76 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 15 + 15), y_Parkplatz1 + (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        P77 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 16 + 16), y_Parkplatz1 + (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        P78 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 17 + 17), y_Parkplatz1 + (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        P79 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 18 + 18), y_Parkplatz1 + (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        P80 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 19 + 19), y_Parkplatz1 + (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)

    # 85 Parkplätze
    if P >= 85:
        P81 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1, y_Parkplatz1 - (breite_Straße * 2 + hohe_Parkplatz * 2), breite_Parkplatz, hohe_Parkplatz), 2)
        P82 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz), y_Parkplatz1 - (breite_Straße * 2 + hohe_Parkplatz * 2), breite_Parkplatz,
        hohe_Parkplatz), 2)
        P83 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 2 + 2), y_Parkplatz1 - (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        P84 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 3 + 3), y_Parkplatz1 - (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        P85 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 4 + 4), y_Parkplatz1 - (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)

    # 90 Parkplätze
    if P >= 90:
        P86 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 5 + 5), y_Parkplatz1 - (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        P87 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 6 + 6), y_Parkplatz1 - (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        P88 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 7 + 7), y_Parkplatz1 - (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        P89 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 8 + 8), y_Parkplatz1 - (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        P90 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 9 + 9), y_Parkplatz1 - (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)

    # 95 Parkplätze
    if P >= 95:
        P91 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 10 + 10), y_Parkplatz1 - (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        P92 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 11 + 11), y_Parkplatz1 - (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        P93 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 12 + 12), y_Parkplatz1 - (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        P94 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 13 + 13), y_Parkplatz1 - (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        P95 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 14 + 14), y_Parkplatz1 - (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)

    # 100 Parkplätze
    if P >= 100:
        P96 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 15 + 15), y_Parkplatz1 - (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        P97 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 16 + 16), y_Parkplatz1 - (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        P98 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 17 + 17), y_Parkplatz1 - (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        P99 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 18 + 18), y_Parkplatz1 - (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)
        P100 = pygame.draw.rect(screen, (Weiß), (
        x_Parkplatz1 + (breite_Parkplatz * 19 + 19), y_Parkplatz1 - (breite_Straße * 2 + hohe_Parkplatz * 2),
        breite_Parkplatz, hohe_Parkplatz), 2)

    go = False

    pygame.display.update()
# Parkplatz Koordinaten in Liste speichern
list = True
while list:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # 5 Parkplätze
    if P >= 5:
        Parkplatz_list.append(P1)
        Parkplatz_list.append(P2)
        Parkplatz_list.append(P3)
        Parkplatz_list.append(P4)
        Parkplatz_list.append(P5)
    # 10 Parkplätze
    if P >= 10:
        Parkplatz_list.append(P6)
        Parkplatz_list.append(P7)
        Parkplatz_list.append(P8)
        Parkplatz_list.append(P9)
        Parkplatz_list.append(P10)
    # 15 Parkplätze
    if P >= 15:
        Parkplatz_list.append(P11)
        Parkplatz_list.append(P12)
        Parkplatz_list.append(P13)
        Parkplatz_list.append(P14)
        Parkplatz_list.append(P15)
    # 20 Parkplätze
    if P >= 20:
        Parkplatz_list.append(P16)
        Parkplatz_list.append(P17)
        Parkplatz_list.append(P18)
        Parkplatz_list.append(P19)
        Parkplatz_list.append(P20)
    # 25 Parkplätze
    if P >= 25:
        Parkplatz_list.append(P21)
        Parkplatz_list.append(P22)
        Parkplatz_list.append(P23)
        Parkplatz_list.append(P24)
        Parkplatz_list.append(P25)
    # 30 Parkplätze
    if P >= 30:
        Parkplatz_list.append(P26)
        Parkplatz_list.append(P27)
        Parkplatz_list.append(P28)
        Parkplatz_list.append(P29)
        Parkplatz_list.append(P30)
    # 35 Parkplätze
    if P >= 35:
        Parkplatz_list.append(P31)
        Parkplatz_list.append(P32)
        Parkplatz_list.append(P33)
        Parkplatz_list.append(P34)
        Parkplatz_list.append(P35)
    # 40 Parkplätze
    if P >= 40:
        Parkplatz_list.append(P36)
        Parkplatz_list.append(P37)
        Parkplatz_list.append(P38)
        Parkplatz_list.append(P39)
        Parkplatz_list.append(P40)
    # 45 Parkplätze
    if P >= 45:
        Parkplatz_list.append(P41)
        Parkplatz_list.append(P42)
        Parkplatz_list.append(P43)
        Parkplatz_list.append(P44)
        Parkplatz_list.append(P45)
    # 50 Parkplätze
    if P >= 50:
        Parkplatz_list.append(P46)
        Parkplatz_list.append(P47)
        Parkplatz_list.append(P48)
        Parkplatz_list.append(P49)
        Parkplatz_list.append(P50)
    # 55 Parkplätze
    if P >= 55:
        Parkplatz_list.append(P51)
        Parkplatz_list.append(P52)
        Parkplatz_list.append(P53)
        Parkplatz_list.append(P54)
        Parkplatz_list.append(P55)
    # 60 Parkplätze
    if P >= 60:
        Parkplatz_list.append(P56)
        Parkplatz_list.append(P57)
        Parkplatz_list.append(P58)
        Parkplatz_list.append(P59)
        Parkplatz_list.append(P60)
    # 65 Parkplätze
    if P >= 65:
        Parkplatz_list.append(P61)
        Parkplatz_list.append(P62)
        Parkplatz_list.append(P63)
        Parkplatz_list.append(P64)
        Parkplatz_list.append(P65)
    # 70 Parkplätze
    if P >= 70:
        Parkplatz_list.append(P66)
        Parkplatz_list.append(P67)
        Parkplatz_list.append(P68)
        Parkplatz_list.append(P69)
        Parkplatz_list.append(P70)
    # 75 Parkplätz
    if P >= 75:
        Parkplatz_list.append(P71)
        Parkplatz_list.append(P72)
        Parkplatz_list.append(P73)
        Parkplatz_list.append(P74)
        Parkplatz_list.append(P75)
    # 80 Parkplätze
    if P >= 80:
        Parkplatz_list.append(P76)
        Parkplatz_list.append(P77)
        Parkplatz_list.append(P78)
        Parkplatz_list.append(P79)
        Parkplatz_list.append(P80)
    # 85 Parkplätze
    if P >= 85:
        Parkplatz_list.append(P81)
        Parkplatz_list.append(P82)
        Parkplatz_list.append(P83)
        Parkplatz_list.append(P84)
        Parkplatz_list.append(P85)
    # 90 Parkplätze
    if P >= 90:
        Parkplatz_list.append(P86)
        Parkplatz_list.append(P87)
        Parkplatz_list.append(P88)
        Parkplatz_list.append(P89)
        Parkplatz_list.append(P90)
    # 95 Parkplätze
    if P >= 95:
        Parkplatz_list.append(P91)
        Parkplatz_list.append(P92)
        Parkplatz_list.append(P93)
        Parkplatz_list.append(P94)
        Parkplatz_list.append(P95)
    # 100 Parkplätze
    if P >= 100:
        Parkplatz_list.append(P96)
        Parkplatz_list.append(P97)
        Parkplatz_list.append(P98)
        Parkplatz_list.append(P99)
        Parkplatz_list.append(P100)

    list = False
    print(Parkplatz_list)
    pygame.display.update()

#variable parkplatzbelegung
lotcount = len(Parkplatz_list)

running = True
while running == True:
    now = time.time()
    secounds = now - starttime
    if len(carsinlot) == lotcount:
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