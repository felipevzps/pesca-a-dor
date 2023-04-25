from pyautogui import *
import pyautogui
from time import sleep
import time
import my_keyboard
import keyboard
import threading

#req
#pip install pyautogui
#pip install keyboard
#pip install Pillow
#pip install opencv-python

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

pyautogui.PAUSE = 0.01 #diminuindo pause, default = 0.1

#IMG PATH
bubble_img='bubble_1024x768_vermilion.PNG'
bar_img='bar_1024x768.PNG'
fish_img='fish_1024x768.PNG'
shiny_img='shiny_1024x768.PNG'
krabby_img='krabby_1024x768.PNG'
tentacool_img='tentacool_1024x768.PNG'
hungry_img='hungry_1024x768.PNG'

FISHING_POSITIONS = (514, 382) #viridian
IMG_BUBBLE_SIZE = (25,28)
MINIGAME_REGION_BAR = (190,478,15,42)
MINIGAME_REGION_FISH = (189,241,13,21)
HOOK_REGION = (557,312,21,21)

def set_fishing_rod():
    area = FISHING_POSITIONS
    area_center = pyautogui.center(area+IMG_BUBBLE_SIZE)
    sleep(1)
    pyautogui.moveTo(area_center)
    my_keyboard.press('NUNLOCK')
    return area

def wait_bubble(fishing_position):
    while True:
        bubble = pyautogui.locateOnScreen(bubble_img, confidence=0.7, region=fishing_position+IMG_BUBBLE_SIZE)
        if bubble != None:
            my_keyboard.press('NUNLOCK')
            break

def minigame():
    sleep(1)
    fish = True
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    max_attempts = 10
    attempts = 0
    while fish != None:
        bar = pyautogui.locateOnScreen(bar_img, confidence=0.7)
        fish = pyautogui.locateOnScreen(fish_img, confidence=0.7, grayscale=True)
        if bar != None and fish != None:
            print(current_time, ': solving puzzle. . .')
            if bar.top > fish.top:
                my_keyboard.key_down(0x39)
            else:
                my_keyboard.release_key(0x39)
        else:
            my_keyboard.key_down(0x39)
            my_keyboard.release_key(0x39)
            attempts += 1
    if attempts == max_attempts:
        print("Não foi possível encontrar a imagem 'fish_img' na tela.")

def kill_shiny():
    sleep(1)
    shiny = True
    while shiny != None:
        shiny = pyautogui.locateOnScreen(shiny_img, confidence=0.9)
        if shiny != None:
            #my_keyboard.press('backspace') # Use medicine on pokémon
            #sleep(0.1)
            #my_keyboard.press('F7') # Mamaragan
            #my_keyboard.press('F4') # Swords Dance
            #sleep(0.1)
            #my_keyboard.press('F7') # Discharge / Air Slash
            #sleep(0.1)
            #my_keyboard.press('F8') 
            #sleep(0.1)
            #my_keyboard.press('F5')
            #sleep(0.1)
            #ball_tentacool()
            #ball_krabby()
            break
        else:
            break

def ball_tentacool():
    #sleep(0.5)
    print('ball_tentacool activated')
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    tentacool = True
    while tentacool != None:
        tentacool = pyautogui.locateOnScreen(tentacool_img, confidence=0.9)
        if tentacool != None:
            tentacool_center = pyautogui.center(tentacool)
            pyautogui.moveTo(tentacool_center)
            sleep(0.2)
            my_keyboard.press('F11')
            print(current_time,': Shiny Tentacool defeated!')
            sleep(0.2)
            mouseDown(tentacool.left, tentacool.top)
            mouseUp()
            ##set_fishing_rod()
            break

def ball_krabby():
    #sleep(0.5)
    print('ball_krabby activated')
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    krabby = True
    while krabby != None:
        krabby = pyautogui.locateOnScreen(krabby_img, confidence=0.7)
        if krabby != None:
            krabby_center = pyautogui.center(krabby)
            pyautogui.moveTo(krabby_center)
            sleep(0.2)
            my_keyboard.press('F12')
            print(current_time,': Shiny Krabby defeated!')
            sleep(0.2)
            mouseDown(krabby.left, krabby.top)
            mouseUp()
            ##set_fishing_rod()
            break

def ball_shiny():
    #sleep(2)
    ball_tentacool()
    ball_krabby()

def some_actions():
    #sleep(2)
    feed_pokemon()
    my_keyboard.press('esc')
    sleep(1)
    my_keyboard.press('tab')

def feed_pokemon():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    while True:
        hungry = pyautogui.locateOnScreen(hungry_img, confidence=0.9, region=(982,99,17,20))
        if hungry != None:
            print(current_time,': Feeding pokémon...')
            my_keyboard.press('caps')
            #sleep(2)
            set_fishing_rod()
            break
        else:
            break

def pescar():
    fishing_position = set_fishing_rod()
    wait_bubble(fishing_position)
    minigame()

keyboard.wait('p')

print(current_time, ": Started fishing")

threadBallShiny = threading.Thread(target=ball_shiny)
threadBallShiny.start()

threadSomeActions = threading.Thread(target=some_actions)
threadSomeActions.start()

#threadPescar = threading.Thread(target=pescar)
#threadPescar.start()

while True:
    print(". . .")
    sleep(0.5)
    fishing_position = set_fishing_rod()
    wait_bubble(fishing_position)
    if not threadBallShiny.is_alive():
        threadBallShiny = threading.Thread(target=ball_shiny)
        threadBallShiny.start()
    if not threadSomeActions.is_alive():
        threadSomeActions = threading.Thread(target=some_actions)
        threadSomeActions.start()
    minigame()




    
    #Conferir threads ativas. Aparentemente usa as duas threads (threadBallShiny e threadSomeActions) e logo finaliza. Sem problemas eu acho
    #threas_ativas = threading.enumerate()
    #print('Threads ativas:')
    #for thread in threas_ativas:
    #    print(thread.name, thread.ident, thread.is_alive())