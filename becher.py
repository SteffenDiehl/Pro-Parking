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
    text_rect.center = (1130, 250 )
    screen.blit(text_surface, text_rect)

time = str(datetime.time())
def uhrzeit(msg='Uhrzeit: ' + time + ' Uhr'):
    my_font = pygame.font.Font(None, 40)
    text_surface = my_font.render(msg, True, White)
    text_rect = text_surface.get_rect()
    text_rect.center = (1150, 300)
    screen.blit(text_surface, text_rect)







def parkplatze():
    parkplatzbreite = 50
    parkplatzhohe = 100
    parkplätze_z = 10
    parkplätze_sp = 2


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
        i = 100
        d += 300

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


#Hier werden die Taster definiert (Settings)
x_taster_minus = 550
y_taster_plus_minus = 220
breite_taster_plus_minus = 100
höhe_taster_plus_minus = 50
abstand_der_taster_x = 230
abstand_der_taster_y = 100
abstand_zw_zwei_plus_minus = 450

#variablen settings
#variable_für_anzahl_der_parkplätze = 0


def parkplatz_Anzahl_Variable (msg='Anzahl Parkplätze: '):
    my_font = pygame.font.Font(None, 45)
    text_surface = my_font.render(msg, True, White)
    text_rect = text_surface.get_rect()
    text_rect.center = (300, y_taster_plus_minus + höhe_taster_plus_minus/2)
    screen.blit(text_surface, text_rect)
def behinderten_parkplatz_Anzahl_Variable (msg='Anzahl Behindertenparkplätze: '):
    my_font = pygame.font.Font(None, 45)
    text_surface = my_font.render(msg, True, White)
    text_rect = text_surface.get_rect()
    text_rect.center = (300, y_taster_plus_minus + abstand_der_taster_y + höhe_taster_plus_minus/2)
    screen.blit(text_surface, text_rect)
def preis_pro_stunde_Variable (msg='Preis pro Stunde: '):
    my_font = pygame.font.Font(None, 45)
    text_surface = my_font.render(msg, True, White)
    text_rect = text_surface.get_rect()
    text_rect.center = (300, y_taster_plus_minus + abstand_der_taster_y*2 + höhe_taster_plus_minus/2)
    screen.blit(text_surface, text_rect)
def Öffnungszeiten_Variable_von (msg='Öffnungszeiten von: '):
    my_font = pygame.font.Font(None, 45)
    text_surface = my_font.render(msg, True, White)
    text_rect = text_surface.get_rect()
    text_rect.center = (300, y_taster_plus_minus + abstand_der_taster_y*3 + höhe_taster_plus_minus/2)
    screen.blit(text_surface, text_rect)
def Öffnungszeiten_Variable_bis (msg='bis: '):
    my_font = pygame.font.Font(None, 45)
    text_surface = my_font.render(msg, True, White)
    text_rect = text_surface.get_rect()
    text_rect.center = (x_taster_minus + breite_taster_plus_minus + abstand_der_taster_x + (abstand_zw_zwei_plus_minus - abstand_der_taster_x- breite_taster_plus_minus)/2, y_taster_plus_minus + abstand_der_taster_y*3 + höhe_taster_plus_minus/2)
    screen.blit(text_surface, text_rect)
#def anzeige_variable_für_anzahl_der_parkpätze (msg = str(variable_für_anzahl_der_parkplätze)):
 #   my_font = pygame.font.Font(None, 45)
  #  text_surface = my_font.render(msg, True, White)
   # text_rect = text_surface.get_rect()
    #text_rect.center = (400, 400)
    #screen.blit(text_surface, text_rect)


