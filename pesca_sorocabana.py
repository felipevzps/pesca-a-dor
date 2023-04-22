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
bubble_img='bubble_1024x768_vermilion.PNG'
bar_img='bar_1024x768.PNG'
fish_img='fish_1024x768.PNG'
shiny_img='shiny_1024x768.PNG'
krabby_img='krabby_1024x768.PNG'
tentacool_img='tentacool_1024x768.PNG'
hungry_img='hungry_1024x768.PNG'

#POSITIONS
#FISHING_POSITIONS = [(543, 295),(543, 295)] #Mankey
FISHING_POSITIONS = [(635, 352),(635, 352)] #porto
IMG_BUBBLE_SIZE = (44,48) #porto
MINIGAME_REGION_BAR = (190,478,15,42)
MINIGAME_REGION_FISH = (189,241,13,21)
HOOK_REGION = (557,312,21,21)

def set_fishing_rod():
    area = random.choice(FISHING_POSITIONS)
    area_center = pyautogui.center(area+IMG_BUBBLE_SIZE)
    pyautogui.moveTo(area_center)
    sleep(1)
    my_keyboard.press('NUNLOCK')
    return area

def wait_bubble(fishing_position):
    while True:
        bubble = pyautogui.locateOnScreen(bubble_img, confidence=0.7)#, region=fishing_position+IMG_BUBBLE_SIZE)
        if bubble != None:
            my_keyboard.press('right')
            sleep(0.5)
            my_keyboard.press('NUNLOCK')
            sleep(0.5)
            my_keyboard.press('left')
            break


keyboard.wait('p')

print(current_time, ": Started fishing")

while True:
    print(". . .")
    fishing_position = set_fishing_rod()
    wait_bubble(fishing_position)
    sleep(2)
