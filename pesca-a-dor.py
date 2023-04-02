import pyautogui
import random
from time import sleep
import my_keyboard
import keyboard

#pyautogui.PAUSE = 0.1 # default
pyautogui.PAUSE = 0.01 # tentando rodar mais rapdo

#IMG PATH
bubble_img='bubble_1024x768_vermilion.PNG'
bar_img='bar_1024x768.PNG'
fish_img='fish_1024x768.PNG'

#POSITIONS
FISHING_POSITIONS = [(505, 259),(505, 259)] #Vermilion
IMG_BUBBLE_SIZE = (42,42) #Vermilion
MINIGAME_REGION_BAR = (190,478,15,42)
MINIGAME_REGION_FISH = (189,241,13,21)

def set_fishing_rod():
    area = random.choice(FISHING_POSITIONS)
    area_center = pyautogui.center(area+IMG_BUBBLE_SIZE)
    pyautogui.moveTo(area_center)
    sleep(1)
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
    while fish != None:
        bar = pyautogui.locateOnScreen(bar_img, confidence=0.7)
        fish = pyautogui.locateOnScreen(fish_img, confidence=0.7, grayscale=True)
        if bar != None and fish != None:
            if bar.top > fish.top:
                my_keyboard.key_down(0x39)
            else:
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
