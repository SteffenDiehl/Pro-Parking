import time
import random
from pygame.locals import *
import pygame
from datetime import date

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
zeittraffer = 120
hins = 3600  # StundeinSekunde(3600)
minparkdauer = hins/4 # 15 min in s
maxparkdauer = 12 * hins # 12h in s
#variable spawntime
minspawntime = hins/60 # min 1 min zwischen spawns
maxspawntime = 15*(hins/60) # max 15 min zwischen spawns

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

class cars: #definiere welche variablen jedes Auto haben soll
    def __init__(self, cartimer, entrietime, exittime, lotnumber, carpos, image, extra):
        self.cartimer = cartimer
        self.entrietime = entrietime
        self.exittime = exittime
        self.lotnumber = lotnumber
        self.carpos = carpos
        self.image = image
        self.extra = extra

def spawncar(): #erstelle ein Auto
    global carsinlot
    timer = random.randint(minparkdauer, maxparkdauer) #zufällige Parkzeit
    starttime = time.time()  # Zeitpunkt einfahrt
    endtime = starttime + timer  # Zeitpunkt ausfahrt
    carimage = random.choice(carcolours)  # zufällige autofarbe
    extra = situation()  # anspruch auf sonderparkplatz
    car = cars(timer, starttime, endtime, 0, (0, 0), carimage, extra) #erstelle das Auto
    if car.extra in extras: #prüfe ob es ein recht auf Sonderparkplätze hat
        if len(belegt_extra) < Parkplatzanzahl_extra: #prüfe ob es noch Sonderparkplätze gibt
            while True:
                car.lotnumber = random.randint(Parkplatzanzahl_ohne_extra + 1, Parkplatzanzahl)
                #print(Parkplatzanzahl_ohne_extra, Parkplatzanzahl)
                if car.lotnumber not in belegt_extra: #prüfe ob der zugewiesene Sonderparkplatz belegt ist
                    belegt_extra.append(car.lotnumber)
                    break
        else:
            while True:
                car.lotnumber = random.randint(0, Parkplatzanzahl_ohne_extra)
                if car.lotnumber not in belegt: #prüfe ob der zugewiesene Parkplatz belegt ist
                    belegt.append(car.lotnumber)
                    break
    else:
        while True: #prüfe ob der zugewiesene Parkplatz belegt ist
            car.lotnumber = random.randint(0, Parkplatzanzahl_ohne_extra)
            if car.lotnumber not in belegt:
                belegt.append(car.lotnumber)
                break
    carsinlot.append(car)
    #print(carsinlot)
    return

def situation():
    x = random.randint(0, 20)  # je 10% chance auf Anspruch für Familien- oder Behindertenparkplatz
    if x == 0 or x == 1:
        extra = extras[x]
    else:
        extra = 'none'
    return extra

def howtodrive(get_car): #stelle fest wo dein Parkplatz liegt und wie du zu parken hast
    global meinestrase, parkrichtung
    reihe = get_car.lotnumber // maxplaetze_pro_reihe
    # print(reihe, car.lotnumber, maxplaetze_pro_reihe)
    spalte = get_car.lotnumber % maxplaetze_pro_reihe
    if spalte == 0:
        spalte = 20
        if reihe != 0:
            reihe -= 1
    fahrrichtung = 1
    if reihe == 3: #reihe oben
        meinestrase = 2
        fahrrichtung = -1
        parkrichtung = -1
    elif reihe == 1: #2. reihe von oben
        meinestrase = 1
        fahrrichtung = -1
        parkrichtung = -1
    elif reihe == 0: #reihe mitte
        meinestrase = 1
        fahrrichtung = -1
        parkrichtung = 1
    elif reihe == 2: #2. reihe von unten
        meinestrase = 0
        fahrrichtung = 0
        parkrichtung = 1
    elif reihe == 4: #reihe unten
        meinestrase = 1
        fahrrichtung = 1
        parkrichtung = 1
    return reihe, spalte, meinestrase, fahrrichtung, parkrichtung

