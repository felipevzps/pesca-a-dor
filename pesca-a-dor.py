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
FISHING_POSITIONS = (553, 148)
IMG_BUBBLE_SIZE = (25,28)
MINIGAME_REGION_BAR = (190,478,15,42)
MINIGAME_REGION_FISH = (189,241,57,57)
HOOK_REGION = (553,148,21,21)

#IMG PATH
bubble_img=f'images/{}/bubble.PNG'.format(RESOLUTION)
bar_img=f'images/{}/bar.PNG'.format(RESOLUTION)
fish_img=f'images/{}/fish_bin.PNG'.format(RESOLUTION)
shiny_img=f'images/{}/shiny.PNG'.format(RESOLUTION)
krabby_img=f'images/{}/krabby.PNG'.format(RESOLUTION)
tentacool_img=f'images/{}/tentacool.PNG'.format(RESOLUTION)
hungry_img=f'images/{}/hungry.PNG'.format(RESOLUTION)
hook_img=f'images/{}/hook.PNG'.format(RESOLUTION)

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

today_var = datetime.date.today()
today_text = today_var.strftime("%d%m%Y")
log="logs/{}.txt".format(today_text)

def set_fishing_rod():
    area = FISHING_POSITIONS
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
    texto = None
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    while fish != None:
        bar = pyautogui.locateOnScreen(bar_img, confidence=0.7)
        fish = pyautogui.locateOnScreen(fish_img, confidence=0.7, grayscale=True)
        if bar != None and fish != None:
            texto = "Solving puzzle..."
            if bar.top > fish.top:
                my_keyboard.key_down(0x39)
            else:   
                my_keyboard.release_key(0x39)
        else:
            my_keyboard.key_down(0x39)  
            my_keyboard.release_key(0x39)
    if texto != None:
        print(current_time,":", texto)
    return texto

def kill_shiny():
    #sleep(0.2)
    shiny = True
    while shiny != None:
        shiny = pyautogui.locateOnScreen(shiny_img, confidence=0.9)
        if shiny != None:
            texto = "{}: Wild pokémon appeared!\n".format(current_time)
            print(current_time,': Wild pokémon appeared!')
            with open(log, "a") as log_out:
                log_out.write(texto)
            sleep(0.1)
            my_keyboard.press('backspace') # Use medicine on pokémon
            sleep(0.1)
            my_keyboard.press('F9') # Swords Dance
            sleep(0.1)
            my_keyboard.press('F6') # Air Slash
            sleep(0.1)
            my_keyboard.press('F2') # Air Cutter
            sleep(0.1)
            ball_tentacool()
            ball_krabby()
            break
        else:
            break

def ball_tentacool():
    sleep(1)
    #print('ball_tentacool activated')
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    tentacool = True
    while tentacool != None:
        tentacool = pyautogui.locateOnScreen(tentacool_img, confidence=0.85)
        if tentacool != None:
            tentacool_center = pyautogui.center(tentacool)
            pyautogui.moveTo(tentacool_center)
            sleep(1)
            my_keyboard.press('F11')
            texto = "{}: Shiny Tentacool defeated!\n".format(current_time)
            print(current_time,': Shiny Tentacool defeated!')
            sleep(0.5)
            mouseDown(tentacool.left, tentacool.top)
            mouseUp()
            with open(log, "a") as log_out:
                log_out.write(texto)
            #set_fishing_rod()
            break

def ball_krabby():
    sleep(1)
    #print('ball_krabby activated')
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
            texto = "{}: Shiny Krabby defeated!\n".format(current_time)
            print(current_time,': Shiny Krabby defeated!')
            sleep(1)
            mouseDown(krabby.left, krabby.top)
            mouseUp()
            with open(log, "a") as log_out:
                log_out.write(texto)
            #set_fishing_rod()
            break

def some_actions():
    check_hook()
    sleep(0.5)
    feed_pokemon()
    #my_keyboard.press('esc')
    my_keyboard.press('tab')

def check_hook():
    sleep(10)
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    hook = True
    while hook != None:
        hook = pyautogui.locateOnScreen(hook_img, confidence=0.5)#, region=HOOK_REGION)
        if hook == None:
            texto = "{}: Fixing fishing position...\n".format(current_time)
            print(current_time,': Fixing fishing position...')
            sleep(0.5)
            set_fishing_rod()
            with open(log, "a") as log_out:
                log_out.write(texto)
        break

def feed_pokemon():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    while True:
        hungry = pyautogui.locateOnScreen(hungry_img, confidence=0.9, region=(982,99,17,20))
        if hungry != None:
            texto = "{}: Feeding pokémon...\n".format(current_time)
            print(current_time,': Feeding pokémon...')
            my_keyboard.press('caps')
            with open(log, "a") as log_out:
                log_out.write(texto)
            break
        else:
            break

threadKillShiny = threading.Thread(target=kill_shiny)
#threadKillShiny.start()

threadSomeActions = threading.Thread(target=some_actions)
#threadSomeActions.start()

texto = "{}: Started fishing\n".format(current_time)
with open(log, "a") as log_output:
    log_output.write(texto)

print(current_time, ": Started fishing")

keyboard.wait('p')

while True:
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    with open(log, "a") as log_output:
        texto_repetido = "{}: ...\n".format(current_time)
        log_output.write(texto_repetido)

    print(current_time,": ...")

    fishing_position = set_fishing_rod()

    if not threadSomeActions.is_alive():
        threadSomeActions = threading.Thread(target=some_actions)
        threadSomeActions.start()

    if not threadKillShiny.is_alive():
        threadKillShiny = threading.Thread(target=kill_shiny)
        threadKillShiny.start()

    #Wait until the thread terminates    
    threadSomeActions.join()
    threadKillShiny.join()

    wait_bubble(fishing_position)

    texto_minigame = minigame()
    texto_log_minigame = "{}: {}\n".format(current_time, texto_minigame)

    with open(log, "a") as log_output:
        if texto_minigame != None:
            sleep(1)
            log_output.write(str(texto_log_minigame))
