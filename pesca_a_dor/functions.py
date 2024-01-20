import sys
sys.path.append('C:\\Users\\PC\\Desktop\\pesca-a-dor-main')

from pyautogui import *
import pyautogui
from time import sleep
import time
import datetime
import utils.my_keyboard as my_keyboard
import threading
import config

pyautogui.PAUSE = 0.01                               # Default = 0.1

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

def kill_shiny(pokemon_list, use_thread_kill_shiny=config.USE_THREAD_KILL_SHINY):
    if use_thread_kill_shiny:
        for pokemon_info in pokemon_list:
            pokemon_name, img_path, confidence = pokemon_info
            sleep(0.5)
            shiny = True
            while shiny != None:
                shiny = pyautogui.locateOnScreen(img_path, confidence=confidence)
                if shiny != None:
                    current_time = time.strftime("%H:%M:%S", time.localtime())
                    texto = "{}: Wild {} appeared!\n".format(current_time, pokemon_name)
                    print(current_time, f": Wild {pokemon_name} appeared!")
                    with open(log, "a") as log_out:
                        log_out.write(texto)
                    sleep(0.1)
                    my_keyboard.press('backspace')  # Use medicine on pokémon
                    sleep(0.1)
                    my_keyboard.press('F7')         # Mamaragan
                    sleep(0.1)
                    my_keyboard.press('F6')         # Discharge
                    sleep(0.1)
                    my_keyboard.press('F4')         # Thunder Wrath
                    sleep(0.1)
                    my_keyboard.press('F5')         # Electrify
                    sleep(1)
                    revive()
                    sleep(0.5)
                    ball_shiny("Shiny Krabby", config.krabby_img, 'F10', 0.7)
                    ball_shiny("Shiny Tentacool", config.tentacool_img, 'F11', 0.85)
                    ball_shiny("Shiny Giant Magikarp", config.shiny_giant_karp_img, 'F10', 0.8, offset_x=25, offset_y=25)

def ball_shiny(pokemon_name, img_path, key, confidence, offset_x=0, offset_y=0):
    sleep(0.5)
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    
    pokemon_found = True
    while pokemon_found != None:
        pokemon_found = pyautogui.locateOnScreen(img_path, confidence=confidence)
        if pokemon_found != None:
            pokemon_center = pyautogui.center(pokemon_found)
            pyautogui.moveTo(pokemon_center[0] + offset_x, pokemon_center[1] + offset_y)
            sleep(1)
            my_keyboard.press(key)
            texto = "{}: {} defeated!\n".format(current_time, pokemon_name)
            print(current_time, f": {pokemon_name} defeated!")
            sleep(1)
            mouseDown(pokemon_center[0] + offset_x, pokemon_center[1] + offset_y)
            mouseUp()
            with open(log, "a") as log_out:
                log_out.write(texto)
            break

def some_actions(use_thread_kill_shiny=config.USE_THREAD_KILL_SHINY):
    if use_thread_kill_shiny:
        threadKillShiny.join()
    check_hook()
    sleep(0.5)

    ball_shiny("Shiny Dratini", config.dratini_img, 'F12', 0.7)
    ball_shiny("Shiny Dragonair", config.dragonair_img, 'F12', 0.7)

    feed_pokemon()
    my_keyboard.press('esc')
    my_keyboard.press('tab')

def check_hook(use_thread_kill_shiny=config.USE_THREAD_KILL_SHINY):
    if use_thread_kill_shiny:
        threadKillShiny.join()
    sleep(2)
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
    sleep(0.2)

threadKillShiny = threading.Thread(target=kill_shiny)
threadSomeActions = threading.Thread(target=some_actions)