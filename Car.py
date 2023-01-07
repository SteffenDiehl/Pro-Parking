import time
import random
import pygame
from pygame.locals import *

carspawntime = random.randint(5, 10)
carsinlot = []
start = time.time()
carcolours =[]
extras = ['family', 'handycaped']
carcounter = 1
carsize = (100, 50)
price = 8 # Preis pro h in €
simend = time.time() + 3* 60
parkinglot = []
revenue = 0

reihen = 3
spalten = 6
for r in range(reihen):
    for s in range(spalten):
        parkinglot.append((r, s))
lotcount = len(parkinglot)

dpx = 600
dpy = 400
reihenabstand = 30
platzabstand = 15
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
    timer = random.randint(20, 30) #(900, 43200)  # 15min - 12h in s
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

def parkcar(car):
    reihe , spalte = parkinglot[car.lotnumber]
    x = 0
    y = 0
    thiscar = car.colour
    screen.blit(thiscar, (x, y))
    x += 20
    screen.blit(thiscar, (x, y))
    thiscar = pygame.transform.rotate(thiscar, -90)
    for i in range(reihe):
        y += reihenabstand
        screen.blit(thiscar, (x, y))
        pygame.display.update()
    thiscar = pygame.transform.rotate(thiscar, 90)
    for i in range(spalte):
        x += platzabstand
        screen.blit(thiscar, (x, y))
        pygame.display.update()
    thiscar = pygame.transform.rotate(thiscar, -90)
    y += 5
    screen.blit(thiscar, (x, y))
    pygame.display.update()

def getcarout(car):
    print('tbd')
    newrevenue = pay(car, revenue)
    deletecar(car)
    return newrevenue

def pay(car, newrevenue):
    hours = car.cartimer//3600
    if hours < car.cartimer/3600:
        hours +=1
    amounttopay = hours * price
    print(f'You have to pay: {amounttopay}')
    newrevenue += amounttopay
    print(f'Your revenue is: {newrevenue}')
    return newrevenue
def deletecar(car):
    print('tbd', car)

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
            parkcar(car)
    for car in carsinlot:
        print(car.cartimer, car.lotnumber, car.colour, car.extra)
        currenttime = time.time()
        if currenttime > car.exittime:
            revenue = getcarout(car)
    if simend == time.time():
        break
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    pygame.display.update()