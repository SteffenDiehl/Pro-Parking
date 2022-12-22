import datetime

import pygame
import random

from pygame.locals import*
from datetime import date

pygame.init()

BREITE = 1400
HÖHE = 750
GRUEN = (0, 255, 0)
BLACK = (0,0,0)
White = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,200,0)
GRAY = (127,127,127)


screen = pygame.display.set_mode((BREITE, HÖHE))
pygame.display.set_caption('Parkhaus Simulation')


x_eingrenzung = 1050
y_eingrenzung = 0
hohe_eingrenzung = 500
breite_eingrenzung = 10
abstand_oberflache = 120
x_eingrenzung_links = 100

y_wert_queer = hohe_eingrenzung
breite_eingrenzung_quer = BREITE - x_eingrenzung


x_button = 450
y_button_play =270
y_button_setting = y_button_play + 120
y_button_info = y_button_setting + 120
y_buuton_exit = y_button_info + 120
breit_Botton = 500
hohe_button = 80

button_play = pygame.Rect(x_button, y_button_play, breit_Botton, hohe_button)
button_settings = pygame.Rect(x_button, y_button_setting, breit_Botton, hohe_button)
button_info = pygame.Rect(x_button, y_button_info, breit_Botton, hohe_button)
button_exit = pygame.Rect(x_button, y_buuton_exit, breit_Botton, hohe_button)


#zurück
x_zurück = 10
y_zurück = 10
höhe_zurück = 50
breite_zurück = 80





def display_message_play(msg='PLAY'):
    my_font = pygame.font.Font(None, 100)
    text_surface = my_font.render(msg, True, White)
    text_rect = text_surface.get_rect()
    text_rect.center = (x_button + breit_Botton/2, y_button_play + hohe_button/2)
    screen.blit(text_surface, text_rect)

def display_message_setting(msg='SETTINGS'):
    my_font = pygame.font.Font(None, 100)
    text_surface = my_font.render(msg, True, White)
    text_rect = text_surface.get_rect()
    text_rect.center = (x_button + breit_Botton/2, y_button_setting + hohe_button/2)
    screen.blit(text_surface, text_rect)

def display_message_info(msg='INFO'):
    my_font = pygame.font.Font(None, 100)
    text_surface = my_font.render(msg, True, White)
    text_rect = text_surface.get_rect()
    text_rect.center = (x_button + breit_Botton/2, y_button_info + hohe_button/2)
    screen.blit(text_surface, text_rect)

def display_message_exit(msg='EXIT'):
    my_font = pygame.font.Font(None, 100)
    text_surface = my_font.render(msg, True, White)
    text_rect = text_surface.get_rect()
    text_rect.center = (x_button + breit_Botton/2, y_buuton_exit + hohe_button/2)
    screen.blit(text_surface, text_rect)

def display_message_title(msg='Parkhaus Überwachung'):
    my_font = pygame.font.Font(None, 120)
    text_surface = my_font.render(msg, True, White)
    text_rect = text_surface.get_rect()
    text_rect.center = (x_button + breit_Botton/2, y_button_play - 150 )
    screen.blit(text_surface, text_rect)


def zurück_in_box(msg='zurück'):
    my_font = pygame.font.Font(None, 30)
    text_surface = my_font.render(msg, True, White)
    text_rect = text_surface.get_rect()
    text_rect.center = (x_zurück + breite_zurück/2, y_zurück + höhe_zurück/2 )
    screen.blit(text_surface, text_rect)


x_eingrenzung = 1050
y_eingrenzung = 0
hohe_eingrenzung = 500
breite_eingrenzung = 10
abstand_oberflache = 120
x_eingrenzung_links = 100

date = str(date.today())
def datum(msg='Datum: '+ date):
    my_font = pygame.font.Font(None, 40)
    text_surface = my_font.render(msg, True, White)
    text_rect = text_surface.get_rect()
    text_rect.center = (1200, 15 )
    screen.blit(text_surface, text_rect)

time = str(datetime.time())
def uhrzeit(msg='Uhrzeit: ' + time + ' Uhr'):
    my_font = pygame.font.Font(None, 40)
    text_surface = my_font.render(msg, True, White)
    text_rect = text_surface.get_rect()
    text_rect.center = (1220, 50)
    screen.blit(text_surface, text_rect)







def parkplatze():
    parkplatzbreite = 50
    parkplatzhohe = 100
    parkplätze_z = 15
    parkplätze_sp = 3


    Parkplatz1 = pygame.Rect(x_eingrenzung_links + breite_eingrenzung + 20, y_eingrenzung + 20, parkplatzbreite,
                             parkplatzhohe)
    i = 20
    d = 20


    for f in range(parkplätze_sp):
        for o in range(parkplätze_z):
            Parkplatz1 = pygame.Rect(x_eingrenzung_links + breite_eingrenzung + i, y_eingrenzung + d, parkplatzbreite,
                                     parkplatzhohe)
            pygame.draw.rect(screen, White, Parkplatz1, 5)

            i += 60
        i = 20
        d += 120

