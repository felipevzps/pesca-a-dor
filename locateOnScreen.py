from pyautogui import *
import pyautogui
from time import sleep

RESOLUTION='1024x768'

# IMG PATH
bubble_img='images/{}/bubble.PNG'.format(RESOLUTION)
hook_img='images/{}/hook.PNG'.format(RESOLUTION)
bar_img='images/{}/bar.PNG'.format(RESOLUTION)
fish_img='images/{}/fish_bin.PNG'.format(RESOLUTION)
hungry_img='images/{}/hungry.PNG'.format(RESOLUTION)
shiny_img='images/{}/shiny.PNG'.format(RESOLUTION)
krabby_img='images/{}/krabby.PNG'.format(RESOLUTION)
tentacool_img='images/{}/tentacool.PNG'.format(RESOLUTION)
feebas_img='images/{}/feebas.PNG'.format(RESOLUTION)
giant_karp_img='images/{}/giant_karp.PNG'.format(RESOLUTION)
shiny_giant_karp_img='images/{}/shiny_giant_karp.PNG'.format(RESOLUTION)

#pyautogui.PAUSE = 0.01 # pyautogui delay default = 0.1

# Function to locate the (left, top) position of each image
while True:
    bubble = pyautogui.locateOnScreen(bubble_img, confidence=0.7)
    hook = pyautogui.locateOnScreen(hook_img, confidence=0.5)
    bar = pyautogui.locateOnScreen(bar_img, confidence=0.7)
    fish = pyautogui.locateOnScreen(fish_img, confidence=0.7, grayscale=True)
    hungry = pyautogui.locateOnScreen(hungry_img, confidence=0.91, region=(982,236,17,20))
    krabby = pyautogui.locateOnScreen(krabby_img, confidence=0.7)
    tentacool = pyautogui.locateOnScreen(tentacool_img, confidence=0.88)
    feebas = pyautogui.locateOnScreen(feebas_img, confidence=0.8)
    giant_karp = pyautogui.locateOnScreen(giant_karp_img, confidence=0.90)
    shiny_giant_karp = pyautogui.locateOnScreen(shiny_giant_karp_img, confidence=0.95)

    # Mouse position
    print(pyautogui.position())
    
    # Bubbles and hook positions
    print("bubble",bubble)
    print("hook",hook)

    # Minigame features positions
    print("bar",bar)
    print("fish",fish)

    # Hungry position (the icon must be RED if the pokemon is hungry)
    print("hungry",hungry)

    # Dead pokemon positions
    print("krabby",krabby)
    print("tentacool",tentacool)
    print("giant_karp",giant_karp)