def parkcar(get_car):  # das auto parken
    self = get_car.image
    self_rect = self.get_rect()
    reihe, spalte, meinestrase, fahrrichtung, parkrichtung = howtodrive(get_car) #stelle fest wo dein Parkplatz ist
    self_rect.x = xeinfahrt
    self_rect.y = yeinfahrt
    screen.blit(self, self_rect)
    self_rect.x += breite_Rand1 + breite_Straße // 2 - bcarsize // 2
    screen.blit(self, self_rect)
    self = pygame.transform.rotate(self, -90 * fahrrichtung)
    ydrive = self_rect.y + (breite_Straße + hohe_Parkplatz) * meinestrase * fahrrichtung
    xdrive = self_rect.x + breite_Straße // 2 + (bcarsize * 2) // 3 + (breite_Parkplatz + 3) * (spalte - 1)
    while self_rect.y != ydrive: #fahre bis du die Straße, in der dein Parkplatz liegt erreichst
        self_rect.y += fahrrichtung
        genbackground(1)
        screen.blit(self, self_rect)
    self = pygame.transform.rotate(self, 90 * fahrrichtung)
    while self_rect.x != xdrive: #fahre bis du deinen Parkplatz erreicht hast
        self_rect.x += 1
        genbackground(1)
        screen.blit(self, self_rect)
    self = pygame.transform.rotate(self, -90) #parke ein
    self_rect.y += (hohe_Parkplatz - lcarsize // 2 + breite_Straße // 2) * parkrichtung - bcarsize // 2
    genbackground(1)
    screen.blit(self, self_rect)
    return (self_rect.x, self_rect.y), self

def getcarout(get_car):
    self = get_car.image
    self_rect = self.get_rect()
    reihe, spalte, meinestrase, fahrrichtung, parkrichtung = howtodrive(get_car) #stelle fest wo und wie du geparkt hast
    if fahrrichtung == 0:
        fahrrichtung = -1
    elif fahrrichtung == 1:
        fahrrichtung = 0
    self_rect.x, self_rect.y = get_car.carpos
    screen.blit(self, self_rect)
    self_rect.y -= (hohe_Parkplatz - lcarsize // 2 + breite_Straße // 2) * parkrichtung - bcarsize // 2 #parke aus
    genbackground(1)
    screen.blit(self, self_rect)
    self = pygame.transform.rotate(self, 90 * parkrichtung)
    xausfahrt = (breite_Parkplatz + 3) * (maxplaetze_pro_reihe - spalte) + breite_Straße // 2
    yausfahrt = yeinfahrt + (breite_Straße + hohe_Parkplatz)
    xfahrt = breite_screen - lcarsize
    while self_rect.x < xausfahrt: #fahre bis ans Ende der Straße
        self_rect.x += 1
        screen.blit(self, self_rect)
        genbackground(1)
    self = pygame.transform.rotate(self, 90 * fahrrichtung)
    while self_rect.y != yausfahrt: #fahre bis du die Ausfahrt erreichst
        self_rect.y -= fahrrichtung
        screen.blit(self, self_rect)
        genbackground(1)
    self = pygame.transform.rotate(self, 90 * fahrrichtung * (-parkrichtung))
    while self_rect.x != xfahrt: #fahre zur Ausfahrt raus
        self_rect.x += 1
        genbackground(1)
        screen.blit(self, self_rect)
    return (self_rect.x, self_rect.y), self


def pay(car, oldrevenue): #leider musst auch du zahlen
    hours = car.cartimer // hins #wie lange hast du geparkt
    if hours < car.cartimer / hins:
        hours += 1 #angefangene Stunden müssen voll gezahlt werden
    amounttopay = hours * price
    print(f'You have to pay: {amounttopay} Euro')
    newrevenue = oldrevenue + amounttopay #wie viel wurde bisher verdient
    print(f'Your revenue is: {newrevenue} Euro')
    return newrevenue


def deletecar(car): #entferne das Auto aus dem Parkplatz
    if car.extra == 'none':
        belegt.remove(car.lotnumber)
    else:
        belegt_extra.remove(car.lotnumber)
    carsinlot.remove(car)
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

def genParkplaetze(j):
    Parkplatz_list = []
    x = 0
    y = 0
    z = 0
    for i in range(Parkplatzanzahl):
        Px = pygame.draw.rect(screen, white, (
            x_Parkplatz1 + (breite_Parkplatz + 3) * x, y_Parkplatz1 - y, breite_Parkplatz, hohe_Parkplatz), 2)
        if j == 0:
            Parkplatz_list.append(Px)
        x += 1
        z += 1
        if x == maxplaetze_pro_reihe:
            x = 0
        if z == 40 or z == 80 or z == 60:
            y *= -1
        if z == 20 or z == 60:
            y += breite_Straße + hohe_Parkplatz
    if j == 0:
        for i in range(Parkplatzanzahl_extra):
            Pex = Parkplatz_list[-1]
            Parkplatz_list_extra.append(Pex)
            Parkplatz_list.remove(Pex)
        #print(Parkplatz_list_extra, Parkplatzanzahl_extra, len(Parkplatz_list_extra), Parkplatzanzahl, len(Parkplatz_list))
def genbackground(i):
    genscreen()
    genrand()
    genParkplaetze(i)
    datum()

# main-loop
park_running = True
genbackground(0)
pygame.display.flip()
while park_running == True: #parkloop
    now = time.time()
    secounds = now - starttime
    if len(carsinlot) == Parkplatzanzahl: #können noch Autos in das Parkhaus fahren
        print('The parkinglot is full!')
    else:
        carspawntime = (random.randint(minspawntime, maxspawntime))/zeittraffer
        if secounds > carspawntime: #steht ein Auto vor dem Parkhaus
            carspawntime = random.randint(1, 3)
            starttime = time.time()
            spawncar()
            carcounter += 1
            car = carsinlot[-1]
            car.carpos, car.image = parkcar(car)
    pygame.display.update()
    for i in carsinlot: #welche Autos parken aktuell
        #print(i.cartimer, i.lotnumber, i.carpos, i.image, i.extra)
        screen.blit(i.image, i.carpos)
        if now > (i.entrietime + i.cartimer/zeittraffer): #fährt ein Auto raus
            i.carpos, i.image = getcarout(i)
            revenue = pay(i, revenue)
            deletecar(i)
    if now == 24 * hins * zeittraffer: #alle Autos müssen raus fahren
        print('Das Parkhaus schliest')
        for i in carsinlot:
            i.carpos, i.image = getcarout(i)
            revenue = pay(i, revenue)
            deletecar(i)
    for event in pygame.event.get():
        if event.type == QUIT:
            park_running = False
    pygame.display.update()