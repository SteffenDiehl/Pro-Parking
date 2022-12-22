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

dpx = 600
dpy = 400
reihenabstand = 30
platzabstand = 15
grey = (170, 170, 170)
screen = pygame.display.set_mode((dpx, dpy))
pygame.display.set_caption('First drive')

class cars:
    def __init__(self, cartimer, lotnumber, colour, extra):
        self.cartimer = cartimer
        self.lotnumber = lotnumber
        self.colour = colour
        self.extra = extra

def spawncar():
    timer = random.randint(900, 43200)  # 15min - 12h in s
    carcolor = random.sample(carcolors, 1)  # zufällige autofarbe
    extra = situation()  # anspruch auf sonderparkplatz
    newcar = cars(timer, 0, carcolor, extra)
    carsinlot.append(newcar)
    print(carsinlot)
    return

def situation():
    x = random.randint(0, 10) # je 10% chance auf anspruch für fimilien oder behinderten parkplatz
    if x == 0 or x == 1:
        extra = extras[x]
    else:
        extra = 'none'
    return extra

def movecar(car, reihe, platz):
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

whitecar = pygame.image.load('whitecar.jpg')
whitecar = pygame.transform.scale(whitecar, carsize)
whitecar = pygame.transform.rotate(whitecar, 180)
carcolors.append(whitecar)

while True:
    now = time.time()
    secounds = now - start
    if secounds > carspawntime:
        carspawntime = random.randint(5, 10)
        start = time.time()
        spawncar()
        carcounter +=1
    if len(carsinlot) == 5:
        break

for i in carsinlot:
    print(i.cartimer, i.lotnumber, i.colour, i.extra)

running = True
while running:
    screen.fill(grey)
    movecar(whitecar, 3, 5)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    pygame.display.update()