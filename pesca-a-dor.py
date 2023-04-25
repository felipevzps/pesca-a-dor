from pyautogui import *
import pyautogui
import random
from time import sleep
import time
import my_keyboard
import keyboard

#req
#pip install pyautogui
#pip install keyboard
#pip install Pillow
#pip install opencv-python

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

#pyautogui.PAUSE = 0.1 # default
pyautogui.PAUSE = 0.01 # tentando rodar mais rapdo

#IMG PATH
#bubble_img='bubble_1024x768_portosolo.PNG'
bubble_img='bubble_1024x768_vermilion.PNG'
bar_img='bar_1024x768.PNG'
fish_img='fish_1024x768.PNG'
shiny_img='shiny_1024x768.PNG'
krabby_img='krabby_1024x768.PNG'
tentacool_img='tentacool_1024x768.PNG'
hungry_img='hungry_1024x768.PNG'
#hook_img='hook_1024x768.PNG'

#POSITIONS
#FISHING_POSITIONS = [(543, 295),(543, 295)] #Mankey
#FISHING_POSITIONS = [(270, 218),(270, 218)] #porto
#FISHING_POSITIONS = [(386, 374),(386, 374)] #portosolo
#IMG_BUBBLE_SIZE = (44,48) #Mankey
#FISHING_POSITIONS = [(388, 100),(388, 100)] #Aero
#IMG_BUBBLE_SIZE = (42,47) #Aero
###FISHING_POSITIONS = [(347, 451),(347, 451)] #GYM PLANTA
###IMG_BUBBLE_SIZE = (44,47) #GYN PLANTA
FISHING_POSITIONS = [(397, 342),(397, 342)] #porto
IMG_BUBBLE_SIZE = (44,47) #Mankey

MINIGAME_REGION_BAR = (190,478,15,42)
MINIGAME_REGION_FISH = (189,241,13,21)
#HOOK_REGION = (557,312,21,21)

def set_fishing_rod():
    area = random.choice(FISHING_POSITIONS)
    area_center = pyautogui.center(area+IMG_BUBBLE_SIZE)
    pyautogui.moveTo(area_center)
    sleep(0.5)
    my_keyboard.press('NUNLOCK')
    return area

def wait_bubble(fishing_position):
    while True:
        bubble = pyautogui.locateOnScreen(bubble_img, confidence=0.7, region=fishing_position+IMG_BUBBLE_SIZE)
        #hook = pyautogui.locateOnScreen(hook_img, confidence=0.7, region=HOOK_REGION)
        if bubble != None:
            my_keyboard.press('NUNLOCK')
            break

def minigame():
    sleep(0.5)
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

def kill_shiny():
    sleep(1)
    shiny = True
    while shiny != None:
        shiny = pyautogui.locateOnScreen(shiny_img, confidence=0.9)
        if shiny != None:
            my_keyboard.press('backspace') # Use medicine on pokémon
            sleep(0.5)
            #my_keyboard.press('F7') # Mamaragan
            my_keyboard.press('F9') # Swords Dance
            sleep(0.5)
            my_keyboard.press('F6') # Discharge / Air Slash
            sleep(0.5)
            my_keyboard.press('F2') 
            sleep(0.5)
            #my_keyboard.press('F5')
            #sleep(6)
            ball_tentacool()
            ball_krabby()
            break
        else:
            break

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
            sleep(1)
            my_keyboard.press('F11')
            print(current_time,': Shiny Tentacool defeated!')
            sleep(0.5)
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
            sleep(1)
            my_keyboard.press('F12')
            print(current_time,': Shiny Krabby defeated!')
            sleep(0.5)
            mouseDown(krabby.left, krabby.top)
            mouseUp()
            break

def feed_pokemon():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    while True:
        hungry = pyautogui.locateOnScreen(hungry_img, confidence=0.9, region=(982,99,17,20))
        if hungry != None:
            print(current_time,': Feeding pokémon...')
            my_keyboard.press('caps')
            sleep(2)
            break
        else:
            break

keyboard.wait('p')
sleep(1)
    
print(current_time, ": Started fishing")

while True:
    print(". . .")
    fishing_position = set_fishing_rod()
    wait_bubble(fishing_position)
    minigame()
    kill_shiny()
    feed_pokemon()
    sleep(3)
    my_keyboard.press('ESC')
    my_keyboard.press('tab')
