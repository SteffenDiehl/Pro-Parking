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
lcarsize, bcarsize = carsize
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
yeinfahrt = (y_Rand1 + hohe_Rand1) + (y_Rand2 - (y_Rand1 + hohe_Rand1))/2 - bcarsize/2
xausfahrt = 600
yausfahrt = 300
belegt = []
belegtextra = []
Parkplatz_list = []

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
        while True:
            car.lotnumber = random.randint(0, P)
            if car.lotnumber not in belegt:
                belegt.append(car.lotnumber)
                break
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
    reihe = car.lotnumber // maxplaetze_pro_reihe
    print(reihe, car.lotnumber, maxplaetze_pro_reihe)
    spalte = car.lotnumber % maxplaetze_pro_reihe
    thiscar = car.colour
    thiscar_rect = thiscar.get_rect()
    if spalte == 0:
        spalte = 19
        reihe -=1
    fahrrichtung = 1
    if reihe == 0:
        meinestrase = 2
        fahrrichtung = -1
        parkrichtung = -1
    elif reihe == 1:
        meinestrase = 1
        fahrrichtung = -1
        parkrichtung = -1
    elif reihe == 2:
        meinestrase = 1
        fahrrichtung = -1
        parkrichtung = 1
    elif reihe == 3:
        meinestrase = 0
        fahrrichtung = 0
        parkrichtung = 1
    elif reihe == 4:
        meinestrase = 1
        fahrrichtung = 1
        parkrichtung = 1
    thiscar_rect.x = xeinfahrt
    thiscar_rect.y = yeinfahrt
    screen.blit(thiscar, thiscar_rect)
    thiscar_rect.x += breite_Rand1 + breite_Straße/2 -bcarsize/2
    screen.blit(thiscar, thiscar_rect)
    thiscar = pygame.transform.rotate(thiscar, -90 * fahrrichtung)
    print(-90 * fahrrichtung)
    ydrive = thiscar_rect.y + (breite_Straße + hohe_Parkplatz) * meinestrase * fahrrichtung
    xdrive = thiscar_rect.x + breite_Straße/2 + (bcarsize*2)/3 + (breite_Parkplatz + 3) * (spalte-1)
    while thiscar_rect.y != ydrive:
        thiscar_rect.y += fahrrichtung
        genbackground()
        screen.blit(thiscar, thiscar_rect)
    thiscar = pygame.transform.rotate(thiscar, 90 * fahrrichtung)
    while thiscar_rect.x != xdrive:
        thiscar_rect.x += 1
        genbackground()
        screen.blit(thiscar, thiscar_rect)
    thiscar = pygame.transform.rotate(thiscar, -90)
    thiscar_rect.y += (hohe_Parkplatz - lcarsize/2 + breite_Straße/2)* parkrichtung - bcarsize/2
    screen.blit(thiscar, thiscar_rect)
    return (thiscar_rect.x, thiscar_rect.y), thiscar
def getcarout(car):
    thiscar = car.colour
    thiscar_rect = thiscar.get_rect()
    thiscar_rect.x, thiscar_rect.y = car.carpos
    screen.blit(thiscar, thiscar_rect)
    thiscar_rect.y -= hohe_Parkplatz
    screen.blit(thiscar, thiscar_rect)
    thiscar = pygame.transform.rotate(thiscar, 90)
    screen.blit(thiscar, thiscar_rect)
    while thiscar_rect.x < xausfahrt:
        thiscar_rect.x += 1
        screen.blit(thiscar, thiscar_rect)
    while thiscar_rect.y > yausfahrt:
        thiscar_rect.y -= 1
        screen.blit(thiscar, thiscar_rect)
    thiscar = pygame.transform.rotate(thiscar, 90)
    thiscar_rect.x += einfahrtslaenge
    screen.blit(thiscar, thiscar_rect)
    return (thiscar_rect.x, thiscar_rect.y), thiscar
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
    belegt.remove(car.lotnumber)
    carsinlot.remove(car)
    print('tbd', car)
    return
def genscreen():
    screen = pygame.display.set_mode((breite_screen, hohe_screen))
    screen.fill(Grau)
def genrand():
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

def genParkplaetze():
    Parkplatz_list = []
    x = 0
    y = 0
    z = 0
    for i in range(100):
        z += 1
        Px = pygame.draw.rect(screen, Weiß, (
            x_Parkplatz1 + (breite_Parkplatz +3) *x, y_Parkplatz1 -y, breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(Px)
        x += 1
        if x == maxplaetze_pro_reihe -1:
            x = 0
        if z == 39 or z ==79 or z == 59:
            y *= -1
        if z == 19  or z == 59:
            y += breite_Straße + hohe_Parkplatz
def genbackground():
    genscreen()
    genrand()
    genParkplaetze()
running = True
while running == True:
    genbackground()
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
            car.carpos, car.colour = parkcar(car)
    for i in carsinlot:
        print(i.cartimer, i.lotnumber, i.carpos, i.colour, i.extra)
        currenttime = time.time()
        screen.blit(i.colour, i.carpos)
        if currenttime > i.exittime:
            i.carpos, i.colour = getcarout()
            screen.blit(i.colour, i.carpos)
            pay(i, revenue)
            deletecar(i)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    pygame.display.update()