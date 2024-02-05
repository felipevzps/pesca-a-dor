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
import json

pyautogui.PAUSE = 0.01                         # Default = 0.1

today_var = datetime.date.today()
today_text = today_var.strftime("%d%m%Y")
log="logs/{}.txt".format(today_text)

with open("pesca_a_dor/infos.json", "r") as file:
    config_json = json.load(file)

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
    with open("pesca_a_dor/infos.json", "r") as file:
        config_json = json.load(file)
    #area = config.FISHING_POSITIONS
    area = config_json["FISHING_POSITION"]
    #area_center = pyautogui.center(area+config.IMG_BUBBLE_SIZE)
    #area_center = pyautogui.center((area[0], area[1], area[0]+config.IMG_BUBBLE_SIZE[0],area[1]+config.IMG_BUBBLE_SIZE[0]))
    area_center = pyautogui.center((area[0], area[1], config.IMG_BUBBLE_SIZE[0], config.IMG_BUBBLE_SIZE[1]))
    pyautogui.moveTo(area_center)
    sleep(0.5)
    pyautogui.click(button="left")
    my_keyboard.press('NUNLOCK')
    return area

def wait_bubble(fishing_position):
    while True:
        #bubble = pyautogui.locateOnScreen(config.bubble_img, confidence=0.7, region=fishing_position+config.IMG_BUBBLE_SIZE)
        bubble = pyautogui.locateOnScreen(config.bubble_img, confidence=0.7, region=(fishing_position[0], fishing_position[1], fishing_position[0] + config.IMG_BUBBLE_SIZE[0], fishing_position[1] + config.IMG_BUBBLE_SIZE[1]))
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

def kill_shiny(pokemon_list, use_thread_kill_shiny):
    if use_thread_kill_shiny:
        for pokemon_info in pokemon_list:
            pokemon_name, img_path, confidence = pokemon_info
            sleep(0.5)
            shiny_found = False
            while True:
                shiny = pyautogui.locateOnScreen(img_path, confidence=confidence, region=config.REGION_BATTLE)
                if shiny == None:
                    break
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
                shiny_found = True

            if shiny_found and pokemon_name == "pokémon":
                ball_shiny("Shiny Krabby", config.krabby_img, 'F10', 0.7)
                ball_shiny("Shiny Tentacool", config.tentacool_img, 'F11', 0.85)
                ball_shiny("Shiny Giant Magikarp", config.shiny_giant_karp_img, 'F10', 0.85, offset_x=15, offset_y=15)
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
                sleep(1)
            pyautogui.moveTo(pokemon_center[0] + offset_x, pokemon_center[1] + offset_y)
            sleep(0.8)
            my_keyboard.press(key)
            sleep(0.5)
            mouseDown(pokemon_center[0] + offset_x, pokemon_center[1] + offset_y)
            mouseUp()
            return True
        else:
            return False   

def some_actions(use_thread_kill_shiny):
    if use_thread_kill_shiny and threadKillShiny.is_alive():
        threadKillShiny.join()
    sleep(0.5)
    check_hook(use_thread_kill_shiny)
    feed_pokemon()
    #my_keyboard.press('esc')
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
    #global USE_THREAD_BALL_DRAGON
    log_message("Wild pokémon appeared!")
    while True:
        #config.USE_THREAD_BALL_DRAGON = False
        config_json["USE_THREAD_BALL_DRAGON"] = False
        sleep(0.5)
        dratini = ball_shiny("Shiny Dratini", config.dratini_img, 'F12', 0.73)
        dragonair = ball_shiny("Shiny Dragonair", config.dragonair_img, 'F12', 0.69)

        # fishing with two characters - only one catching!
        krabby = ball_shiny("Shiny Krabby", config.krabby_img, 'F10', 0.7)
        tentacool = ball_shiny("Shiny Tentacool", config.tentacool_img, 'F11', 0.85)

        if dratini or dragonair:
        #if dratini or dragonair or krabby or tentacool:
            #config.USE_THREAD_BALL_DRAGON = True
            config_json["USE_THREAD_BALL_DRAGON"] = True
            break
        sleep(1)

def find_elixir():
    #global FISH_MAGIKARP
    use_elixir = config_json["FISH_MAGIKARP"]
    #while config_json["FISH_MAGIKARP"]:
    while use_elixir:
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
    my_keyboard.press_ctrl_key('F2', delay=0)

def use_elixir(message):
    sleep(1)    
    log_message(message)
    my_keyboard.press_ctrl_key('F3', delay=0)

