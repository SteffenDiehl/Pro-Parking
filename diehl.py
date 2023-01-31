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
carsinlot = []
starttime = time.time()
carcolours = []
extras = ['family', 'handycaped']
carcounter = 1
carsize = (60, 30)
lcarsize, bcarsize = carsize
autobilder = ['whitecar.jpg', 'redcar.png']
# variable bezahlung
price = 8  # Preis pro h in €
revenue = 0
# variable parkdauer
zeittraffer = 30
hins = 3600  # StundeinSekunde(3600)
minparkdauer = hins/4 # 15 min in s
maxparkdauer = 12 * hins # 12h in s
#variable spawntime
minspawntime = hins/60 # min 1 min zwischen spawns
maxspawntime = 5*(hins/60) # max 5 min zwischen spawns

# variable parken
maxplaetze_pro_reihe = 20
einfahrtslaenge = breite_Rand1
xeinfahrt = 0
yeinfahrt = (y_Rand1 + hohe_Rand1) + (y_Rand2 - (y_Rand1 + hohe_Rand1)) / 2 - bcarsize / 2
belegt = []
belegt_extra = []
Parkplatz_list = []
Parkplatz_list_extra =[]
Parkplatzanzahl = 100  # Parkplatzanzahl
Parkplatzanzahl_extra = 10
Parkplatzanzahl_ohne_extra = Parkplatzanzahl - Parkplatzanzahl_extra
# lade autobilder
for i in autobilder:
    carpic = pygame.image.load(i)
    carpic = pygame.transform.scale(carpic, carsize)
    carpic = pygame.transform.rotate(carpic, 180)
    carcolours.append(carpic)

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
        if len(Parkplatz_list_extra) < Parkplatzanzahl_extra:
            while True:
                car.lotnumber = random.randint(Parkplatzanzahl_ohne_extra + 1, Parkplatzanzahl)
                if car.lotnumber not in belegt_extra:
                    belegt_extra.append(car.lotnumber)
                    break
        else:
            while True:
                car.lotnumber = random.randint(0, Parkplatzanzahl_ohne_extra)
                if car.lotnumber not in belegt:
                    belegt.append(car.lotnumber)
                    break
    else:
        while True:
            car.lotnumber = random.randint(0, Parkplatzanzahl_ohne_extra)
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
    if fahrrichtung == 0:
        fahrrichtung = -1
    elif fahrrichtung == 1:
        fahrrichtung = 0
    self_rect.x, self_rect.y = get_car.carpos
    screen.blit(self, self_rect)
    self_rect.y -= (hohe_Parkplatz - lcarsize // 2 + breite_Straße // 2) * parkrichtung - bcarsize // 2 # hohe_Parkplatz * parkrichtung
    genbackground()
    screen.blit(self, self_rect)
    self = pygame.transform.rotate(self, 90 * parkrichtung)
    xausfahrt = (breite_Parkplatz + 3) * (maxplaetze_pro_reihe - spalte) + breite_Straße // 2
    yausfahrt = yeinfahrt + (breite_Straße + hohe_Parkplatz)#(y_zurückfenster - hohe_anzeigefenster)/2 + hohe_anzeigefenster - bcarsize/2
    xfahrt = breite_screen - lcarsize
    while self_rect.x < xausfahrt:
        self_rect.x += 1
        screen.blit(self, self_rect)
        genbackground()
    self = pygame.transform.rotate(self, 90 * fahrrichtung)
    print('get_out', self_rect.y, yausfahrt, fahrrichtung)
    while self_rect.y != yausfahrt:
        print(self_rect.y, yausfahrt)
        self_rect.y -= fahrrichtung
        screen.blit(self, self_rect)
        genbackground()
    self = pygame.transform.rotate(self, 90 * fahrrichtung * (-parkrichtung))
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
    print(f'You have to pay: {amounttopay} Euro')
    newrevenue = oldrevenue + amounttopay
    print(f'Your revenue is: {newrevenue} Euro')
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
    pygame.draw.rect(screen, black, (x_anzeigefenster, y_anzeigefenster, breite_anzeigefenster, hohe_anzeigefenster))  # Anzeigefenster
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
    for i in range(Parkplatzanzahl):
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
    for i in range(Parkplatzanzahl_extra):
        Pex = Parkplatz_list[-1]
        Parkplatz_list_extra.append(Pex)
        Parkplatz_list.remove(Pex)
def genbackground():
    genscreen()
    genrand()
    genParkplaetze()
    datum()

# main-loop
running = True
genbackground()
pygame.display.flip()
while running == True:
    now = time.time()
    secounds = now - starttime
    if len(carsinlot) == Parkplatzanzahl:
        print('The parkinglot is full!')
    else:
        carspawntime = (random.randint(minspawntime, maxspawntime))/zeittraffer
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
        screen.blit(i.image, i.carpos)
        if now > i.exittime/zeittraffer:
            i.carpos, i.image = getcarout(i)
            revenue = pay(i, revenue)
            deletecar(i)
    if now == 24 * hins * zeittraffer:
        for i in carsinlot:
            i.carpos, i.image = getcarout(i)
            revenue = pay(i, revenue)
            deletecar(i)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    pygame.display.update()