import datetime
import time
import pygame
import random
#import asyncio
#import sys
from pygame.locals import *
import pygame
from datetime import date

pygame.init()
#Bildschirmgroeße
BREITE = 1400
HÖHE = 750

date = str(date.today())
nowtime = datetime.datetime.now()
nur_zeit = str(nowtime.strftime("%H:%M"))
#Farben
GRUEN = (0, 255, 0)
farbe = BLACK = (0,0,0)
White = weiß = (255,255,255)
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

#startvariablen
variable_für_anzahl_der_parkplätze = 10
variable_für_anzahl_der_behinderten_parkplätze = 0
variable_für_kosten = 0
variable_öffnungszeit = 00.00
variable_schließzeit = 01.00

#höchste Anzahl der Variablen
höchste_anzahl_parkplätze = 120
höchste_anzahl_behinderten_parkplätze = 12
höchsten_kosten = 10
letzte_öffnung = 23.00
letzte_schließzeit = 24.00

#Hier werden die Taster definiert (Settings)
x_taster_minus = 550
y_taster_plus_minus = 220
breite_taster_plus_minus = 100
höhe_taster_plus_minus = 50
abstand_der_taster_x = 230
abstand_der_taster_y = 100
abstand_zw_zwei_plus_minus = 450

# Koordinaten Anzeigefenster
x_anzeigefenster = 1100
y_anzeigefenster = 0
breite_anzeigefenster = 300
hohe_anzeigefenster = 410

# Koordinaten Zurückfenster
x_zurückfenster = 1100
y_zurückfenster = 470
breite_zurückfenster = 300
hohe_zurückfenster = 400

# Koordinaten Rand Links
x_Rand1 = 0
y_Rand1 = 0
breite_Rand1 = 100
hohe_Rand1 = 300
x_Rand2 = 0
y_Rand2 = 350
breite_Rand2 = 100
hohe_Rand2 = 400

# Koordinaten Rand oben
x_Rand_oben = 30
y_Rand_oben = 0
hohe_Rand_oben = 20
breite_Rand_oben = 1350

#Koordinaten Rand unten
x_Rand_unten = 30
y_Rand_unten = 630
hohe_Rand_unten = 130
breite_Rand_unten = 1350

# Parkplatz maße
hohe_Parkplatz = 60
breite_Parkplatz = 40
breite_Straße = 50
x_Parkplatz1 = breite_Straße + breite_Rand1
y_Parkplatz1 = 240

# variable auto
extras = ['family', 'handycaped']
carsize = (60, 30)
lcarsize, bcarsize = carsize
autobilder = ['whitecar.jpg', 'redcar.png'] #die Bilder müssen ein Seitenverhältnis von 2,25 haben
carcolours = []

# variable parkdauer
zeittraffer = 120
hins = 3600  # StundeinSekunde(3600)
minparkdauer = hins/4 # 15 min in s
maxparkdauer = 4 * hins # 12h in s
#variable spawntime
minspawntime = 1*hins/60 # min 1 min zwischen spawns
maxspawntime = 15*(hins/60) # max 15 min zwischen spawns

# variable parken
maxplaetze_pro_reihe = 20
einfahrtslaenge = breite_Rand1
xeinfahrt = 0
yeinfahrt = (y_Rand1 + hohe_Rand1) + (y_Rand2 - (y_Rand1 + hohe_Rand1)) / 2 - bcarsize / 2
xendestrase = x_Parkplatz1 + (breite_Parkplatz + 3) * 20 + breite_Straße // 2
xausfahrt = BREITE - lcarsize
yausfahrt = yeinfahrt + (breite_Straße + hohe_Parkplatz)
Parkplatz_list = []
Parkplatz_list_extra = []
Parkplatz_list_extra_vorhanden = []
Parkplatz_list_vorhanden = []
belegt = []
belegt_extra = []

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
def display_message_setting_in_setting(msg='SETTINGS'):
    my_font = pygame.font.Font(None, 100)
    text_surface = my_font.render(msg, True, White)
    text_rect = text_surface.get_rect()
    text_rect.center = (x_button + breit_Botton/2, y_zurück+50 + hohe_button/2)
    screen.blit(text_surface, text_rect)
def display_message_info(msg='INFO'):
    my_font = pygame.font.Font(None, 100)
    text_surface = my_font.render(msg, True, White)
    text_rect = text_surface.get_rect()
    text_rect.center = (x_button + breit_Botton/2, y_button_info + hohe_button/2)
    screen.blit(text_surface, text_rect)