def oberflaeche_menue():
    x_button = 450
    y_button_play = 270
    y_button_setting = y_button_play + 120
    y_button_info = y_button_setting + 120
    y_buuton_exit = y_button_info + 120
    breit_Botton = 500
    hohe_button = 80

    button_play = pygame.Rect(x_button, y_button_play, breit_Botton, hohe_button)
    button_settings = pygame.Rect(x_button, y_button_setting, breit_Botton, hohe_button)
    button_info = pygame.Rect(x_button, y_button_info, breit_Botton, hohe_button)
    button_exit = pygame.Rect(x_button, y_buuton_exit, breit_Botton, hohe_button)
    farbe = BLACK
    running = True
    while running:
        screen.fill(farbe)

        pygame.draw.rect(screen, GRUEN, button_play, 0)
        pygame.draw.rect(screen, BLUE, button_settings, 0)
        pygame.draw.rect(screen, YELLOW, button_info, 0)
        pygame.draw.rect(screen, RED, button_exit, 0)

        display_message_play()
        display_message_setting()
        display_message_info()
        display_message_exit()
        display_message_title()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    button_play = pygame.Rect(x_button - 10, y_button_play - 10, breit_Botton + 20, hohe_button + 20)
                    pygame.draw.rect(screen, RED, button_play, 10)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    farbe = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255),)

        (x, y) = pygame.mouse.get_pos()
        pygame.draw.rect(screen, White, (x, y, 10, 10,), 0)

        if x > x_button and x < x_button + breit_Botton and y > y_button_play and y < y_button_play + hohe_button:
            button_play = pygame.Rect(x_button - 10, y_button_play - 10, breit_Botton + 20, hohe_button + 20)
            pygame.draw.rect(screen, White, button_play, 10)
            if event.type == MOUSEBUTTONDOWN:
                running = False
                parkhaus_oberflaeche()
                #parkplatze()
        else:
            button_play = pygame.Rect(x_button, y_button_play, breit_Botton, hohe_button)



        if x > x_button and x < x_button + breit_Botton and y > y_button_setting and y < y_button_setting + hohe_button:
            button_settings = pygame.Rect(x_button - 10, y_button_setting - 10, breit_Botton + 20, hohe_button + 20)
            pygame.draw.rect(screen, White, button_settings, 10)
            if event.type == MOUSEBUTTONDOWN:
                running = False
                settings()

        else:
            button_settings = pygame.Rect(x_button, y_button_setting, breit_Botton, hohe_button)



        if x > x_button and x < x_button + breit_Botton and y > y_button_info and y < y_button_info + hohe_button:
            button_info = pygame.Rect(x_button - 10, y_button_info - 10, breit_Botton + 20, hohe_button + 20)
            pygame.draw.rect(screen, White, button_info, 10)
        else:
            button_info = pygame.Rect(x_button, y_button_info, breit_Botton, hohe_button)



        if x > x_button and x < x_button + breit_Botton and y > y_buuton_exit and y < y_buuton_exit + hohe_button:
            button_exit = pygame.Rect(x_button - 10, y_buuton_exit - 10, breit_Botton + 20, hohe_button + 20)
            pygame.draw.rect(screen, White, button_exit, 10)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    running = False
        else:
            button_exit = pygame.Rect(x_button, y_buuton_exit, breit_Botton, hohe_button)

        pygame.display.update()




