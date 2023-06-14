from pyautogui import *
import pyautogui
from time import sleep
import time
import datetime
import my_keyboard
import keyboard
import threading

#req
#pip install pyautogui
#pip install keyboard
#pip install Pillow
#pip install opencv-python

pyautogui.PAUSE = 0.01 #default = 0.1

RESOLUTION='1024x768'
#FISHING_POSITIONS = (319, 383) #hamlin esgoto
#FISHING_POSITIONS = (397, 343) #cerulean perto cp
FISHING_POSITIONS = (397, 305) #pewter caminho cerulean
IMG_BUBBLE_SIZE = (25,28)
MINIGAME_REGION_BAR = (190,478,15,42)
MINIGAME_REGION_FISH = (189,241,57,57)
HOOK_REGION = (401,389,21,21)
POKEBALL_POSITION = (838, 237)
POKE_POSITION = (408, 243)
EMBAIXO_POKE_POSITION = (410, 317)

#IMG PATH
bubble_img='images/{}/bubble.PNG'.format(RESOLUTION)
bar_img='images/{}/bar.PNG'.format(RESOLUTION)
fish_img='images/{}/fish_bin.PNG'.format(RESOLUTION)
shiny_img='images/{}/shiny.PNG'.format(RESOLUTION)
krabby_img='images/{}/krabby.PNG'.format(RESOLUTION)
tentacool_img='images/{}/tentacool.PNG'.format(RESOLUTION)
hungry_img='images/{}/hungry.PNG'.format(RESOLUTION)
hook_img='images/{}/hook2.PNG'.format(RESOLUTION)
giant_karp_img='images/{}/giant_karp.PNG'.format(RESOLUTION)
shiny_giant_karp_img='images/{}/shiny_giant_karp.PNG'.format(RESOLUTION)
shiny_karp_img='images/{}/shiny_karp.PNG'.format(RESOLUTION)
feebas_img='images/{}/feebas.PNG'.format(RESOLUTION)

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

today_var = datetime.date.today()
today_text = today_var.strftime("%d%m%Y")
log="logs/{}.txt".format(today_text)

def set_fishing_rod():
    area = FISHING_POSITIONS
    area_center = pyautogui.center(area+IMG_BUBBLE_SIZE)
    pyautogui.moveTo(area_center, duration=0.1)
    #sleep(1.5)
    my_keyboard.press('NUNLOCK')
    return area

def wait_bubble(fishing_position):
    sleep(2)
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

def revive():
    current_position = pyautogui.position()
    pyautogui.moveTo(POKEBALL_POSITION, duration=0.1)
    pyautogui.click(button="right")
    my_keyboard.press('F1')
    pyautogui.click()
    pyautogui.click()
    pyautogui.click(button="right")
    sleep(0.1)
    pyautogui.moveTo(POKE_POSITION, duration=0.1)
    my_keyboard.press('F2')
    sleep(0.2)
    my_keyboard.press('F2')
    sleep(0.2)
    my_keyboard.press('F2')
    sleep(0.2)
    my_keyboard.press('F2')
    sleep(0.2)
    my_keyboard.press('esc')
    pyautogui.moveTo(current_position, duration=0.1)

def kill_shiny():
    sleep(0.5)#2 pra tentacool
    shiny = True
    while shiny != None:
        shiny = pyautogui.locateOnScreen(shiny_img, confidence=0.9)
        if shiny != None:
            #texto = "{}: Wild Shiny Giant Magikarp appeared!\n".format(current_time)
            print(current_time,': Wild Shiny Giant Magikarp appeared!')
            #with open(log, "a") as log_out:
                #log_out.write(texto)
            sleep(0.1)
            my_keyboard.press('F7') # Mamaragan
            sleep(0.1)
            my_keyboard.press('F6') # Discharge
            sleep(0.1)
            my_keyboard.press('F4') # Thunder Wrath
            sleep(0.1)
            my_keyboard.press('F5') # Electrify
            sleep(0.5)
            revive()
            ball_giant_magikarp()
            
def kill_giant_karp():
    sleep(0.5)
    giant_karp = True
    while giant_karp != None:
        giant_karp = pyautogui.locateOnScreen(giant_karp_img, confidence=0.9)
        if giant_karp != None:
            print(current_time,': Wild Giant Magikarp appeared!')
            sleep(0.1)
            my_keyboard.press('F7') # Swords Dance
            sleep(0.1)
            my_keyboard.press('F6') # Air Slash
            sleep(0.1)
            my_keyboard.press('F4') # X-Scissor
            sleep(0.1)
            my_keyboard.press('F5') # Wing Attack
            sleep(0.1)
            revive()

