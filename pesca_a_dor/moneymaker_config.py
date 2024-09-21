import sys
sys.path.append('C:\\Users\\PC\\Desktop\\pesca-a-dor-main')

from pyautogui import *
import pyautogui
from time import sleep
import time
import functions
import utils.my_keyboard as my_keyboard
import keyboard
import threading
import config

def login(email, password, user_image_path, char):
    sleep(3)
    pyautogui.click(1026, 365, duration=0.3)  # email
    pyautogui.write(email)      
    time.sleep(0.3)               

    pyautogui.click(1015, 472, duration=0.3)  # password
    pyautogui.write(password)   
    time.sleep(0.3)               

    pyautogui.click(1090, 604, duration=0.3)  # login
    time.sleep(5)               

    char_image_location = pyautogui.locateOnScreen(user_image_path, confidence=0.65)

    if char_image_location:
        pyautogui.moveTo(char_image_location)
        time.sleep(1)
        pyautogui.doubleClick(char_image_location)
        functions.log_message(f"Logging with {char}...")
    else:
        functions.log_message(f"{char} not found. Exiting.")
    
    time.sleep(5)

def logout():
    combat = pyautogui.locateOnScreen(config.combat_img, confidence=0.9, region=(960, 850, 110, 70))
    while combat != None:
        combat = pyautogui.locateOnScreen(config.combat_img, confidence=0.9, region=(960, 850, 110, 70))
    sleep(1)
    functions.log_message("Session complete. Logging out now.")
    sleep(1)
    keyboard.press_and_release("ctrl+q")
    sleep(1)
    keyboard.press_and_release("enter")
    sleep(1)
    keyboard.press_and_release("esc")
    sleep(1)
    pyautogui.moveTo(1426, 565)
    sleep(0.2)
    pyautogui.click(button="left")

def set_fishing_rod(account):
    functions.log_message("...")
    
    area = account["FISHING_POSITION"]
    area_center = pyautogui.center((area[0], area[1], config.IMG_BUBBLE_SIZE[0], config.IMG_BUBBLE_SIZE[1]))
    pyautogui.moveTo(area_center)
    sleep(1)
    pyautogui.click(button="left")
    my_keyboard.press('NUNLOCK')
    return area

def release_pokemon(message):
    functions.log_message(message)
    pyautogui.moveTo(config.POKEBALL_POSITION, duration=0.5)
    sleep(0.5)
    pyautogui.click(button="right")
    sleep(1)

def check_hook(use_thread_kill_shiny, account):
    if use_thread_kill_shiny and functions.threadKillShiny.is_alive():
        functions.threadKillShiny.join()
    sleep(1)
    hook = True
    while hook != None: 
        hook = pyautogui.locateOnScreen(config.hook_img, confidence=0.5, region=(account["FISHING_POSITION"][0], account["FISHING_POSITION"][1], account["FISHING_POSITION"][0] + config.IMG_HOOK_SIZE[0], account["FISHING_POSITION"][1] + config.IMG_HOOK_SIZE[1]))
        if hook == None:
            sleep(3)
            functions.log_message("Fixing fishing position...")
            set_fishing_rod(account)
        break

def some_actions(use_thread_kill_shiny, account):
    if use_thread_kill_shiny and functions.threadKillShiny.is_alive():
        functions.threadKillShiny.join()
    sleep(0.5)
    check_hook(use_thread_kill_shiny, account)
    functions.feed_pokemon()
    my_keyboard.press('scroll')
    my_keyboard.press('tab')

def apply_elixir_mode(use_thread_kill_shiny, account):
    use_thread_kill_shiny = True

    functions.log_message("Starting elixir mode!")
    sleep(0.5)

    release_pokemon("Releasing pokémon")
    functions.order_pokemon()
    functions.use_elixir("Using fisherman's elixir")
    
    start_time = time.time()

    while use_thread_kill_shiny and time.time() - start_time < 300:  # 5 minutes
        
        threadSomeActions = threading.Thread(target=some_actions, args=(use_thread_kill_shiny, account))

        fishing_position = set_fishing_rod(account)
        functions.start_and_join_thread(functions.threadKillShiny, functions.kill_shiny, (config.KILL_POKEMON_LIST, use_thread_kill_shiny))
        functions.start_and_join_thread(threadSomeActions, some_actions, (use_thread_kill_shiny,account))
        functions.wait_bubble(fishing_position)
        functions.minigame(config.counter)

    functions.start_and_join_thread(functions.threadKillShiny, functions.kill_shiny, (config.KILL_POKEMON_LIST, use_thread_kill_shiny))
    sleep(0.5)
    functions.log_message("Exiting elixir mode!")

use_thread_kill_shiny = True