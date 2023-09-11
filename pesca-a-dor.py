from pyautogui import *
import pyautogui
from time import sleep
import time
import datetime
import my_keyboard
import keyboard
import threading

#pyautogui.PAUSE = 0.01 #default = 0.1

RESOLUTION='1024x768'

#FISHING_POSITIONS = (280, 382) #hamlin bueiro
FISHING_POSITIONS = (319, 110) #hamlin Guru (fish on map)
MINIGAME_REGION = (160,150,100,400)
HUNGRY_POSITION = (982,236,17,20)
IMG_BUBBLE_SIZE = (25,28)
POKEBALL_POSITION = (838, 237)
POKE_POSITION = (410, 242)

#IMG PATH
bubble_img='images/{}/bubble.PNG'.format(RESOLUTION)
bar_img='images/{}/bar.PNG'.format(RESOLUTION)
fish_img='images/{}/fish_bin.PNG'.format(RESOLUTION)
shiny_img='images/{}/shiny.PNG'.format(RESOLUTION)
krabby_img='images/{}/krabby.PNG'.format(RESOLUTION)
tentacool_img='images/{}/tentacool.PNG'.format(RESOLUTION)
hungry_img='images/{}/hungry.PNG'.format(RESOLUTION)
hook_img='images/{}/hook.PNG'.format(RESOLUTION)

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
        bar = pyautogui.locateOnScreen(bar_img, confidence=0.7, region=MINIGAME_REGION)
        fish = pyautogui.locateOnScreen(fish_img, confidence=0.7, grayscale=True, region=MINIGAME_REGION)
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
    sleep(0.5)
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
            my_keyboard.press('F7') # Mamaragan
            sleep(0.1)
            my_keyboard.press('F6') # Discharge
            sleep(0.1)
            my_keyboard.press('F4') # Thunder Wrath
            sleep(0.1)
            my_keyboard.press('F5') # Electrify
            sleep(1)
            revive()
            sleep(0.2)
            ball_tentacool()
            sleep(0.1)
            ball_krabby()

def ball_tentacool():
    sleep(1)
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    tentacool = True
    while tentacool != None:
        tentacool = pyautogui.locateOnScreen(tentacool_img, confidence=0.88)
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
            texto = "{}: Shiny Krabby defeated!\n".format(current_time)
            print(current_time,': Shiny Krabby defeated!')
            sleep(1)
            mouseDown(krabby.left, krabby.top)
            mouseUp()
            with open(log, "a") as log_out:
                log_out.write(texto)
            break

def some_actions():
    threadKillShiny.join()
    check_hook()
    sleep(0.5)
    feed_pokemon()
    my_keyboard.press('esc')
    my_keyboard.press('tab')

def check_hook():
    threadKillShiny.join()
    sleep(6)
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    hook = True
    while hook != None:
        hook = pyautogui.locateOnScreen(hook_img, confidence=0.5)
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
        hungry = pyautogui.locateOnScreen(hungry_img, confidence=0.91, region=HUNGRY_POSITION)
        if hungry != None:
            texto = "{}: Feeding pokémon...\n".format(current_time)
            print(current_time,': Feeding pokémon...')
            my_keyboard.press('caps')
            with open(log, "a") as log_out:
                log_out.write(texto)
            break
        else:
            break

def revive():
    current_position = pyautogui.position()
    pyautogui.moveTo(POKEBALL_POSITION, duration=0.3)
    pyautogui.click(button="right")
    my_keyboard.press('F1')
    pyautogui.click()
    pyautogui.click()
    pyautogui.click(button="right")
    sleep(0.1)
    pyautogui.moveTo(POKE_POSITION, duration=0.3)
    my_keyboard.press('F2')
    sleep(0.2)
    my_keyboard.press('F2')
    sleep(0.2)
    my_keyboard.press('F2')
    sleep(0.2)
    my_keyboard.press('F2')
    sleep(0.2)
    my_keyboard.press('tab')
    pyautogui.moveTo(current_position, duration=0.3)

threadKillShiny = threading.Thread(target=kill_shiny)
#threadKillShiny.start()

threadSomeActions = threading.Thread(target=some_actions)
#threadSomeActions.start()

######## START ########

texto = "{}: Started fishing\n".format(current_time)
with open(log, "a") as log_output:
    log_output.write(texto)

print(current_time, ": Started fishing")

keyboard.wait('p')

#Set the number of minigame_repeats
#A minigame appears for every 4 minutes on average
minigame_repeats = 120   
counter = 0

while counter < minigame_repeats:
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    with open(log, "a") as log_output:
        texto_repetido = "{}: ...\n".format(current_time)
        log_output.write(texto_repetido)

    print(current_time,": ...")

    fishing_position = set_fishing_rod()

    if not threadKillShiny.is_alive():
        threadKillShiny = threading.Thread(target=kill_shiny)
        threadKillShiny.start()
    
    #Wait until the thread terminates  
    threadKillShiny.join()

    if not threadSomeActions.is_alive():
        threadSomeActions = threading.Thread(target=some_actions)
        threadSomeActions.start()

    #Wait until the thread terminates    
    threadSomeActions.join()
    
    sleep(0.5)
    wait_bubble(fishing_position)
    texto_minigame = minigame()
    texto_log_minigame = "{}: {}\n".format(current_time, texto_minigame)

    with open(log, "a") as log_output:
        if texto_minigame != None:
            sleep(1)
            log_output.write(str(texto_log_minigame))
            counter += 1

    #Logout after the end of minigame_repeats
    if minigame_repeats == counter:
        sleep(20)
        keyboard.press_and_release("ctrl+q")
        sleep(1)
        keyboard.press_and_release("enter")

######## END ########
