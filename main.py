import pygame
import time
import random
import sys
speelveld = (24, 24)  # grootte van het speelveld

# ik heb zogenaamde tuples gebruikt in plaats van de vector.
# lees het document wat ik heb gestuurd. wat vooral belangrijk
# is hier, is dat x = [0] en y = [1].
appel=(0,0)
grootte_blokje = 24  # grootte van 1 blokje
framerate = 0.1  # tijd tussen de frames
# speelveld -1, maximum voor 0-based index
speelveld_max = (speelveld[0]-1, speelveld[1]-1)
            # dit is dus x ^      en dit y ^
pygame.init() # initialiseer pygame
pygame.font.init() #initialiseer de pygame font
font = pygame.font.SysFont('calibri', 30, bold=True)  # lettertype
# maak een venster aan: dimensies is het speelveld keer de grootte van een blokje
scherm = pygame.display.set_mode((speelveld[0] * grootte_blokje, speelveld[1] * grootte_blokje))
def sterf():
    global running # zie tick()
    time.sleep(0.5) # wacht om te laten zien dat je het hebt verneukt
    # 23-24: beetje rommelig doen, dit zou in de teken() functie moeten
    scherm.blit(font.render('Je bent dood. Score: ' + str(score), True, (255, 0, 0)), (10, 50))
    pygame.display.flip() 
    time.sleep(1.5) # wacht nog wat langer
    running = False # stop de tick-loop

def tick():
    global richting # 29-32 dit is om duidelijk te maken dat we hier een globale variabele wijzigen.
    global lichaam  # locale variabelen worden in een functie aangemaakt en daarna verwijderd. omdat we nu de
    global appel    # waardes buiten de functie willen aanpassen, moeten we dit erbij schrijven. Deze code
    global score    # schreeuwt om object orientatie, dus is realistisch dat jij het hebt geschreven :)
    if pygame.key.get_pressed()[pygame.K_w] and richting != 2: # als w wordt ingedrukt en we gaan niet omlaag
        richting = 0 # ga omhoog
    elif pygame.key.get_pressed()[pygame.K_d] and richting != 3: # d en niet naar links
        richting = 1 # ga naar links
    elif pygame.key.get_pressed()[pygame.K_s] and richting != 0: # s en niet omhoog
        richting = 2 # ga omlaag
    elif pygame.key.get_pressed()[pygame.K_a] and richting != 1: # a en niet naar rechts
        richting = 3 # ga naar rechts
    elif pygame.key.get_pressed()[pygame.K_UP] and richting != 2: # zelfde riedeltje voor pijltjestoetsen
        richting = 0
    elif pygame.key.get_pressed()[pygame.K_RIGHT] and richting != 3:
        richting = 1
    elif pygame.key.get_pressed()[pygame.K_DOWN] and richting != 0:
        richting = 2
    elif pygame.key.get_pressed()[pygame.K_LEFT] and richting != 1:
        richting = 3
    eind = lichaam[len(lichaam)-1] # onthou de oude plek van het laatste blokje (dat is waar een nieuw
                                   # blokje moet komen als de speler een appel eet)
    # elke keer dat de slang beweegt, krijgt elk blokje de positie van het blokje ervoor.
    for j in range(len(lichaam)-1, 0, -1):
        # dit moet in omgekeerde volgorde gebeuren, anders komen alle blokjes op dezelfde plek te zitten.
        # we stoppen voor i = 0 omdat het eerste blokje in de huidige richting beweegt
        lichaam[j] = lichaam[j-1] # j is het huidige blokje, j - 1 is het blokje 1 hoger in de lijst (aka degene ervoor)

    # nu het hoofd bewegen
    if(richting == 0): # als we omhoog gaan
        lichaam[0] = (lichaam[0][0], lichaam[0][1]-1) # y -1
    if(richting == 1): # als we naar rechts gaan
        lichaam[0] = (lichaam[0][0]+1, lichaam[0][1]) # x +1
    if(richting == 2): # als we omlaag gaan
        lichaam[0] = (lichaam[0][0], lichaam[0][1]+1) # y +1
    if(richting == 3): # als we naar links gaan
        lichaam[0] = (lichaam[0][0]-1, lichaam[0][1]) # x -1
    if(lichaam[0] == appel): # kijk of het hoofd op dezelfe plek is als de appel
        lichaam.append(eind) # zo ja, voeg een nieuw blokje toe op de oude plek van de staart
        score = score + 1 # score + 1
        while(appel in lichaam): # zet de appel op een andere plek (dus niet dezelfde, vandaar de while loop)
            appel = (random.randint(0, speelveld_max[0]), random.randint(0, speelveld_max[1])) 
    for i in range(1, len(lichaam)): # ga langs elk blokje van het lichaam
        if(lichaam[0] == lichaam[i]): # en kijk of ons hoofd op de zelfde plek is
            sterf() # zo ja, dan hebben we onszelf aangeraakt en zijn we DOOD.
    # als we de rand aanraken (dus x < 0 of x > speelveld breedte of y < 0 of y > speelveld grootte)
    # we moeten hier de max gebruiken, want de coordinaten zijn 0-based
    if(lichaam[0][0] < 0 or lichaam[0][0] > speelveld_max[0] or lichaam[0][1] < 0 or lichaam[0][1] > speelveld_max[1]):
        sterf()  # speler gametick

def teken():
    scherm.fill((0, 43, 61)) # vul het scherm met donkerblauw (om vorig frame uit te wissen)
    for i in range(0, len(lichaam)): # voor elk blokje van het lichaam van de speler
        #teken het blokje        kleur (luchtblauw)         x coordinaat                  y coordinaat                  breedte         hoogte
        pygame.draw.rect(scherm, (4, 161, 195), pygame.Rect(lichaam[i][0]*grootte_blokje, lichaam[i][1]*grootte_blokje, grootte_blokje, grootte_blokje))
    #teken de appel          kleur (aquablauw)          x coordinaat             y coordinaat             breedte         hoogte
    pygame.draw.rect(scherm, (0, 255, 255), pygame.Rect(grootte_blokje*appel[0], grootte_blokje*appel[1], grootte_blokje, grootte_blokje))
    #teken de score tekst   tekst                   AA    kleur(aqua)   positie (x, y) [AA = Anti-Aliasing (tegen kartelrandjes)]
    scherm.blit(font.render('Score: ' + str(score), True, (0, 255, 255)), (10, 10))
    pygame.display.flip() # ververs het scherm

while(True): # deze loop herhaalt elke game sessie (begint opnieuw als de speler doodgaat)
    score = 0 # score van de speler
    richting = 0 # richting waarin de speler beweegt. 0 = omhoog, 1 = naar rechts, 2 = omlaag, 3 = naar links
    
    
    #lichaam van de speler. speler begint met 3 segmenten in het midden van het speelveld
    lichaam = [(speelveld[0]/2, speelveld[1]/2), (speelveld[0]/2, speelveld[1]/2+1), (speelveld[0]/2, speelveld[1]/2+2)]
    appel = (random.randint(0, speelveld_max[0]), random.randint(0, speelveld_max[1])) # zet de appel op random plek
    running = True # spel is draaiend
    while running: # gametick loop, herhaalt elke frame / gametick
        tick() # update de speler
        teken() # teken het scherm
        time.sleep(framerate) # wacht framerate seconden
        for event in pygame.event.get(): # pygame.event.get() geeft een lijst met events in het venster
            if event.type == pygame.QUIT: # als een van deze events QUIT is (op kruisje drukken)
                sys.exit(0)  # programma afsluiten