def settings():
    runningsetting = True
    farbe = BLACK

    # variablen
    variable_für_anzahl_der_parkplätze = 0
    variable_für_anzahl_der_behinderten_parkplätze = 0
    variable_für_kosten = 0
    variable_öffnungszeit = 00.00
    variable_schließzeit = 01.00

    #höchste Anzahl der Variablen
    höchste_anzahl_parkplätze = 100
    höchste_anzahl_behinderten_parkplätze = 10
    höchsten_kosten = 10
    letzte_öffnung = 23.00
    letzte_schließzeit = 24.00

    while runningsetting:
        #Bildschirmfarbe/Hintergrundfarbe
        screen.fill(farbe)

        #Knopf um in das Menü zurückzukommen
        x_zurück = 10
        y_zurück = 10
        höhe_zurück = 50
        breite_zurück = 80

        zurück = pygame.Rect(x_zurück, y_zurück, breite_zurück, höhe_zurück)
        pygame.draw.rect(screen, RED, zurück, 0)
        zurück_in_box()

        #maus im Spiel(Reckteck)
        (x, y) = pygame.mouse.get_pos()

        #Hier wird geschaut, ob die Maus auf dem knopf ist und ggf. drückt
        if x > x_zurück and x < x_zurück + breite_zurück and y > y_zurück and y < y_zurück + höhe_zurück:
            button_exit = pygame.Rect(x_zurück - 10, y_zurück - 10, breite_zurück + 20, höhe_zurück + 20)
            pygame.draw.rect(screen, White, zurück, 4)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    runningsetting = False
                    oberflaeche_menue()

        #Hier wird die große Box gebaut
        große_box = pygame.Rect(30,y_taster_plus_minus-50, BREITE - 60, 450)
        pygame.draw.rect(screen, BLUE, große_box)


        #Hier wird die Box um Datum und Uhrzeit gebaut
        box_date_time = pygame.Rect(BREITE - 400, y_taster_plus_minus-5 , 320,120)
        pygame.draw.rect(screen, BLACK, box_date_time)

        # Anzeige von Datum und Uhrzeit
        datum()
        uhrzeit()

        #Hier werden die Boxen um die Einstellungen gebaut

        Box_um_anzahl_parkplätze = pygame.Rect(50,y_taster_plus_minus-5, x_taster_minus + breite_taster_plus_minus*2 + (abstand_der_taster_x-breite_taster_plus_minus)-20, höhe_taster_plus_minus+10)
        pygame.draw.rect(screen, BLACK, Box_um_anzahl_parkplätze)
        Box_um_anzahl_behindertenparkplätze = pygame.Rect(50, y_taster_plus_minus + abstand_der_taster_y - 5, x_taster_minus + breite_taster_plus_minus * 2 + (abstand_der_taster_x - breite_taster_plus_minus) - 20,höhe_taster_plus_minus + 10)
        pygame.draw.rect(screen, BLACK, Box_um_anzahl_behindertenparkplätze)
        Box_um_preis_je_stunde = pygame.Rect(50, y_taster_plus_minus + abstand_der_taster_y * 2 - 5,x_taster_minus + breite_taster_plus_minus * 2 + (abstand_der_taster_x - breite_taster_plus_minus) - 20,höhe_taster_plus_minus + 10)
        pygame.draw.rect(screen, BLACK, Box_um_preis_je_stunde)
        Box_um_öffnngszeiten = pygame.Rect(50, y_taster_plus_minus + abstand_der_taster_y * 3 - 5,x_taster_minus + breite_taster_plus_minus * 4 + (abstand_der_taster_x - breite_taster_plus_minus) + (abstand_zw_zwei_plus_minus - breite_taster_plus_minus*2) - 20,höhe_taster_plus_minus + 10)
        pygame.draw.rect(screen, BLACK, Box_um_öffnngszeiten)

        #Hier entstehen die Taster für die anzahl der Parkplätze
        parkplatz_Anzahl_Variable()

        minustaste_parkplätze = pygame.Rect(x_taster_minus,  y_taster_plus_minus, breite_taster_plus_minus, höhe_taster_plus_minus)
        pygame.draw.rect(screen, RED, minustaste_parkplätze, 0)
        if x > x_taster_minus and x < x_taster_minus + breite_taster_plus_minus and y > y_taster_plus_minus and y < y_taster_plus_minus + höhe_taster_plus_minus:
            minustaste = pygame.Rect(x_taster_minus - 2.5, y_taster_plus_minus - 2.5, breite_taster_plus_minus + 5, höhe_taster_plus_minus + 5)
            pygame.draw.rect(screen, White, minustaste_parkplätze, 4)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    variable_für_anzahl_der_parkplätze -= 1
                   #print(variable_für_anzahl_der_parkplätze)

        plustaste_parkplätze = pygame.Rect(x_taster_minus + abstand_der_taster_x, y_taster_plus_minus, breite_taster_plus_minus, höhe_taster_plus_minus)
        pygame.draw.rect(screen, GRUEN, plustaste_parkplätze, 0)
        if x > x_taster_minus + abstand_der_taster_x and x < x_taster_minus + breite_taster_plus_minus + abstand_der_taster_x and y > y_taster_plus_minus and y < y_taster_plus_minus + höhe_taster_plus_minus:
            plustaste = pygame.Rect(x_taster_minus - 2.5 + abstand_der_taster_x, y_taster_plus_minus - 2.5, breite_taster_plus_minus + 5, höhe_taster_plus_minus + 5)
            pygame.draw.rect(screen, White, plustaste_parkplätze, 4)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    variable_für_anzahl_der_parkplätze += 1
                    #print(variable_für_anzahl_der_parkplätze)

        if variable_für_anzahl_der_parkplätze <= 0:
            variable_für_anzahl_der_parkplätze = 0
        if variable_für_anzahl_der_parkplätze >= höchste_anzahl_parkplätze:
            variable_für_anzahl_der_parkplätze = höchste_anzahl_parkplätze

        my_font = pygame.font.Font(None, 45)
        text_surface = my_font.render(str(variable_für_anzahl_der_parkplätze), True, White)
        text_rect = text_surface.get_rect()
        text_rect.center = (x_taster_minus + breite_taster_plus_minus + (abstand_der_taster_x - breite_taster_plus_minus)/2, y_taster_plus_minus + höhe_taster_plus_minus/2 )
        screen.blit(text_surface, text_rect)

        # Hier entstehen die Taster für die anzahl der Behindertenparkplätze
        behinderten_parkplatz_Anzahl_Variable()
        minustaste_behinderten_parkplätze = pygame.Rect(x_taster_minus, y_taster_plus_minus + abstand_der_taster_y, breite_taster_plus_minus,höhe_taster_plus_minus)
        pygame.draw.rect(screen, RED, minustaste_behinderten_parkplätze, 0)
        if x > x_taster_minus and x < x_taster_minus + breite_taster_plus_minus and y > y_taster_plus_minus +abstand_der_taster_y and y < y_taster_plus_minus + höhe_taster_plus_minus + abstand_der_taster_y:
            minustaste = pygame.Rect(x_taster_minus - 2.5, y_taster_plus_minus - 2.5, breite_taster_plus_minus + 5,
                                     höhe_taster_plus_minus + 5)
            pygame.draw.rect(screen, White, minustaste_behinderten_parkplätze, 4)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    variable_für_anzahl_der_behinderten_parkplätze -= 1

        plustaste_behinderten_parkplätze = pygame.Rect(x_taster_minus + abstand_der_taster_x, y_taster_plus_minus + abstand_der_taster_y, breite_taster_plus_minus, höhe_taster_plus_minus)
        pygame.draw.rect(screen, GRUEN, plustaste_behinderten_parkplätze, 0)
        if x > x_taster_minus + abstand_der_taster_x and x < x_taster_minus + breite_taster_plus_minus + abstand_der_taster_x and y > y_taster_plus_minus + abstand_der_taster_y and y < y_taster_plus_minus + höhe_taster_plus_minus + abstand_der_taster_y:
            plustaste = pygame.Rect(x_taster_minus - 2.5 + abstand_der_taster_x, y_taster_plus_minus - 2.5,
                                    breite_taster_plus_minus + 5, höhe_taster_plus_minus + 5)
            pygame.draw.rect(screen, White, plustaste_behinderten_parkplätze, 4)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    variable_für_anzahl_der_behinderten_parkplätze += 1

        if variable_für_anzahl_der_behinderten_parkplätze <= 0:
            variable_für_anzahl_der_behinderten_parkplätze = 0
        if variable_für_anzahl_der_behinderten_parkplätze >= höchste_anzahl_behinderten_parkplätze:
            variable_für_anzahl_der_behinderten_parkplätze = höchste_anzahl_behinderten_parkplätze

        my_font = pygame.font.Font(None, 45)
        text_surface = my_font.render(str(variable_für_anzahl_der_behinderten_parkplätze), True, White)
        text_rect = text_surface.get_rect()
        text_rect.center = (x_taster_minus + breite_taster_plus_minus + (abstand_der_taster_x - breite_taster_plus_minus)/2, y_taster_plus_minus +abstand_der_taster_y + höhe_taster_plus_minus/2 )
        screen.blit(text_surface, text_rect)


        # Hier entstehen die Taster für den Preis pro stunde
        preis_pro_stunde_Variable()
        minustaste_preis_je_stunde = pygame.Rect(x_taster_minus, y_taster_plus_minus + abstand_der_taster_y*2,
                                                        breite_taster_plus_minus, höhe_taster_plus_minus)
        pygame.draw.rect(screen, RED, minustaste_preis_je_stunde, 0)
        if x > x_taster_minus and x < x_taster_minus + breite_taster_plus_minus and y > y_taster_plus_minus + abstand_der_taster_y*2 and y < y_taster_plus_minus + höhe_taster_plus_minus + abstand_der_taster_y*2:
            minustaste = pygame.Rect(x_taster_minus - 2.5, y_taster_plus_minus - 2.5, breite_taster_plus_minus + 5,
                                     höhe_taster_plus_minus + 5)
            pygame.draw.rect(screen, White, minustaste_preis_je_stunde, 4)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    variable_für_kosten -= 0.5

        plustaste_je_stunde = pygame.Rect(x_taster_minus + abstand_der_taster_x,
                                                       y_taster_plus_minus + abstand_der_taster_y*2,
                                                       breite_taster_plus_minus, höhe_taster_plus_minus)
        pygame.draw.rect(screen, GRUEN, plustaste_je_stunde, 0)
        if x > x_taster_minus + abstand_der_taster_x and x < x_taster_minus + breite_taster_plus_minus + abstand_der_taster_x and y > y_taster_plus_minus + abstand_der_taster_y*2 and y < y_taster_plus_minus + höhe_taster_plus_minus + abstand_der_taster_y*2:
            plustaste = pygame.Rect(x_taster_minus - 2.5 + abstand_der_taster_x, y_taster_plus_minus - 2.5,
                                    breite_taster_plus_minus + 5, höhe_taster_plus_minus + 5)
            pygame.draw.rect(screen, White, plustaste_je_stunde, 4)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    variable_für_kosten += 0.5

        if variable_für_kosten <= 0:
            variable_für_kosten = 0
        if variable_für_kosten >= höchsten_kosten:
            variable_für_kosten = höchsten_kosten

        my_font = pygame.font.Font(None, 45)
        text_surface = my_font.render(str(variable_für_kosten) + '$', True, White)
        text_rect = text_surface.get_rect()
        text_rect.center = (x_taster_minus + breite_taster_plus_minus + (abstand_der_taster_x - breite_taster_plus_minus)/2, y_taster_plus_minus + abstand_der_taster_y*2 + höhe_taster_plus_minus/2 )
        screen.blit(text_surface, text_rect)

        # Hier entstehen die Taster für die Öffnungszeiten
        Öffnungszeiten_Variable_von()
        minustaste_offen = pygame.Rect(x_taster_minus, y_taster_plus_minus + abstand_der_taster_y * 3,
                                                 breite_taster_plus_minus, höhe_taster_plus_minus)
        pygame.draw.rect(screen, RED, minustaste_offen, 0)
        if x > x_taster_minus and x < x_taster_minus + breite_taster_plus_minus and y > y_taster_plus_minus + abstand_der_taster_y * 3 and y < y_taster_plus_minus + höhe_taster_plus_minus + abstand_der_taster_y * 3:
            minustaste = pygame.Rect(x_taster_minus - 2.5, y_taster_plus_minus - 2.5, breite_taster_plus_minus + 5,
                                     höhe_taster_plus_minus + 5)
            pygame.draw.rect(screen, White, minustaste_offen, 4)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    variable_öffnungszeit -= 0.5

        plustaste_offen = pygame.Rect(x_taster_minus + abstand_der_taster_x,
                                          y_taster_plus_minus + abstand_der_taster_y * 3,
                                          breite_taster_plus_minus, höhe_taster_plus_minus)
        pygame.draw.rect(screen, GRUEN, plustaste_offen, 0)
        if x > x_taster_minus + abstand_der_taster_x and x < x_taster_minus + breite_taster_plus_minus + abstand_der_taster_x and y > y_taster_plus_minus + abstand_der_taster_y * 3 and y < y_taster_plus_minus + höhe_taster_plus_minus + abstand_der_taster_y * 3:
            plustaste = pygame.Rect(x_taster_minus - 2.5 + abstand_der_taster_x, y_taster_plus_minus - 2.5,
                                    breite_taster_plus_minus + 5, höhe_taster_plus_minus + 5)
            pygame.draw.rect(screen, White, plustaste_offen, 4)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    variable_öffnungszeit += 0.5

        if variable_öffnungszeit <= 0:
            variable_öffnungszeit = 00.00
        if variable_öffnungszeit >= letzte_öffnung:
            variable_öffnungszeit = letzte_öffnung

        my_font = pygame.font.Font(None, 45)
        text_surface = my_font.render(str(variable_öffnungszeit) + 'Uhr', True, White)
        text_rect = text_surface.get_rect()
        text_rect.center = (
        x_taster_minus + breite_taster_plus_minus + (abstand_der_taster_x - breite_taster_plus_minus) / 2,
        y_taster_plus_minus + abstand_der_taster_y * 3 + höhe_taster_plus_minus / 2)
        screen.blit(text_surface, text_rect)


        #ab hier Schließungszeit
        Öffnungszeiten_Variable_bis()
        minustaste_geschlossen = pygame.Rect(x_taster_minus + abstand_zw_zwei_plus_minus, y_taster_plus_minus + abstand_der_taster_y * 3,
                                       breite_taster_plus_minus, höhe_taster_plus_minus)
        pygame.draw.rect(screen, RED, minustaste_geschlossen, 0)
        if x > x_taster_minus  + abstand_zw_zwei_plus_minus and x < x_taster_minus + breite_taster_plus_minus + abstand_zw_zwei_plus_minus and y > y_taster_plus_minus + abstand_der_taster_y * 3 and y < y_taster_plus_minus + höhe_taster_plus_minus + abstand_der_taster_y * 3:
            minustaste = pygame.Rect(x_taster_minus - 2.5, y_taster_plus_minus - 2.5, breite_taster_plus_minus + 5,
                                     höhe_taster_plus_minus + 5)
            pygame.draw.rect(screen, White, minustaste_geschlossen, 4)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    variable_schließzeit -= 0.5


        plustaste_geschlossen = pygame.Rect(x_taster_minus + abstand_der_taster_x + abstand_zw_zwei_plus_minus,
                                      y_taster_plus_minus + abstand_der_taster_y * 3,
                                      breite_taster_plus_minus, höhe_taster_plus_minus)
        pygame.draw.rect(screen, GRUEN, plustaste_geschlossen, 0)
        if x > x_taster_minus + abstand_der_taster_x + abstand_zw_zwei_plus_minus and x < x_taster_minus + breite_taster_plus_minus + abstand_der_taster_x + abstand_zw_zwei_plus_minus and y > y_taster_plus_minus + abstand_der_taster_y * 3 and y < y_taster_plus_minus + höhe_taster_plus_minus + abstand_der_taster_y * 3:
            plustaste = pygame.Rect(x_taster_minus - 2.5 + abstand_der_taster_x, y_taster_plus_minus - 2.5,
                                    breite_taster_plus_minus + 5, höhe_taster_plus_minus + 5)
            pygame.draw.rect(screen, White, plustaste_geschlossen, 4)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    variable_schließzeit += 0.5

        if variable_schließzeit <= 1:
            variable_schließzeit = 01.00
        if variable_schließzeit >= letzte_schließzeit:
            variable_schließzeit = letzte_schließzeit

        if variable_öffnungszeit == variable_schließzeit:
            variable_schließzeit += 0.5

        my_font = pygame.font.Font(None, 45)
        text_surface = my_font.render(str(variable_schließzeit) + 'Uhr', True, White)
        text_rect = text_surface.get_rect()
        text_rect.center = (
        x_taster_minus + breite_taster_plus_minus*2 + (abstand_der_taster_x-breite_taster_plus_minus) + (abstand_zw_zwei_plus_minus - breite_taster_plus_minus-abstand_der_taster_x) + (breite_taster_plus_minus + abstand_der_taster_x)/2,
        y_taster_plus_minus + abstand_der_taster_y * 3 + höhe_taster_plus_minus / 2)
        screen.blit(text_surface, text_rect)

        pygame.draw.rect(screen, White, (x - 5, y - 5, 10, 10,), 0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runningsetting = False


        pygame.display.update()











oberflaeche_menue()





