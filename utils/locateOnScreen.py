import sys
sys.path.append('C:\\Users\\PC\\Desktop\\pesca-a-dor-main')

from pyautogui import *
import pyautogui
import pesca_a_dor.config as config

pyautogui.PAUSE = 0.01 # pyautogui delay default = 0.1

# Function to locate the (left, top) position of each image
while True:
    bubble = pyautogui.locateOnScreen(config.bubble_img, confidence=0.7)
    hook = pyautogui.locateOnScreen(config.hook_img, confidence=0.5)
    bar = pyautogui.locateOnScreen(config.bar_img, confidence=0.7)
    fish = pyautogui.locateOnScreen(config.fish_img, confidence=0.7, grayscale=True)
    hungry = pyautogui.locateOnScreen(config.hungry_img, confidence=0.91, region=(982,236,17,20))
    krabby = pyautogui.locateOnScreen(config.krabby_img, confidence=0.7)
    tentacool = pyautogui.locateOnScreen(config.tentacool_img, confidence=0.88)
    feebas = pyautogui.locateOnScreen(config.feebas_img, confidence=0.8)
    giant_karp = pyautogui.locateOnScreen(config.giant_karp_img, confidence=0.90)
    shiny_giant_karp = pyautogui.locateOnScreen(config.shiny_giant_karp_img, confidence=0.88)
    magikarp = pyautogui.locateOnScreen(config.magikarp_img, confidence=0.88)
    shiny_dratini = pyautogui.locateOnScreen(config.dratini_img, confidence=0.69)
    shiny_dragonair = pyautogui.locateOnScreen(config.dragonair_img, confidence=0.69)
    elixir = pyautogui.locateOnScreen(config.elixir_img, confidence=0.9, region=(1382, 879, 36,21))
    combat = pyautogui.locateOnScreen(config.combat_img, confidence=0.9, region=(960, 850, 110, 70))
    electabuzz = pyautogui.locateOnScreen(config.electabuzz_img, confidence=0.95, region=(1717, 228, 34, 34))
    shedinja = pyautogui.locateOnScreen(config.shedinja_img, confidence=0.9, region=(1717, 228, 34, 34))

    print(pyautogui.position())             # Mouse position
    print("bubble",bubble)                  # Bubble and hook positions
    print("hook",hook)
    #print("bar",bar)                       # Minigame features positions
    #print("fish",fish)
    #print("hungry",hungry)                 # Hungry position (the icon must be RED if the pokemon is hungry)
    #print("shiny krabby",krabby)           # Dead pokemon positions
    #print("shiny tentacool",tentacool)
    print("shiny giant magikarp", shiny_giant_karp)
    print("shiny magikarp", magikarp)
    #print("shiny dratini",shiny_dratini)
    #print("shiny dragonair",shiny_dragonair)
    #print("normal dratini",normal_dratini)
    #print("normal dragonair",normal_dragonair)
    #print("elixir",elixir)
    #print("combat",combat)
    print("electabuzz",electabuzz)
    #print("shedinja",shedinja)