def kill_feebas():
    sleep(0.5)
    feebas = True
    while feebas != None:
        feebas = pyautogui.locateOnScreen(feebas_img, confidence=0.8)
        if feebas != None:
            print(current_time,': Wild feebas appeared!')
            sleep(0.1)
            my_keyboard.press('F7') # Swords Dance
            sleep(0.1)
            my_keyboard.press('F6') # Air Slash
            sleep(0.1)
            my_keyboard.press('F4') # X-Scissor
            sleep(0.1)
            my_keyboard.press('F5') # Wing Attack
            sleep(0.1)
            revive()

def ball_giant_magikarp():
    sleep(1)
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    shiny_giant_karp = True
    while shiny_giant_karp != None:
        shiny_giant_karp = pyautogui.locateOnScreen(shiny_giant_karp_img, confidence=0.95)
        if shiny_giant_karp != None:
            #texto = "{}: Shiny Giant Magikarp defeated!\n".format(current_time)
            print(current_time,': Shiny Giant Magikarp defeated!')
            pyautogui.moveTo(shiny_giant_karp.left + 25, shiny_giant_karp.top + 25, duration=0.1)
            #sleep(0.7)
            pyautogui.click(button="right")
            sleep(1)
            my_keyboard.press('down')
            sleep(0.7)
            pyautogui.moveTo(shiny_giant_karp.left + 25, shiny_giant_karp.top + 25, duration=0.1)
            #sleep(0.2)
            my_keyboard.press('F12')
            sleep(0.2)
            mouseDown(shiny_giant_karp.left + 25, shiny_giant_karp.top + 25)
            mouseUp()
            #with open(log, "a") as log_out:
                #log_out.write(texto)
            break

def ball_magikarp():
    sleep(1)
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    shiny_karp = True
    while shiny_karp != None:
        shiny_karp = pyautogui.locateOnScreen(shiny_karp_img, confidence=0.93)
        if shiny_karp != None:
            #texto = "{}: Shiny Magikarp defeated!\n".format(current_time)
            print(current_time,': Shiny Magikarp defeated!')
            magikarp_center = pyautogui.center(shiny_karp)
            pyautogui.moveTo(magikarp_center, duration=0.1)
            #sleep(0.7)
            pyautogui.click(button="right")
            sleep(1)
            my_keyboard.press('down')
            sleep(0.8)
            pyautogui.moveTo(magikarp_center, duration=0.1)
            #sleep(0.4)
            my_keyboard.press('F12')
            sleep(1)
            mouseDown(shiny_karp.left, shiny_karp.top)
            mouseUp()
            #with open(log, "a") as log_out:
                #log_out.write(texto)
            break

def kill_pokes():
    kill_shiny()
    kill_giant_karp()
    kill_feebas()

def some_actions():
    threadKillShiny.join()
    check_hook()
    sleep(0.5)
    feed_pokemon()
    my_keyboard.press('esc')
    my_keyboard.press('tab')

def check_hook():
    sleep(2)
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    hook = True
    while hook != None:
        hook = pyautogui.locateOnScreen(hook_img, confidence=0.5)#, region=HOOK_REGION)
        if hook == None:
            #texto = "{}: Fixing fishing position...\n".format(current_time)
            print(current_time,': Fixing fishing position...')
            sleep(0.5)
            set_fishing_rod()
            #with open(log, "a") as log_out:
            #    log_out.write(texto)
        break

def feed_pokemon():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    while True:
        hungry = pyautogui.locateOnScreen(hungry_img, confidence=0.91, region=(982,236,17,20))
        if hungry != None:
            #texto = "{}: Feeding pokémon...\n".format(current_time)
            print(current_time,': Feeding pokémon...')
            my_keyboard.press('caps')
            #with open(log, "a") as log_out:
            #    log_out.write(texto)
            break
        else:
            break

threadKillShiny = threading.Thread(target=kill_pokes)
threadSomeActions = threading.Thread(target=some_actions)
#threadSomeActions.start()

#texto = "{}: Started fishing\n".format(current_time)
#with open(log, "a") as log_output:
#    log_output.write(texto)

print(current_time, ": Started fishing")

keyboard.wait('p')

#def login_account():
#def soltar_pokemon():
#def usar elixir():
#def pescar():
    #começa contar 5 minutos
#def deslogar():

while True:
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    #with open(log, "a") as log_output:
    #    texto_repetido = "{}: ...\n".format(current_time)
    #    log_output.write(texto_repetido)

    print(current_time,": ...")

    fishing_position = set_fishing_rod()

    if not threadKillShiny.is_alive():
        threadKillShiny = threading.Thread(target=kill_pokes)
        threadKillShiny.start()
    threadKillShiny.join()

    if not threadSomeActions.is_alive():
        threadSomeActions = threading.Thread(target=some_actions)
        threadSomeActions.start()
    #Wait until the thread terminates    
    threadSomeActions.join()

    wait_bubble(fishing_position)
    minigame()
