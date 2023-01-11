import time
import random
import pygame
from pygame.locals import *
pygame.init()

carspawntime = random.randint(3, 5)
carsinlot = []
start = time.time()
carcolours =[]
extras = ['family', 'handycaped']
carcounter = 1
carsize = (60, 30)
price = 8 # Preis pro h in €
simend = time.time() + 3* 60
zeittraffer = 0
parkinglot = []
revenue = 0
hins = 3600 #StundeinSekunde(3600)
minparkdauer = 10 #900 = 15 min in s
maxparkdauer = 30 #43200 = 12h in s

maxreihen = 3
maxspalten = 6
for r in range(maxreihen):
    for s in range(maxspalten):
        parkinglot.append((r, s))
lotcount = len(parkinglot)
print(lotcount)

dpx = 1000
dpy = 800
reihenabstand = 100
platzabstand = 25
parkplatzlaenge = 50
einfahrtslaenge = 50
xeinfahrt = 50
yeinfahrt = 300
xausfahrt = 600
yausfahrt = 300
grey = (170, 170, 170)
screen = pygame.display.set_mode((dpx, dpy))
pygame.display.set_caption('First drive')

whitecar = pygame.image.load('whitecar.jpg')
whitecar = pygame.transform.scale(whitecar, carsize)
whitecar = pygame.transform.rotate(whitecar, 180)
carcolours.append(whitecar)
class cars:
    def __init__(self, cartimer, entrietime, exittime, lotnumber, colour, extra):
        self.cartimer = cartimer
        self.entrietime = entrietime
        self.exittime = exittime
        self.lotnumber = lotnumber
        self.colour = colour
        self.extra = extra

def spawncar():
    timer = random.randint(minparkdauer, maxparkdauer)
    starttime = time.time() # Zeitpunkt einfahrt
    endtime = starttime + timer # Zeitpunkt ausfahrt
    carcolour = random.choice(carcolours)  # zufällige autofarbe
    extra = situation()  # anspruch auf sonderparkplatz
    car = cars(timer, starttime, endtime, 0, carcolour, extra)
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

def parkcar(car): # das auto parken
    pygame.display.update()
    reihe , spalte = parkinglot[car.lotnumber]
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
    return (x,y)

def getcarout(car):
    reihe, spalte = parkinglot[car.lotnumber]
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
    return (x, y)

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

running = True
while running == True:
    screen.fill(grey)
    now = time.time()
    secounds = now - start
    if len(carsinlot) == lotcount:
        print('The parkinglot is full!')
    else:
        if secounds > carspawntime:
            carspawntime = random.randint(3, 8)
            start = time.time()
            spawncar()
            carcounter += 1
            car = carsinlot[-1]
            screen.blit(car.colour, parkcar(car))
    for i in carsinlot:
        print(i.cartimer, i.lotnumber, i.colour, i.extra)
        currenttime = time.time()
        if currenttime > i.exittime:
            screen.blit(i.colour, getcarout(i))
            pay(i, revenue)
            deletecar(i)
    if simend == time.time():
        break
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    #pygame.display.update()