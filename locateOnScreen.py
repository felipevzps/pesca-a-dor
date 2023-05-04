from pyautogui import *
import pyautogui
import win32gui
from time import sleep

#IMG PATH
RESOLUTION='1024x768'

bubble_img='images/{}/bubble.PNG'.format(RESOLUTION)
bar_img='bar_1024x768.PNG'
fish_img='fish_1024x768_binarizada.PNG'
hungry_img='images/{}/hungry.PNG'.format(RESOLUTION)
krabby_img='krabby_1024x768.PNG'
tentacool_img='images/{}/tentacool1.PNG'.format(RESOLUTION)
hook_img='hook_1024x768.PNG'


#POSITIONS
FISHING_POSITIONS = (514, 382) #viridian
IMG_BUBBLE_SIZE = (25,28)
MINIGAME_REGION_BAR = (189,555,15,38)
MINIGAME_REGION_FISH = (236,178,14,14)

#pyautogui.PAUSE = 0.1 # default
pyautogui.PAUSE = 0.01 

#pxg = win32gui.FindWindow(None, "PokeXGames")
#x, y, largura, altura = win32gui.GetWindowRect(pxg)

# Ajustar as coordenadas para a posição da janela na tela
#x, y = pyautogui.position()[0] - x, pyautogui.position()[1] - y

#PXG Client
#<Win32Window left="-8", top="-8", width="1040", height="744", title="PokeXGames">
#print()

while True:
    bubble = pyautogui.locateOnScreen(bubble_img, confidence=0.7)#, region=FISHING_POSITIONS+IMG_BUBBLE_SIZE)
    #bubble = pyautogui.locateOnScreen(bubble_img, confidence=0.7, region=(x, y, largura, altura))   
    #bar = pyautogui.locateOnScreen(bar_img, confidence=0.7)
    #hook = pyautogui.locateOnScreen(hook_img, confidence=0.5)

    #fish = pyautogui.locateOnScreen(fish_img, confidence=0.7, grayscale=True)
    hungry = pyautogui.locateOnScreen(hungry_img, confidence=0.91, region=(982,236,17,20))
    #krabby = pyautogui.locateOnScreen(krabby_img, confidence=0.7)
    tentacool = pyautogui.locateOnScreen(tentacool_img, confidence=0.91)
    print("bubble",bubble)
    #print("bar",bar)
    #print("fish",fish)
    #print("hook",hook)
    print("hungry",hungry)
    #print("krabby",krabby)
    print("tentacool",tentacool)