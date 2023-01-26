import time
import random
import pygame
from pygame.locals import *
import datetime
import pygame
from datetime import date
import sys

black = (0, 0, 0)
grey = (127, 127, 127)
white = (255, 255, 255)
P = 100  # Parkplatzanzahl
breite_screen = 1250
hohe_screen = 530

pygame.init()
screen = pygame.display.set_mode((breite_screen, hohe_screen))
screen.fill(grey)
# Koordinaten Anzeigefenster
x_anzeigefenster = 1000
y_anzeigefenster = 0
breite_anzeigefenster = 300
hohe_anzeigefenster = 410

# Koordinaten Zurückfenster
x_zurückfenster = 1000
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

# Parkplatz maße
hohe_Parkplatz = 60
breite_Parkplatz = 40
breite_Straße = 50
x_Parkplatz1 = breite_Straße + breite_Rand1
y_Parkplatz1 = 240

# variable auto
carspawntime = random.randint(3, 5)
carsinlot = []
starttime = time.time()
carcolours = []
extras = ['family', 'handycaped']
carcounter = 1
carsize = (60, 30)
lcarsize, bcarsize = carsize

# variable bezahlung
price = 8  # Preis pro h in €
revenue = 0
# variable parkdauer
hins = 3600  # StundeinSekunde(3600)
minparkdauer = 10  # 900 = 15 min in s
maxparkdauer = 30  # 43200 = 12h in s

# variable parken
maxplaetze_pro_reihe = 20
einfahrtslaenge = breite_Rand1
xeinfahrt = 0
yeinfahrt = (y_Rand1 + hohe_Rand1) + (y_Rand2 - (y_Rand1 + hohe_Rand1)) / 2 - bcarsize / 2
belegt = []
belegtextra = []
Parkplatz_list = []

# bildeinstellungen
whitecar = pygame.image.load('whitecar.jpg')
whitecar = pygame.transform.scale(whitecar, carsize)
whitecar = pygame.transform.rotate(whitecar, 180)
carcolours.append(whitecar)


class cars:
    def __init__(self, cartimer, entrietime, exittime, lotnumber, carpos, image, extra):
        self.cartimer = cartimer
        self.entrietime = entrietime
        self.exittime = exittime
        self.lotnumber = lotnumber
        self.carpos = carpos
        self.image = image
        self.extra = extra


def spawncar():
    global carsinlot
    timer = random.randint(minparkdauer, maxparkdauer)
    starttime = time.time()  # Zeitpunkt einfahrt
    endtime = starttime + timer  # Zeitpunkt ausfahrt
    carimage = random.choice(carcolours)  # zufällige autofarbe
    extra = situation()  # anspruch auf sonderparkplatz
    car = cars(timer, starttime, endtime, 0, (0, 0), carimage, extra)
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
    x = random.randint(0, 10)  # je 10% chance auf anspruch für fimilien oder behinderten parkplatz
    if x == 0 or x == 1:
        extra = extras[x]
    else:
        extra = 'none'
    return extra


def getextralot(get_car):
    print('tbd', get_car.extra)
    get_car.lotnumber = random.randint(0, P)
    belegt.append(get_car.lotnumber)
    return


def howtodrive(get_car):
    global meinestrase, parkrichtung
    reihe = get_car.lotnumber // maxplaetze_pro_reihe
    # print(reihe, car.lotnumber, maxplaetze_pro_reihe)
    spalte = get_car.lotnumber % maxplaetze_pro_reihe
    if spalte == 0:
        spalte = 20
        if reihe != 0:
            reihe -= 1
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
    print(reihe, spalte)
    return reihe, spalte, meinestrase, fahrrichtung, parkrichtung


