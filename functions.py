from pyautogui import *
import pyautogui
from time import sleep
import time
import datetime
import my_keyboard
import keyboard
import threading
import config

#pyautogui.PAUSE = 0.01 #default = 0.1

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

today_var = datetime.date.today()
today_text = today_var.strftime("%d%m%Y")
log="logs/{}.txt".format(today_text)

def set_fishing_rod():
    area = config.FISHING_POSITIONS
    area_center = pyautogui.center(area+config.IMG_BUBBLE_SIZE)
    pyautogui.moveTo(area_center)
    sleep(1)
    my_keyboard.press('NUNLOCK')
    return area

def wait_bubble(fishing_position):
    while True:
        bubble = pyautogui.locateOnScreen(config.bubble_img, confidence=0.7, region=fishing_position+config.IMG_BUBBLE_SIZE)
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
        bar = pyautogui.locateOnScreen(config.bar_img, confidence=0.7, region=config.MINIGAME_REGION)
        fish = pyautogui.locateOnScreen(config.fish_img, confidence=0.7, grayscale=True, region=config.MINIGAME_REGION)
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
        shiny = pyautogui.locateOnScreen(config.shiny_img, confidence=0.9)
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
        tentacool = pyautogui.locateOnScreen(config.tentacool_img, confidence=0.85)
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
        krabby = pyautogui.locateOnScreen(config.krabby_img, confidence=0.7)
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

def ball_dratini():
    sleep(1)
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    dratini = True
    while dratini != None:
        dratini = pyautogui.locateOnScreen(config.dratini_img, confidence=0.7)
        if dratini != None:
            dratini_center = pyautogui.center(dratini)
            pyautogui.moveTo(dratini_center)
            sleep(1)
            my_keyboard.press('F12')
            texto = "{}: Shiny Dratini defeated!\n".format(current_time)
            print(current_time,': Shiny Dratini defeated!')
            sleep(1)
            mouseDown(dratini.left, dratini.top)
            mouseUp()
            with open(log, "a") as log_out:
                log_out.write(texto)
            break
    
def ball_dragonair():
    sleep(1)
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    dragonair = True
    while dragonair != None:
        dragonair = pyautogui.locateOnScreen(config.dragonair_img, confidence=0.7)
        if dragonair != None:
            dragonair_center = pyautogui.center(dragonair)
            pyautogui.moveTo(dragonair_center)
            sleep(1)
            my_keyboard.press('F12')
            texto = "{}: Shiny Dragonair defeated!\n".format(current_time)
            print(current_time,': Shiny Dragonair defeated!')
            sleep(1)
            mouseDown(dragonair.left, dragonair.top)
            mouseUp()
            with open(log, "a") as log_out:
                log_out.write(texto)
            break

def some_actions():
    #threadKillShiny.join()
    ball_dratini()  
    ball_dragonair()
    check_hook()
    sleep(0.5)
    feed_pokemon()
    my_keyboard.press('esc')
    my_keyboard.press('tab')

def check_hook():
    #threadKillShiny.join()
    sleep(6)
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    hook = True
    while hook != None: 
        hook = pyautogui.locateOnScreen(config.hook_img, confidence=0.5, region=config.FISHING_POSITIONS+config.IMG_HOOK_SIZE)
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
        hungry = pyautogui.locateOnScreen(config.hungry_img, confidence=0.91, region=config.HUNGRY_POSITION)
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
    pyautogui.moveTo(config.POKEBALL_POSITION, duration=0.3)
    pyautogui.click(button="right")
    my_keyboard.press('F1')
    pyautogui.click()
    pyautogui.click()
    pyautogui.click(button="right")
    sleep(0.1)
    pyautogui.moveTo(config.POKE_POSITION, duration=0.3)
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