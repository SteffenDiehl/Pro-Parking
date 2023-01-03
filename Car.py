import time
import random
import pygame
from pygame.locals import *

carspawntime = random.randint(5, 10)
carsinlot = []
start = time.time()
carcolors =[]
extras = ['family', 'handycaped']
carcounter = 1
carsize = (100, 50)
lotcount = 5
price = 8 # Preis pro h in €
simend = time.time() + 3* 60

dpx = 600
dpy = 400
reihenabstand = 30
platzabstand = 15
grey = (170, 170, 170)
screen = pygame.display.set_mode((dpx, dpy))
pygame.display.set_caption('First drive')

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
    carcolor = random.sample(carcolors, 1)  # zufällige autofarbe
    extra = situation()  # anspruch auf sonderparkplatz
    car = cars(timer, starttime, endtime, 0, carcolor, extra)
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

def parkcar(car, reihe, platz):
    x = 0
    y = 0
    screen.blit(car, (x, y))
    x += 20
    screen.blit(car, (x, y))
    car = pygame.transform.rotate(car, -90)
    for i in range(reihe):
        y += reihenabstand
        screen.blit(car, (x, y))
    car = pygame.transform.rotate(car, 90)
    for i in range(platz):
        x += platzabstand
        screen.blit(car, (x, y))
    car = pygame.transform.rotate(car, -90)
    y += 5
    screen.blit(car, (x, y))

def getcarout(car):
    print('tbd')
    pay(car)


def pay(car):
    hours = car.cartimer//3600
    if hours < car.cartimer/3600:
        hours +=1
    amounttopay = hours * price
    print(f'You have to pay: {amounttopay}')


whitecar = pygame.image.load('whitecar.jpg')
whitecar = pygame.transform.scale(whitecar, carsize)
whitecar = pygame.transform.rotate(whitecar, 180)
carcolors.append(whitecar)

while True:
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
    for car in carsinlot:
        print(car.cartimer, car.lotnumber, car.colour, car.extra)
        currenttime = time.time()
        if currenttime > car.exittime:
            getcarout(car)
    if simend == time.time():
        break




running = True
while running:
    screen.fill(grey)
    parkcar(whitecar, 3, 5)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    pygame.display.update()