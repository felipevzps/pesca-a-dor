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

RESOLUTION='1024x768'
FISHING_POSITIONS = (514, 149 )
IMG_BUBBLE_SIZE = (25,28)
MINIGAME_REGION_BAR = (190,478,15,42)
MINIGAME_REGION_FISH = (189,241,57,57)
HOOK_REGION = (553,148,21,21)

#IMG PATH
bubble_img='images/{}/bubble.PNG'.format(RESOLUTION)
bar_img='images/{}/bar.PNG'.format(RESOLUTION)
fish_img='images/{}/fish_bin.PNG'.format(RESOLUTION)
shiny_img='images/{}/shiny.PNG'.format(RESOLUTION)
krabby_img='images/{}/krabby.PNG'.format(RESOLUTION)
tentacool_img='images/{}/tentacool.PNG'.format(RESOLUTION)
hungry_img='images/{}/hungry.PNG'.format(RESOLUTION)
hook_img='images/{}/hook.PNG'.format(RESOLUTION)

octillery_img='images/{}/octillery.PNG'.format(RESOLUTION)
cloyster_img='images/{}/cloyster.PNG'.format(RESOLUTION)
golduck_img='images/{}/golduck.PNG'.format(RESOLUTION)
normal_golduck_img='images/{}/normal_golduck.PNG'.format(RESOLUTION)
psyduck_img='images/{}/psyduck.PNG'.format(RESOLUTION)

def set_fishing_rod():
    area = FISHING_POSITIONS
    area_center = pyautogui.center(area+IMG_BUBBLE_SIZE)
    sleep(1)
    pyautogui.moveTo(area_center)
    sleep(0.2)
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

def ball_tentacool():
    sleep(1)
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
            break

def ball_krabby():
    sleep(1)
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
            break

def ball_pokemon(image):
    sleep(1)
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    pokemon = True
    while pokemon != None:
        pokemon = pyautogui.locateOnScreen(image, confidence=0.8)
        if pokemon != None:
            pokemon_center = pyautogui.center(pokemon)
            pyautogui.moveTo(pokemon_center)
            sleep(0.2)
            my_keyboard.press('F12')
            sleep(0.2)
            mouseDown(pokemon.left, pokemon.top)
            mouseUp()
            break

def ball_shiny():
    sleep(2)
    ball_tentacool()
    ball_krabby()
    #ball_pokemon(octillery_img)
    #ball_pokemon(cloyster_img)
    #ball_pokemon(normal_golduck_img)
    #ball_pokemon(golduck_img)
    #  ball_pokemon(psyduck_img)

def check_hook():
    #sleep(2)
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    hook = True
    while hook != None:
        hook = pyautogui.locateOnScreen(hook_img, confidence=0.5)#, region=HOOK_REGION)
        if hook == None:
            print(current_time,': Fixing fishing position...')
            sleep(0.5)
            set_fishing_rod()
        break

def some_actions():
    sleep(10)
    check_hook()
    sleep(0.5)
    feed_pokemon()
    my_keyboard.press('esc')
    my_keyboard.press('tab')

def feed_pokemon():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    while True:
        hungry = pyautogui.locateOnScreen(hungry_img, confidence=0.9, region=(982,236,17,20))
        if hungry != None:
            print(current_time,': Feeding pokémon...')
            my_keyboard.press('caps')
            break
        else:
            break

keyboard.wait('p')

print(current_time, ": Started fishing")

threadBallShiny = threading.Thread(target=ball_shiny)
threadBallShiny.start()

threadSomeActions = threading.Thread(target=some_actions)
threadSomeActions.start()

while True:
    print(". . .")
    fishing_position = set_fishing_rod()
    if not threadBallShiny.is_alive():
        threadBallShiny = threading.Thread(target=ball_shiny)
        threadBallShiny.start()
    if not threadSomeActions.is_alive():
        threadSomeActions = threading.Thread(target=some_actions)
        threadSomeActions.start()

    threadSomeActions.join()
    threadBallShiny.join()
    
    wait_bubble(fishing_position)
    minigame()