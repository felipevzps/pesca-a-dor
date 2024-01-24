import sys
sys.path.append('C:\\Users\\PC\\Desktop\\pesca-a-dor-main')

from pyautogui import *
import pyautogui
from time import sleep
import time
import datetime
import utils.my_keyboard as my_keyboard
import keyboard
import threading
import config

pyautogui.PAUSE = 0.01                         # Default = 0.1

today_var = datetime.date.today()
today_text = today_var.strftime("%d%m%Y")
log="logs/{}.txt".format(today_text)

def get_current_time():
    t = time.localtime()
    return time.strftime("%H:%M:%S", t)

def log_message(message):
    current_time = get_current_time()
    formatted_message = f"{current_time}: {message}\n"
    with open(log, "a") as log_output:
        log_output.write(formatted_message)
    print(current_time, ":", message)

def set_fishing_rod():
    log_message("...")
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

def minigame(counter):
    sleep(1)
    fish = True
    message = None
    while fish != None:
        bar = pyautogui.locateOnScreen(config.bar_img, confidence=0.7, region=config.MINIGAME_REGION)
        fish = pyautogui.locateOnScreen(config.fish_img, confidence=0.7, grayscale=True, region=config.MINIGAME_REGION)
        if bar != None and fish != None:
            message="Solving puzzle..."
            if bar.top > fish.top:
                my_keyboard.key_down(0x39)
            else:   
                my_keyboard.release_key(0x39)
        else:
            my_keyboard.key_down(0x39)  
            my_keyboard.release_key(0x39)
    if message != None:
        log_message(message)
        counter += 1
    return counter

def kill_shiny(pokemon_list, use_thread_kill_shiny=config.USE_THREAD_KILL_SHINY):
    if use_thread_kill_shiny:
        for pokemon_info in pokemon_list:
            pokemon_name, img_path, confidence = pokemon_info
            sleep(0.5)
            shiny = True
            while shiny != None:
                shiny = pyautogui.locateOnScreen(img_path, confidence=confidence)
                if shiny != None:
                    log_message("Wild {} appeared!".format(pokemon_name))
                    sleep(0.1)
                    my_keyboard.press('backspace')  # Use medicine on pokémon
                    sleep(0.1)
                    my_keyboard.press('F7')         # Mamaragan
                    sleep(0.1)
                    my_keyboard.press('F5')         # Electrify
                    sleep(0.1)
                    my_keyboard.press('F4')         # Thunder Wrath
                    sleep(0.1)
                    my_keyboard.press('F6')         # Discharge 
                    sleep(0.5)
                    revive()
                    order_pokemon()
                    sleep(0.5)
                    ball_shiny("Shiny Krabby", config.krabby_img, 'F10', 0.7)
                    ball_shiny("Shiny Tentacool", config.tentacool_img, 'F11', 0.85)
                    ball_shiny("Shiny Giant Magikarp", config.shiny_giant_karp_img, 'F10', 0.88, offset_x=15, offset_y=15)
                    ball_shiny("Shiny Magikarp", config.magikarp_img, 'F10', 0.9, offset_x=1, offset_y=1)

def ball_shiny(pokemon_name, img_path, key, confidence, offset_x=0, offset_y=0):
    sleep(0.5)
    pokemon_found = True
    while pokemon_found != None:
        pokemon_found = pyautogui.locateOnScreen(img_path, confidence=confidence)
        if pokemon_found != None:
            log_message("{} defeated!".format(pokemon_name))
            pokemon_center = pyautogui.center(pokemon_found)
            if offset_x > 0:
                pyautogui.moveTo(pokemon_center[0] + offset_x, pokemon_center[1] + offset_y)
                pyautogui.click(button="right")
                sleep(1)
                my_keyboard.press("right")
                sleep(0.5)
            pyautogui.moveTo(pokemon_center[0] + offset_x, pokemon_center[1] + offset_y)
            sleep(1)
            my_keyboard.press(key)
            sleep(0.5)
            mouseDown(pokemon_center[0] + offset_x, pokemon_center[1] + offset_y)
            mouseUp()
            return True
        else:
            return False   

def some_actions(use_thread_kill_shiny=config.USE_THREAD_KILL_SHINY):
    if use_thread_kill_shiny and threadKillShiny.is_alive():
        threadKillShiny.join()
    check_hook()
    sleep(0.5)
    feed_pokemon()
    my_keyboard.press('esc')
    my_keyboard.press('tab')

def constant_search_dragon():
    shiny = True
    while shiny != None:
        shiny = pyautogui.locateOnScreen(config.shiny_img, confidence=0.9)
        if shiny != None:
            return True
        else:
            sleep(1)
    return False

def ball_dragon():
    global USE_THREAD_BALL_DRAGON
    log_message("Wild pokémon appeared!")
    while True:
        config.USE_THREAD_BALL_DRAGON = False
        sleep(0.5)
        dratini = ball_shiny("Shiny Dratini", config.dratini_img, 'F12', 0.73)
        dragonair = ball_shiny("Shiny Dragonair", config.dragonair_img, 'F12', 0.69)
        if dratini or dragonair:
            config.USE_THREAD_BALL_DRAGON = True
            break
        sleep(1)

