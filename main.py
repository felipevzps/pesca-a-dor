import pyautogui
import random
from time import sleep
import my_keyboard
import keyboard

#bolha do lado esquedo da bola
#minha posição: 3 acima da arvore, 2 esquerda da estrela
#884, top=165, width=90, height=93

#pyautogui.PAUSE = 0.1 # default
pyautogui.PAUSE = 0.01 # tentando rodar mais rapdo

#TODO: encontrar melhores imagens (bolha) e valores de 'confidence'
#+1 Luffynaruto - 2 sqm acima npc Sam
#FISHING_POSITIONS = [(195, 259),(195, 259)]
#IMG_BUBBLE_SIZE = (38,42)
#MINIGAME_REGION_BAR = (190,478,15,42)
#MINIGAME_REGION_FISH = (189,241,13,21)

#-1 Luffynaruto
#FISHING_POSITIONS = [(202, 209),(202, 209)]
#IMG_BUBBLE_SIZE = (38,42)
#MINIGAME_REGION_BAR = (190,478,15,42)
#MINIGAME_REGION_FISH = (189,241,13,21)

#vermilion
FISHING_POSITIONS = [(505, 259),(505, 259)]
IMG_BUBBLE_SIZE = (42,42)

#TODO: encontrar melhores imagens (bolha) e valores de 'confidence'
def set_fishing_rod():
    area = random.choice(FISHING_POSITIONS)
    area_center = pyautogui.center(area+IMG_BUBBLE_SIZE)
    pyautogui.moveTo(area_center)
    sleep(1)
    my_keyboard.press('NUNLOCK')
    return area

def wait_bubble(fishing_position):
    while True:
        bubble = pyautogui.locateOnScreen('bubble_1024_vermilion.PNG', confidence=0.7, region=fishing_position+IMG_BUBBLE_SIZE)
        if bubble != None:
            my_keyboard.press('NUNLOCK')
            break

#TODO: encontrar melhores imagens (barra e peixe) e valores de 'confidence'
#TODO: entender como usar o region pra pegar a imagem mais rapido 
def minigame():
    sleep(1)
    fish = True
    while fish != None:
        bar = pyautogui.locateOnScreen('bar_1024.PNG', confidence=0.7)#, region=MINIGAME_REGION_BAR)
        fish = pyautogui.locateOnScreen('fish_1024_8.PNG', confidence=0.7, grayscale=True)#, region=MINIGAME_REGION_FISH)
        print("bar", bar)
        print("fish", fish)
        if bar != None and fish != None:
            if bar.top > fish.top:
                print('pressing space')
                my_keyboard.key_down(0x39)
            else:
                print('realising space')
                my_keyboard.release_key(0x39)
        else:
            my_keyboard.key_down(0x39)
            my_keyboard.release_key(0x39)

keyboard.wait('p')

while True:
    print("iniciando pesca")
    fishing_position = set_fishing_rod()
    wait_bubble(fishing_position)
    minigame()
    sleep(4)
    my_keyboard.press('tab')