def parkcar(get_car):  # das auto parken
    self = get_car.image
    self_rect = self.get_rect()
    reihe, spalte, meinestrase, fahrrichtung, parkrichtung = howtodrive(get_car)
    self_rect.x = xeinfahrt
    self_rect.y = yeinfahrt
    screen.blit(self, self_rect)
    self_rect.x += breite_Rand1 + breite_Straße // 2 - bcarsize // 2
    screen.blit(self, self_rect)
    self = pygame.transform.rotate(self, -90 * fahrrichtung)
    print(-90 * fahrrichtung)
    ydrive = self_rect.y + (breite_Straße + hohe_Parkplatz) * meinestrase * fahrrichtung
    xdrive = self_rect.x + breite_Straße // 2 + (bcarsize * 2) // 3 + (breite_Parkplatz + 3) * (spalte - 1)
    while self_rect.y != ydrive:
        self_rect.y += fahrrichtung
        genbackground()
        screen.blit(self, self_rect)
    self = pygame.transform.rotate(self, 90 * fahrrichtung)
    while self_rect.x != xdrive:
        self_rect.x += 1
        genbackground()
        screen.blit(self, self_rect)
    self = pygame.transform.rotate(self, -90)
    self_rect.y += (hohe_Parkplatz - lcarsize // 2 + breite_Straße // 2) * parkrichtung - bcarsize // 2
    genbackground()
    screen.blit(self, self_rect)
    return (self_rect.x, self_rect.y), self


def getcarout(get_car):
    self = get_car.image
    self_rect = self.get_rect()
    reihe, spalte, meinestrase, fahrrichtung, parkrichtung = howtodrive(get_car)
    self_rect.x, self_rect.y = get_car.carpos
    screen.blit(self, self_rect)
    self_rect.y -= hohe_Parkplatz * parkrichtung
    genbackground()
    screen.blit(self, self_rect)
    self = pygame.transform.rotate(self, 90 * parkrichtung)
    xausfahrt = (breite_Parkplatz + 3) * (maxplaetze_pro_reihe - spalte) + breite_Straße // 2
    yausfahrt = (breite_Straße + hohe_Parkplatz) * meinestrase * -1 * fahrrichtung
    xfahrt = breite_screen - lcarsize
    while self_rect.x != xausfahrt:
        self_rect.x += 1
        genbackground()
        screen.blit(self, self_rect)
    self = pygame.transform.rotate(self, 90 * fahrrichtung)
    while self_rect.y != yausfahrt:
        self_rect.y -= fahrrichtung
        genbackground()
        screen.blit(self, self_rect)
    self = pygame.transform.rotate(self, 90 * fahrrichtung)
    while self_rect.x != xfahrt:
        self_rect.x += 1
        genbackground()
        screen.blit(self, self_rect)
    return (self_rect.x, self_rect.y), self


def pay(car, oldrevenue):
    hours = car.cartimer // hins
    if hours < car.cartimer / hins:
        hours += 1
    amounttopay = hours * price
    print(f'You have to pay: {amounttopay} €')
    newrevenue = oldrevenue + amounttopay
    print(f'Your revenue is: {newrevenue} €')
    return newrevenue


def deletecar(car):
    belegt.remove(car.lotnumber)
    print(carsinlot, car)
    carsinlot.remove(car)
    print('tbd - delete', car)
    return


def genscreen():
    screen = pygame.display.set_mode((breite_screen, hohe_screen))
    screen.fill(grey)


def genrand():
    pygame.draw.rect(screen, black,
                     (x_anzeigefenster, y_anzeigefenster, breite_anzeigefenster, hohe_anzeigefenster))  # Anzeigefenster
    pygame.draw.rect(screen, black, (x_Rand1, y_Rand1, breite_Rand1, hohe_Rand1))  # Rand links oben
    pygame.draw.rect(screen, black, (x_Rand2, y_Rand2, breite_Rand2, hohe_Rand2))  # Rand links unten
    pygame.draw.rect(screen, black, (x_zurückfenster, y_zurückfenster, breite_zurückfenster, hohe_zurückfenster))


# Datum
date = str(date.today())


def datum(msg='Datum: ' + date):
    my_font = pygame.font.Font(None, 35)
    text_surface = my_font.render(msg, True, white)
    text_rect = text_surface.get_rect()
    text_rect.center = (1125, 15)
    screen.blit(text_surface, text_rect)


def genParkplaetze():
    Parkplatz_list = []
    x = 0
    y = 0
    z = 0
    for i in range(100):
        z += 1
        Px = pygame.draw.rect(screen, white, (
            x_Parkplatz1 + (breite_Parkplatz + 3) * x, y_Parkplatz1 - y, breite_Parkplatz, hohe_Parkplatz), 2)
        Parkplatz_list.append(Px)
        x += 1
        if x == maxplaetze_pro_reihe:
            x = 0
        if z == 40 or z == 80 or z == 60:
            y *= -1
        if z == 20 or z == 60:
            y += breite_Straße + hohe_Parkplatz

def genbackground():
    genscreen()
    genrand()
    genParkplaetze()
    datum()


# main-loop
running = True
genbackground()
while running == True:
    now = time.time()
    secounds = now - starttime
    if len(carsinlot) == P:
        print('The parkinglot is full!')
    else:
        if secounds > carspawntime:
            carspawntime = random.randint(1, 3)
            starttime = time.time()
            spawncar()
            carcounter += 1
            car = carsinlot[-1]
            car.carpos, car.image = parkcar(car)
    pygame.display.update()
    for i in carsinlot:
        print(i.cartimer, i.lotnumber, i.carpos, i.image, i.extra)
        currenttime = time.time()
        screen.blit(i.image, i.carpos)
        if currenttime > i.exittime:
            i.carpos, i.image = getcarout(i)
            pay(i, revenue)
            deletecar(i)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    pygame.display.update()