def display_message_info_in_Info(msg='INFO'):
    my_font = pygame.font.Font(None, 100)
    text_surface = my_font.render(msg, True, White)
    text_rect = text_surface.get_rect()
    text_rect.center = (x_button + breit_Botton/2, y_zurück+50 + hohe_button/2)
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
def display_message_Info_Text_Zeile1(msg='Dies ist eine Parkhaus Simulation. Mit dieser lässt sich ein Tag in einem Parkhaus nachstellen.'):
    my_font = pygame.font.Font(None, 30)
    text_surface = my_font.render(msg, True, White)
    text_rect = text_surface.get_rect()
    text_rect.center = (x_button + breit_Botton/2,250)
    screen.blit(text_surface, text_rect)
def display_message_Info_Text_Zeile2(msg='Man kann in den Einstellungen einstellen, wie lange das Parkhaus geöffnet sein soll,'):
    my_font = pygame.font.Font(None, 30)
    text_surface = my_font.render(msg, True, White)
    text_rect = text_surface.get_rect()
    text_rect.center = (x_button + breit_Botton/2,300)
    screen.blit(text_surface, text_rect)
def display_message_Info_Text_Zeile3(msg='wie viele Parkplätze und Behindertenparkplätze es geben soll'):
    my_font = pygame.font.Font(None, 30)
    text_surface = my_font.render(msg, True, White)
    text_rect = text_surface.get_rect()
    text_rect.center = (x_button + breit_Botton/2,330)
    screen.blit(text_surface, text_rect)
def display_message_Info_Text_Zeile4(msg='und wie viel dies je Stunde kosten soll.'):
    my_font = pygame.font.Font(None, 30)
    text_surface = my_font.render(msg, True, White)
    text_rect = text_surface.get_rect()
    text_rect.center = (x_button + breit_Botton/2,360)
    screen.blit(text_surface, text_rect)
def display_message_Info_Text_Zeile5(msg='Im Anschluss kann man beobachten wie die Autos in das Parkhaus hineinfahren,'):
    my_font = pygame.font.Font(None, 30)
    text_surface = my_font.render(msg, True, White)
    text_rect = text_surface.get_rect()
    text_rect.center = (x_button + breit_Botton/2,390)
    screen.blit(text_surface, text_rect)
def display_message_Info_Text_Zeile6(msg='wie sie auf dem Parkplatz stehen, wie dad verdiente Geld ansteigt,'):
    my_font = pygame.font.Font(None, 30)
    text_surface = my_font.render(msg, True, White)
    text_rect = text_surface.get_rect()
    text_rect.center = (x_button + breit_Botton/2,420)
    screen.blit(text_surface, text_rect)
def display_message_Info_Text_Zeile7(msg='und wie die Autos wieder hinausfahren.'):
    my_font = pygame.font.Font(None, 30)
    text_surface = my_font.render(msg, True, White)
    text_rect = text_surface.get_rect()
    text_rect.center = (x_button + breit_Botton/2,450)
    screen.blit(text_surface, text_rect)
def display_message_Info_Text_Zeile8(msg='Ersteller des Programms: Steffen Diehl, Tom Böttcher, Daniel Becher'):
    my_font = pygame.font.Font(None, 40)
    text_surface = my_font.render(msg, True, White)
    text_rect = text_surface.get_rect()
    text_rect.center = (x_button + breit_Botton/2,530)
    screen.blit(text_surface, text_rect)
def zurück_in_box(msg='zurück'):
    my_font = pygame.font.Font(None, 30)
    text_surface = my_font.render(msg, True, White)
    text_rect = text_surface.get_rect()
    text_rect.center = (x_zurück + breite_zurück/2, y_zurück + höhe_zurück/2 )
    screen.blit(text_surface, text_rect)
def uhrzeit(msg='Uhrzeit: ' + nur_zeit + ' Uhr'):
    my_font = pygame.font.Font(None, 40)
    text_surface = my_font.render(msg, True, White)
    text_rect = text_surface.get_rect()
    text_rect.center = (1160, 300)
    screen.blit(text_surface, text_rect)
def datum(msg='Datum: '+ date):
    my_font = pygame.font.Font(None, 40)
    text_surface = my_font.render(msg, True, White)
    text_rect = text_surface.get_rect()
    text_rect.center = (1250, 40 )
    screen.blit(text_surface, text_rect)