def find_elixir():
    global FISH_MAGIKARP
    while config.FISH_MAGIKARP:
        elixir = pyautogui.locateOnScreen(config.elixir_img, confidence=0.9, region=(1382, 879, 36,21))
        if elixir != None:
            return True
        else:
            return False

def change_pokemon(message):
    log_message(message)
    pyautogui.moveTo(config.POKEBALL_POSITION, duration=0.3)
    pyautogui.click(button="right")
    sleep(1)
    pyautogui.moveTo(1735, 306)
    sleep(0.5)
    pyautogui.dragTo(1735, 243, button="left", duration=1)
    sleep(0.5)
    pyautogui.click(1735, 242, button="right")
    sleep(1)

def use_bait(message):
    sleep(1)
    log_message(message)
    pyautogui.moveTo(1251, 898, duration=0.3)
    pyautogui.click(button="left")
    sleep(1)

def use_elixir(message):
    log_message(message)
    pyautogui.moveTo(1398, 898, duration=0.3)
    pyautogui.click(button="left")
    sleep(1)

def get_pokemon_info():
    electabuzz = pyautogui.locateOnScreen(config.electabuzz_img, confidence=0.9, region=(1717, 228, 34, 34))
    shedinja = pyautogui.locateOnScreen(config.shedinja_img, confidence=0.9, region=(1717, 228, 34, 34))
    if electabuzz != None:
        pokemon = "electabuzz"
    elif shedinja != None:
        pokemon = "shedinja"
    return pokemon 

def apply_elixir_mode():
    global FISH_MAGIKARP
    log_message("Starting elixir mode!")

    sleep(0.5)
    pokemon = get_pokemon_info()

    if pokemon == "shedinja":
        sleep(1)
        combat = pyautogui.locateOnScreen(config.combat_img, confidence=0.9, region=(960, 850, 110, 70))
        while combat != None:
            combat = pyautogui.locateOnScreen(config.combat_img, confidence=0.9, region=(960, 850, 110, 70))
            sleep(1)
        change_pokemon("Changing pokémon")
        order_pokemon()

    use_bait("Removing bait")
    use_elixir("Using fisherman's elixir")
    start_time = time.time()

    while config.FISH_MAGIKARP and time.time() - start_time < 300:  # 5 minutes
        
        fishing_position = set_fishing_rod()
        start_and_join_thread(threadKillShiny, kill_shiny, (config.KILL_POKEMON_LIST,))
        start_and_join_thread(threadSomeActions, some_actions)
        wait_bubble(fishing_position)
        minigame(config.counter)

    sleep(0.5)
    log_message("Exiting elixir mode!")

    if pokemon == "shedinja":
        sleep(1)
        combat = pyautogui.locateOnScreen(config.combat_img, confidence=0.9, region=(960, 850, 110, 70))
        while combat != None:
            combat = pyautogui.locateOnScreen(config.combat_img, confidence=0.9, region=(960, 850, 110, 70))
            sleep(1)
        change_pokemon("Changing pokémon")
        order_pokemon()

    use_bait("Applying bait")
    sleep(1)

def check_hook(use_thread_kill_shiny=config.USE_THREAD_KILL_SHINY):
    if use_thread_kill_shiny and threadKillShiny.is_alive():
        threadKillShiny.join()
    sleep(2)
    hook = True
    while hook != None: 
        hook = pyautogui.locateOnScreen(config.hook_img, confidence=0.5, region=config.FISHING_POSITIONS+config.IMG_HOOK_SIZE)
        if hook == None:
            log_message("Fixing fishing position...")
            set_fishing_rod()
        break

def feed_pokemon():
    while True:
        hungry = pyautogui.locateOnScreen(config.hungry_img, confidence=0.91, region=config.HUNGRY_POSITION)
        if hungry != None:
            log_message("Feeding pokémon...")
            my_keyboard.press('caps')
        break

def order_pokemon():
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

def revive():
    pyautogui.moveTo(config.POKEBALL_POSITION, duration=0.3)
    pyautogui.click(button="right", duration=0.8)
    my_keyboard.press('F1', delay=0)
    pyautogui.click(button="right", duration=0.8)
    sleep(0.5)

def start_and_join_thread(thread, target, args=()):
    if not thread.is_alive():
        thread = threading.Thread(target=target, args=args)
        thread.start()
    thread.join()

def join_thread_if_alive(thread):
    if thread is not None and thread.is_alive():
        thread.join()

def logout(counter):
    if config.minigame_repeats == counter:
        log_message("Session complete. Logging out now.")
        sleep(20)
        keyboard.press_and_release("ctrl+q")
        sleep(1)
        keyboard.press_and_release("enter")

threadKillShiny = threading.Thread(target=kill_shiny, args=(config.KILL_POKEMON_LIST,))
threadSomeActions = threading.Thread(target=some_actions)
threadSearchDragon = threading.Thread(target=ball_dragon)