def parkhaus_oberflaeche():
    runningspiel = True
    farbe = BLACK
    while runningspiel:
        screen.fill(farbe)


        #zurück
        x_zurück = 10
        y_zurück = 10
        höhe_zurück = 50
        breite_zurück = 80

        zurück = pygame.Rect(x_zurück, y_zurück, breite_zurück, höhe_zurück)
        pygame.draw.rect(screen, RED, zurück, 0)

        zurück_in_box()


        (x, y) = pygame.mouse.get_pos()
        pygame.draw.rect(screen, White, (x, y, 10, 10,), 0)




        if x > x_zurück and x < x_zurück + breite_zurück and y > y_zurück and y < y_zurück + höhe_zurück:
            button_exit = pygame.Rect(x_zurück - 10, y_zurück - 10, breite_zurück + 20, höhe_zurück + 20)
            pygame.draw.rect(screen, White, zurück, 4)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    runningspiel = False
                    oberflaeche_menue()



        x_eingrenzung = 1050
        y_eingrenzung = 0
        hohe_eingrenzung = 500
        breite_eingrenzung = 10
        abstand_oberflache = 120
        x_eingrenzung_links = 100

        y_wert_queer = hohe_eingrenzung
        breite_eingrenzung_quer = BREITE - x_eingrenzung
        benutzerfenster1 = pygame.Rect(x_eingrenzung, y_eingrenzung, breite_eingrenzung, hohe_eingrenzung)
        benutzerfenster2 = pygame.Rect(x_eingrenzung, y_wert_queer, breite_eingrenzung_quer, breite_eingrenzung)
        benutzerfenster3 = pygame.Rect(x_eingrenzung, y_wert_queer + abstand_oberflache, breite_eingrenzung_quer,
                                       breite_eingrenzung)
        benutzerfenster4 = pygame.Rect(x_eingrenzung, y_eingrenzung + abstand_oberflache + hohe_eingrenzung,
                                       breite_eingrenzung, HÖHE - hohe_eingrenzung)
        benutzerfenster5 = pygame.Rect(x_eingrenzung_links, y_eingrenzung, breite_eingrenzung, hohe_eingrenzung)
        benutzerfenster6 = pygame.Rect(0, y_wert_queer, x_eingrenzung_links + breite_eingrenzung, breite_eingrenzung)
        benutzerfenster7 = pygame.Rect(0, y_wert_queer + abstand_oberflache, x_eingrenzung_links + breite_eingrenzung,
                                       breite_eingrenzung)
        benutzerfenster8 = pygame.Rect(x_eingrenzung_links, y_eingrenzung + abstand_oberflache + hohe_eingrenzung,
                                       breite_eingrenzung, HÖHE - hohe_eingrenzung)

        ParkundStrasse1 = pygame.Rect(x_eingrenzung_links + breite_eingrenzung, y_eingrenzung, BREITE - x_eingrenzung_links - (BREITE-x_eingrenzung) - breite_eingrenzung, HÖHE)
        ParkundStrasse2 = pygame.Rect(0, hohe_eingrenzung, BREITE, abstand_oberflache)



        pygame.draw.rect(screen, GRAY, ParkundStrasse1, 0)
        pygame.draw.rect(screen, GRAY, ParkundStrasse2, 0)

        pygame.draw.rect(screen, White, benutzerfenster1, 0)
        pygame.draw.rect(screen, White, benutzerfenster2, 0)
        pygame.draw.rect(screen, White, benutzerfenster3, 0)
        pygame.draw.rect(screen, White, benutzerfenster4, 0)
        pygame.draw.rect(screen, White, benutzerfenster5, 0)
        pygame.draw.rect(screen, White, benutzerfenster6, 0)
        pygame.draw.rect(screen, White, benutzerfenster7, 0)
        pygame.draw.rect(screen, White, benutzerfenster8, 0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runningspiel = False

        datum()
        uhrzeit()
        parkplatze()
        pygame.display.update()



def parkplatz_antahl_x (msg='Anzahl Parkplätze X: '):
    my_font = pygame.font.Font(None, 50)
    text_surface = my_font.render(msg, True, White)
    text_rect = text_surface.get_rect()
    text_rect.center = (500, 500)
    screen.blit(text_surface, text_rect)

def settings():
    runningsetting = True
    farbe = BLACK
    while runningsetting:
        screen.fill(farbe)

        # zurück
        x_zurück = 10
        y_zurück = 10
        höhe_zurück = 50
        breite_zurück = 80

        zurück = pygame.Rect(x_zurück, y_zurück, breite_zurück, höhe_zurück)
        pygame.draw.rect(screen, RED, zurück, 0)

        zurück_in_box()
        datum()
        uhrzeit()
        parkplatz_antahl_x()

        (x, y) = pygame.mouse.get_pos()
        pygame.draw.rect(screen, White, (x, y, 10, 10,), 0)

        if x > x_zurück and x < x_zurück + breite_zurück and y > y_zurück and y < y_zurück + höhe_zurück:
            button_exit = pygame.Rect(x_zurück - 10, y_zurück - 10, breite_zurück + 20, höhe_zurück + 20)
            pygame.draw.rect(screen, White, zurück, 4)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    runningsetting = False
                    oberflaeche_menue()

        minustaste = pygame.Rect(700, 475, 100, 50)
        pygame.draw.rect(screen, RED, minustaste, 0)
        if x > 700 and x < 800 and y > 475 and y < 525:
            minustaste = pygame.Rect(700 - 2.5, 475 - 2.5, 100 + 5, 50 + 5)
            pygame.draw.rect(screen, White, minustaste, 4)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    parkplätze_z -= 2



        plustaste = pygame.Rect(700+120, 475, 100, 50)
        pygame.draw.rect(screen, GRUEN, plustaste, 0)
        if x > (700 + 120) and x < 800 + 120 and y > 475 and y < 525:
            plustaste = pygame.Rect(700 + 120 - 2.5, 475 - 2.5, 100 + 5, 50 + 5)
            pygame.draw.rect(screen, White, plustaste, 4)
            # if event.type == MOUSEBUTTONDOWN:
            #   if event.button == 1:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runningsetting = False






        pygame.display.update()











oberflaeche_menue()