def variable_in_zeit_konvertieren(number):
    hour = int(number)
    minute = int((number - hour) * 60)
    return f"{hour:02d}:{minute:02d}"
def minus_parkplätze(msg='-'):
    my_font = pygame.font.Font(None, 70)
    text_surface = my_font.render(msg, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.center = (x_taster_minus + breite_taster_plus_minus/2, y_taster_plus_minus + höhe_taster_plus_minus/2 )
    screen.blit(text_surface, text_rect)
def plus_parkplätze(msg='+'):
    my_font = pygame.font.Font(None, 70)
    text_surface = my_font.render(msg, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.center = (x_taster_minus + abstand_der_taster_x + breite_taster_plus_minus/2, y_taster_plus_minus + höhe_taster_plus_minus/2 )
    screen.blit(text_surface, text_rect)
def minus_b_parkplätze(msg='-'):
    my_font = pygame.font.Font(None, 70)
    text_surface = my_font.render(msg, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.center = (x_taster_minus + breite_taster_plus_minus/2, y_taster_plus_minus + abstand_der_taster_y + höhe_taster_plus_minus/2 )
    screen.blit(text_surface, text_rect)
def plus_b_parkplätze(msg='+'):
    my_font = pygame.font.Font(None, 70)
    text_surface = my_font.render(msg, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.center = (x_taster_minus + abstand_der_taster_x + breite_taster_plus_minus/2, y_taster_plus_minus + abstand_der_taster_y + höhe_taster_plus_minus/2 )
    screen.blit(text_surface, text_rect)
def minus_geldbetrag(msg='-'):
    my_font = pygame.font.Font(None, 70)
    text_surface = my_font.render(msg, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.center = (x_taster_minus + breite_taster_plus_minus/2, y_taster_plus_minus +abstand_der_taster_y*2+ höhe_taster_plus_minus/2 )
    screen.blit(text_surface, text_rect)
def plus_geldbetrag(msg='+'):
    my_font = pygame.font.Font(None, 70)
    text_surface = my_font.render(msg, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.center = (x_taster_minus + abstand_der_taster_x + breite_taster_plus_minus/2, y_taster_plus_minus +abstand_der_taster_y*2+ höhe_taster_plus_minus/2 )
    screen.blit(text_surface, text_rect)
def minus_öffnungszeit(msg='-'):
    my_font = pygame.font.Font(None, 70)
    text_surface = my_font.render(msg, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.center = (x_taster_minus + breite_taster_plus_minus/2, y_taster_plus_minus + abstand_der_taster_y*3 + höhe_taster_plus_minus/2 )
    screen.blit(text_surface, text_rect)
def plus_öffnungszeit(msg='+'):
    my_font = pygame.font.Font(None, 70)
    text_surface = my_font.render(msg, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.center = (x_taster_minus + abstand_der_taster_x + breite_taster_plus_minus/2, y_taster_plus_minus + abstand_der_taster_y*3 + höhe_taster_plus_minus/2 )
    screen.blit(text_surface, text_rect)
def minus_schließzeit(msg='-'):
    my_font = pygame.font.Font(None, 70)
    text_surface = my_font.render(msg, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.center = (x_taster_minus + abstand_zw_zwei_plus_minus + breite_taster_plus_minus/2, y_taster_plus_minus + abstand_der_taster_y*3+ höhe_taster_plus_minus/2 )
    screen.blit(text_surface, text_rect)
def plus_schließzeit(msg='+'):
    my_font = pygame.font.Font(None, 70)
    text_surface = my_font.render(msg, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.center = (x_taster_minus + abstand_der_taster_x + abstand_zw_zwei_plus_minus + breite_taster_plus_minus/2, y_taster_plus_minus + abstand_der_taster_y*3+ höhe_taster_plus_minus/2 )
    screen.blit(text_surface, text_rect)
def oberflaeche_menue():
    global farbe
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
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    farbe = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255),)

        (x, y) = pygame.mouse.get_pos()
        pygame.draw.rect(screen, White, (x-5, y-5, 10, 10,), 0)

        if x > x_button and x < x_button + breit_Botton and y > y_button_play and y < y_button_play + hohe_button:
            button_play = pygame.Rect(x_button - 10, y_button_play - 10, breit_Botton + 20, hohe_button + 20)
            pygame.draw.rect(screen, White, button_play, 10)
            if event.type == MOUSEBUTTONDOWN:
                running = False
                parkhaus_oberflaeche()

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
            if event.type == MOUSEBUTTONDOWN:
                Info()
                running = False
        else:
            button_info = pygame.Rect(x_button, y_button_info, breit_Botton, hohe_button)



        if x > x_button and x < x_button + breit_Botton and y > y_buuton_exit and y < y_buuton_exit + hohe_button:
            button_exit = pygame.Rect(x_button - 10, y_buuton_exit - 10, breit_Botton + 20, hohe_button + 20)
            pygame.draw.rect(screen, White, button_exit, 10)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    running = False
                    quit()
        else:
            button_exit = pygame.Rect(x_button, y_buuton_exit, breit_Botton, hohe_button)

        pygame.display.update()
def Info():
    runningsinfo = True
    while runningsinfo:
        screen.fill(farbe)

        zurück = pygame.Rect(x_zurück, y_zurück, breite_zurück, höhe_zurück)
        pygame.draw.rect(screen, RED, zurück, 0)
        zurück_in_box()

        #Hier steht noch einmal Info als Überschrift
        button_info = pygame.Rect(x_button, y_zurück+50, breit_Botton, hohe_button)
        pygame.draw.rect(screen, YELLOW, button_info, 0)
        button_info = pygame.Rect(x_button - 10, y_zurück+50 - 10, breit_Botton + 20, hohe_button + 20)
        pygame.draw.rect(screen, White, button_info, 10)
        display_message_info_in_Info()

        #Hier entsteht die Maus
        (x, y) = pygame.mouse.get_pos()

        #Hier wird überprüft, ob die Taste zurück gefrückt wird
        if x > x_zurück and x < x_zurück + breite_zurück and y > y_zurück and y < y_zurück + höhe_zurück:
            button_exit = pygame.Rect(x_zurück - 10, y_zurück - 10, breite_zurück + 20, höhe_zurück + 20)
            pygame.draw.rect(screen, White, zurück, 4)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    runningsinfo = False
                    oberflaeche_menue()

        # Hier wird die große Box gebaut
        große_box = pygame.Rect(30, y_taster_plus_minus - 50, BREITE - 60, 450)
        pygame.draw.rect(screen, YELLOW, große_box)

        #Hier wird eine kleine Box über die andere gebaut
        kleine_box = pygame.Rect(30+50, y_taster_plus_minus , BREITE - 160, 350)
        pygame.draw.rect(screen, BLACK, kleine_box)

        #Hier kommen die Funktionen mit unserem text
        display_message_Info_Text_Zeile1()
        display_message_Info_Text_Zeile2()
        display_message_Info_Text_Zeile3()
        display_message_Info_Text_Zeile4()
        display_message_Info_Text_Zeile5()
        display_message_Info_Text_Zeile6()
        display_message_Info_Text_Zeile7()
        display_message_Info_Text_Zeile8()

        #Maus
        pygame.draw.rect(screen, White, (x-5, y-5, 10, 10,), 0)

        #Programm schließen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runningsinfo = False
                quit()


        pygame.display.update()
def settings():
    runningsetting = True

    #zeit zwischen dem Drücken einer taste bei plus und minus
    import time
    delay = 0.1

    # variablen
    global variable_für_anzahl_der_parkplätze
    global variable_für_anzahl_der_behinderten_parkplätze
    global variable_für_kosten
    global variable_öffnungszeit
    global variable_schließzeit

    #höchste Anzahl der Variablen
    global höchste_anzahl_parkplätze
    global höchste_anzahl_behinderten_parkplätze
    global höchsten_kosten
    global letzte_öffnung
    global letzte_schließzeit

    while runningsetting:
        #Bildschirmfarbe/Hintergrundfarbe
        screen.fill(farbe)
        höchste_anzahl_behinderten_parkplätze =  2*(variable_für_anzahl_der_parkplätze//20)

        zurück = pygame.Rect(x_zurück, y_zurück, breite_zurück, höhe_zurück)
        pygame.draw.rect(screen, RED, zurück, 0)
        zurück_in_box()

        #maus im Spiel(Reckteck)
        (x, y) = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                quit()

            #Hier wird geschaut, ob die Maus auf dem knopf ist und ggf. drückt
            if x > x_zurück and x < x_zurück + breite_zurück and y > y_zurück and y < y_zurück + höhe_zurück:
                button_exit = pygame.Rect(x_zurück - 10, y_zurück - 10, breite_zurück + 20, höhe_zurück + 20)
                pygame.draw.rect(screen, White, zurück, 4)
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        runningsetting = False
                        oberflaeche_menue()

            # Hier steht noch einmal Einstellung über allem
            button_settings = pygame.Rect(x_button - 10, y_zurück+50 - 10, breit_Botton + 20, hohe_button + 20)
            pygame.draw.rect(screen, White, button_settings, 10)
            button_settings = pygame.Rect(x_button, y_zurück+50, breit_Botton, hohe_button)
            pygame.draw.rect(screen, BLUE, button_settings, 0)
            display_message_setting_in_setting()

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
                        variable_für_anzahl_der_parkplätze -= 5
                        time.sleep(delay)


            plustaste_parkplätze = pygame.Rect(x_taster_minus + abstand_der_taster_x, y_taster_plus_minus, breite_taster_plus_minus, höhe_taster_plus_minus)
            pygame.draw.rect(screen, GRUEN, plustaste_parkplätze, 0)
            if x > x_taster_minus + abstand_der_taster_x and x < x_taster_minus + breite_taster_plus_minus + abstand_der_taster_x and y > y_taster_plus_minus and y < y_taster_plus_minus + höhe_taster_plus_minus:
                plustaste = pygame.Rect(x_taster_minus - 2.5 + abstand_der_taster_x, y_taster_plus_minus - 2.5, breite_taster_plus_minus + 5, höhe_taster_plus_minus + 5)
                pygame.draw.rect(screen, White, plustaste_parkplätze, 4)
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        variable_für_anzahl_der_parkplätze += 5
                        time.sleep(delay)


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
                        variable_für_anzahl_der_behinderten_parkplätze -= 2
                        time.sleep(delay)

            plustaste_behinderten_parkplätze = pygame.Rect(x_taster_minus + abstand_der_taster_x, y_taster_plus_minus + abstand_der_taster_y, breite_taster_plus_minus, höhe_taster_plus_minus)
            pygame.draw.rect(screen, GRUEN, plustaste_behinderten_parkplätze, 0)
            if x > x_taster_minus + abstand_der_taster_x and x < x_taster_minus + breite_taster_plus_minus + abstand_der_taster_x and y > y_taster_plus_minus + abstand_der_taster_y and y < y_taster_plus_minus + höhe_taster_plus_minus + abstand_der_taster_y:
                plustaste = pygame.Rect(x_taster_minus - 2.5 + abstand_der_taster_x, y_taster_plus_minus - 2.5,
                                        breite_taster_plus_minus + 5, höhe_taster_plus_minus + 5)
                pygame.draw.rect(screen, White, plustaste_behinderten_parkplätze, 4)
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        variable_für_anzahl_der_behinderten_parkplätze += 2
                        time.sleep(delay)

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
                        time.sleep(delay)

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
                        time.sleep(delay)

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
                        time.sleep(delay)

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
                        time.sleep(delay)

            if variable_öffnungszeit <= 0:
                variable_öffnungszeit = 00.00
            if variable_öffnungszeit >= letzte_öffnung:
                variable_öffnungszeit = letzte_öffnung


            variable_als_zeit =str(variable_in_zeit_konvertieren(variable_öffnungszeit))

            my_font = pygame.font.Font(None, 40)
            text_surface = my_font.render(str(variable_als_zeit) + 'Uhr', True, White)
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
                        time.sleep(delay)


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
                        time.sleep(delay)

            if variable_schließzeit <= 1:
                variable_schließzeit = 01.00
            if variable_schließzeit >= letzte_schließzeit:
                variable_schließzeit = letzte_schließzeit

            if variable_öffnungszeit == variable_schließzeit:
                variable_schließzeit += 0.5

            variable_als_zeit_bei_schließung = str(variable_in_zeit_konvertieren(variable_schließzeit))

            my_font = pygame.font.Font(None, 40)
            text_surface = my_font.render(str(variable_als_zeit_bei_schließung) + 'Uhr', True, White)
            text_rect = text_surface.get_rect()
            text_rect.center = (
            x_taster_minus + breite_taster_plus_minus*2 + (abstand_der_taster_x-breite_taster_plus_minus) + (abstand_zw_zwei_plus_minus - breite_taster_plus_minus-abstand_der_taster_x) + (breite_taster_plus_minus + abstand_der_taster_x)/2,
            y_taster_plus_minus + abstand_der_taster_y * 3 + höhe_taster_plus_minus / 2)
            screen.blit(text_surface, text_rect)

            plus_parkplätze()
            plus_b_parkplätze()
            plus_geldbetrag()
            plus_öffnungszeit()
            plus_schließzeit()
            minus_parkplätze()
            minus_b_parkplätze()
            minus_geldbetrag()
            minus_öffnungszeit()
            minus_schließzeit()

            #Maus
            pygame.draw.rect(screen, White, (x - 5, y - 5, 10, 10,), 0)

            #for event in pygame.event.get():
             #   if event.type == pygame.QUIT:
              #      runningsetting = False


            pygame.display.update()
def spawncar(): #erstelle ein Auto
    global carsinlot, starttime
    timer = random.randint(minparkdauer, maxparkdauer) #zufällige Parkzeit
    starttime = time.time()  # Zeitpunkt einfahrt
    endtime = starttime + timer  # Zeitpunkt ausfahrt
    carimage = random.choice(carcolours)  # zufällige autofarbe
    extra = situation()  # anspruch auf sonderparkplatz
    car = cars(timer, starttime, endtime, 0, (0, 0), carimage, extra) #erstelle das Auto
    Parkplatzanzahl_ohne_extra = variable_für_anzahl_der_parkplätze - variable_für_anzahl_der_behinderten_parkplätze
    if car.extra in extras: #prüfe ob es ein recht auf Sonderparkplätze hat
        if len(belegt_extra) < variable_für_anzahl_der_behinderten_parkplätze: #prüfe ob es noch Sonderparkplätze gibt
            while True:
                car.lotnumber = random.choice(Parkplatz_list_extra_vorhanden)
                if car.lotnumber not in belegt_extra: #prüfe ob der zugewiesene Sonderparkplatz belegt ist
                    belegt_extra.append(car.lotnumber)
                    break
        else:
            while True:
                car.lotnumber = random.choice(Parkplatz_list_vorhanden)
                if car.lotnumber not in belegt: #prüfe ob der zugewiesene Parkplatz belegt ist
                    belegt.append(car.lotnumber)
                    break
    else:
        while True: #prüfe ob der zugewiesene Parkplatz belegt ist
            car.lotnumber = random.choice(Parkplatz_list_vorhanden)
            if car.lotnumber not in belegt:
                belegt.append(car.lotnumber)
                break
    carsinlot.append(car)
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
    spalte = get_car.lotnumber % maxplaetze_pro_reihe
    if spalte == 0:
        spalte = 20
        reihe -= 1
    fahrrichtung = 1
    if reihe == 3: #reihe oben
        meinestrase = 2
        fahrrichtung = -1
        parkrichtung = -1
    elif reihe == 2: #2. reihe von oben
        meinestrase = 1
        fahrrichtung = -1
        parkrichtung = -1
    elif reihe == 0: #reihe mitte
        meinestrase = 1
        fahrrichtung = -1
        parkrichtung = 1
    elif reihe == 1: #2. reihe von unten
        meinestrase = 0
        fahrrichtung = 0
        parkrichtung = 1
    elif reihe == 4: #2. reihe unten
        meinestrase = 1
        fahrrichtung = 1
        parkrichtung = 1
    elif reihe == 5: # reihe unten
        meinestrase = 2
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
    self_rect.y = ydrive #fahre bis du die Straße, in der dein Parkplatz liegt erreichst
    screen.blit(self, self_rect)
    self = pygame.transform.rotate(self, 90 * fahrrichtung)
    self_rect.x = xdrive #fahre bis du deinen Parkplatz erreicht hast
    screen.blit(self, self_rect)
    self = pygame.transform.rotate(self, -90) #parke ein
    self_rect.y += ((hohe_Parkplatz - lcarsize // 2 + breite_Straße // 2) * parkrichtung - bcarsize // 2)
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
    self_rect.y -= ((hohe_Parkplatz - lcarsize // 2 + breite_Straße // 2) * parkrichtung - bcarsize // 2) #parke aus
    screen.blit(self, self_rect)
    self = pygame.transform.rotate(self, 90 * parkrichtung)
    self_rect.x = xendestrase #fahre bis ans Ende der Straße
    screen.blit(self, self_rect)
    self = pygame.transform.rotate(self, 90 * fahrrichtung)
    self_rect.y = yausfahrt #fahre bis du die Ausfahrt erreichst
    screen.blit(self, self_rect)
    self = pygame.transform.rotate(self, -90 * fahrrichtung * parkrichtung)
    self_rect.x = xausfahrt #fahre zur Ausfahrt raus
    screen.blit(self, self_rect)
    return (self_rect.x, self_rect.y), self
def pay(car, oldrevenue): #leider musst auch du zahlen
    hours = car.cartimer // hins #wie lange hast du geparkt
    if hours < car.cartimer / hins:
        hours += 1 #angefangene Stunden müssen voll gezahlt werden
    amounttopay = hours * variable_für_kosten
    print(f'Sie müssen: {amounttopay} Euro bezahlen')
    newrevenue = oldrevenue + amounttopay #wie viel wurde bisher verdient
    print(f'Ihre Einnahmen sind: {newrevenue} Euro')
    return newrevenue
def deletecar(car): #entferne das Auto aus dem Parkplatz
    if car.lotnumber in belegt:
        belegt.remove(car.lotnumber)
    elif car.lotnumber in belegt_extra:
        belegt_extra.remove(car.lotnumber)
    carsinlot.remove(car)
def genrand():
    pygame.draw.rect(screen, farbe, (x_anzeigefenster, y_anzeigefenster, breite_anzeigefenster, hohe_anzeigefenster))  # Rand rechts oben
    pygame.draw.rect(screen, farbe, (x_Rand1, y_Rand1, breite_Rand1, hohe_Rand1))  # Rand links oben
    pygame.draw.rect(screen, farbe, (x_Rand2, y_Rand2, breite_Rand2, hohe_Rand2))  # Rand links unten
    pygame.draw.rect(screen, farbe, (x_zurückfenster, y_zurückfenster, breite_zurückfenster, hohe_zurückfenster))  # Rand rechts unten
    pygame.draw.rect(screen, farbe, (x_Rand_oben,y_Rand_oben,breite_Rand_oben,hohe_Rand_oben)) # Rand oben
    pygame.draw.rect(screen, farbe, (x_Rand_unten,y_Rand_unten, breite_Rand_unten, hohe_Rand_unten))
def genParkplaetze(j):
    x = 0
    y = 0
    z = 0
    for i in range(variable_für_anzahl_der_parkplätze):
        Px = pygame.draw.rect(screen, White, (x_Parkplatz1 + (breite_Parkplatz + 3) * x, y_Parkplatz1 + y, breite_Parkplatz, hohe_Parkplatz), 2)
        if j == 0:
            Parkplatz_list.append(Px)
        x += 1
        z += 1
        if x == maxplaetze_pro_reihe:
            x = 0
        if z == 60:
            y += -(breite_Straße+hohe_Parkplatz)
        if z == 20 or z == 100:
            y += breite_Straße + hohe_Parkplatz
        if z == 80:
            y += 4* (breite_Straße+hohe_Parkplatz)
        if z== 40:
            y += -(breite_Straße+hohe_Parkplatz)*2



    if j == 0:
        for i in range(variable_für_anzahl_der_behinderten_parkplätze):
            Pex = Parkplatz_list[-1]
            Parkplatz_list_extra.append(Pex)
            Parkplatz_list.remove(Pex)

 #Behinderten Parkplätze

    image = pygame.image.load("behindert.jpg")
    image = image.convert()
    image = pygame.transform.scale(image, (30, 45))

    if variable_für_anzahl_der_behinderten_parkplätze >= 2 and variable_für_anzahl_der_parkplätze >= 2:
        for p in range (2):
            screen.blit(image, (p*43+155,y_Parkplatz1+8))

    if variable_für_anzahl_der_behinderten_parkplätze >= 4 and variable_für_anzahl_der_parkplätze >= 22 :
        for p in range (2):
            screen.blit(image,(p*43+155,y_Parkplatz1+8+breite_Straße+hohe_Parkplatz))

    if variable_für_anzahl_der_behinderten_parkplätze >= 6 and variable_für_anzahl_der_parkplätze >= 42:
        for p in range (2):
            screen.blit(image,(p*43+155,y_Parkplatz1+8-breite_Straße-hohe_Parkplatz))

    if variable_für_anzahl_der_behinderten_parkplätze >= 8 and variable_für_anzahl_der_parkplätze >= 62:
        for p in range (2):
            screen.blit(image,(p*43+155,y_Parkplatz1+8-(2*breite_Straße)-(2*hohe_Parkplatz)))

    if variable_für_anzahl_der_behinderten_parkplätze >= 10 and variable_für_anzahl_der_parkplätze >= 82:
        for p in range (2):
            screen.blit(image,(p*43+155,y_Parkplatz1+8+(2*breite_Straße)+(2*hohe_Parkplatz)))

    if variable_für_anzahl_der_behinderten_parkplätze >= 12 and variable_für_anzahl_der_parkplätze >= 102:
        for p in range (2):
            screen.blit(image,(p*43+155,y_Parkplatz1+8+(3*breite_Straße)+(3*hohe_Parkplatz)))
def genbackground(j):
    screen = pygame.display.set_mode((BREITE, HÖHE))
    screen.fill(GRAY)
    genrand()
    genParkplaetze(j)
    datum()
def parkhaus_oberflaeche():
    global Parkplatz_list_extra_vorhanden, Parkplatz_list_vorhanden, belegt, belegt_extra, carsinlot, Parkplatz_list, Parkplatz_list_extra
    runningspiel = True
    # variablen auto
    carsinlot = []
    starttime = time.time()
    carcounter = 0
    # variablen einnahmen
    revenue = 0
    #variablen parken
    belegt = []
    belegt_extra = []
    Parkplatz_list = []
    Parkplatz_list_extra = []
    nochParkplaetze_frei = True
    Parkplatz_list_extra_vorhanden = []
    Parkplatz_list_vorhanden = []
    carsinlot = []
    screen.fill(farbe)
    genbackground(0)
    for i in range(variable_für_anzahl_der_parkplätze):
        Parkplatz_list_vorhanden.append(i+1)
    reihen_behindert = variable_für_anzahl_der_behinderten_parkplätze//2
    for i in range(reihen_behindert):
        Platz = 1
        Platz += 20*i
        for i in range(2):
            Platz += i
            Parkplatz_list_extra_vorhanden.append(Platz)
            Parkplatz_list_vorhanden.remove(Platz)
    carspawntime = (random.randint(minspawntime, maxspawntime)) / zeittraffer
    while runningspiel:
        genbackground(1)
        zurück = pygame.Rect(x_zurück, y_zurück, breite_zurück, höhe_zurück)
        pygame.draw.rect(screen, RED, zurück, 0)
        zurück_in_box()

        (x, y) = pygame.mouse.get_pos()

        if x > x_zurück and x < x_zurück + breite_zurück and y > y_zurück and y < y_zurück + höhe_zurück:
            button_exit = pygame.Rect(x_zurück - 10, y_zurück - 10, breite_zurück + 20, höhe_zurück + 20)
            pygame.draw.rect(screen, White, zurück, 4)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    runningspiel = False
                    oberflaeche_menue()
        now = time.time()
        secounds = now - starttime
        if len(carsinlot) < variable_für_anzahl_der_parkplätze:#if now != variable_schließzeit and len(carsinlot) < variable_für_anzahl_der_parkplätze:
            nochParkplaetze_frei = True
            if secounds > carspawntime:  # steht ein Auto vor dem Parkhaus
                carspawntime = (random.randint(minspawntime, maxspawntime)) / zeittraffer
                starttime = time.time()
                spawncar()
                carcounter += 1
                car = carsinlot[-1]
                car.carpos, car.image = parkcar(car)
        else:  # können noch Autos in das Parkhaus fahren
            nochParkplaetze_frei = False
            print('Das Parkhaus ist voll!')
            time.sleep(0.1)
        for i in carsinlot:  # welche Autos parken aktuell
            screen.blit(i.image, i.carpos)
            if now > (i.entrietime + i.cartimer / zeittraffer):  # fährt ein Auto raus
                i.carpos, i.image = getcarout(i)
                revenue = pay(i, revenue)
                deletecar(i)
        if now == (variable_schließzeit * hins) / zeittraffer:  # alle Autos müssen raus fahren
            print('Das Parkhaus schliest!')
            for i in carsinlot:
                i.carpos, i.image = getcarout(i)
                revenue = pay(i, revenue)
                deletecar(i)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runningspiel = False
        pygame.display.update()

oberflaeche_menue()