def get_pokemon_info():
    electabuzz = pyautogui.locateOnScreen(config.electabuzz_img, confidence=0.9, region=(1717, 228, 34, 34))
    shedinja = pyautogui.locateOnScreen(config.shedinja_img, confidence=0.9, region=(1717, 228, 34, 34))
    if electabuzz != None:
        pokemon = "electabuzz"
    elif shedinja != None:
        pokemon = "shedinja"
    return pokemon 

def apply_elixir_mode(use_thread_kill_shiny):
    #global FISH_MAGIKARP
    original_use_thread_kill_shiny = use_thread_kill_shiny
    use_thread_kill_shiny = True

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

    while config_json["FISH_MAGIKARP"] and time.time() - start_time < 300:  # 5 minutes
        
        fishing_position = set_fishing_rod()
        start_and_join_thread(threadKillShiny, kill_shiny, (config.KILL_POKEMON_LIST, use_thread_kill_shiny))
        start_and_join_thread(threadSomeActions, some_actions, (use_thread_kill_shiny,))
        wait_bubble(fishing_position)
        minigame(config.counter)

    start_and_join_thread(threadKillShiny, kill_shiny, (config.KILL_POKEMON_LIST, use_thread_kill_shiny))
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
        #order_pokemon_north()

    #config.USE_THREAD_KILL_SHINY = original_use_thread_kill_shiny 
    config_json["USE_THREAD_KILL_SHINY"] = original_use_thread_kill_shiny 
    
    use_bait("Applying bait")
    sleep(1)
    return config_json["USE_THREAD_KILL_SHINY"]

def check_hook(use_thread_kill_shiny):
    if use_thread_kill_shiny and threadKillShiny.is_alive():
        threadKillShiny.join()
    sleep(0.5)
    hook = True
    while hook != None: 
        # (fishing_position[0], fishing_position[1], fishing_position[0] + config.IMG_BUBBLE_SIZE[0], fishing_position[1] + config.IMG_BUBBLE_SIZE[1])
        #hook = pyautogui.locateOnScreen(config.hook_img, confidence=0.5, region=config_json["FISHING_POSITION"]+config.IMG_HOOK_SIZE)
        hook = pyautogui.locateOnScreen(config.hook_img, confidence=0.5, region=(config_json["FISHING_POSITION"][0], config_json["FISHING_POSITION"][1], config_json["FISHING_POSITION"][0] + config.IMG_HOOK_SIZE[0], config_json["FISHING_POSITION"][1] + config.IMG_HOOK_SIZE[1]))
        if hook == None:
            sleep(3)
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
    my_keyboard.press('F2')
    my_keyboard.press('F2')
    sleep(0.2)
    my_keyboard.press('F2')
    sleep(0.3)
    my_keyboard.press('F2')
    sleep(0.3)
    my_keyboard.press('F2')
    sleep(0.2)
    my_keyboard.press('tab')

def order_pokemon_north():
    pyautogui.moveTo(1323, 331, duration=0.3)
    my_keyboard.press('F2')
    my_keyboard.press('F2')
    my_keyboard.press('F2')
    sleep(0.2)
    my_keyboard.press('F2')
    sleep(0.3)
    my_keyboard.press('F2')
    sleep(0.3)
    my_keyboard.press('F2')
    sleep(0.2)
    my_keyboard.press('tab')

def revive():
    pyautogui.moveTo(config.POKEBALL_POSITION, duration=0.3)
    sleep(0.1)
    pyautogui.click(button="right", duration=0.8)
    sleep(0.1)
    my_keyboard.press('F1', delay=0)
    sleep(0.1)
    pyautogui.click(button="right", duration=0.8)

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

#threadKillShiny = threading.Thread(target=kill_shiny, args=(config.KILL_POKEMON_LIST, config.USE_THREAD_KILL_SHINY))
threadKillShiny = threading.Thread(target=kill_shiny, args=(config.KILL_POKEMON_LIST, config_json["USE_THREAD_KILL_SHINY"]))

#threadSomeActions = threading.Thread(target=some_actions, args=(config_json["USE_THREAD_KILL_SHINY"],))
threadSomeActions = threading.Thread(target=some_actions, args=(config_json["USE_THREAD_KILL_SHINY"],))

#threadSearchDragon = threading.Thread(target=ball_dragon, args=(config.USE_THREAD_BALL_DRAGON,))
threadSearchDragon = threading.Thread(target=ball_dragon, args=(config_json["USE_THREAD_BALL_DRAGON"],))