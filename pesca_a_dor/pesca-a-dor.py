from pyautogui import *
from time import sleep
import time
import keyboard
import threading
import config
import functions

print(f"{functions.current_time} : Press 'P' to start")
keyboard.wait('p')                                   # Press 'P' to start

texto = "{}: Started fishing\n".format(functions.current_time)
with open(functions.log, "a") as log_output:
    log_output.write(texto)
print(functions.current_time, ": Started fishing")

while config.counter < config.minigame_repeats:
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    with open(functions.log, "a") as log_output:
        texto_repetido = "{}: ...\n".format(current_time)
        log_output.write(texto_repetido)
    print(current_time,": ...")

    fishing_position = functions.set_fishing_rod()

    if not functions.threadKillShiny.is_alive():
        functions.threadKillShiny = threading.Thread(target=functions.kill_shiny, args=(config.KILL_POKEMON_LIST,))
        functions.threadKillShiny.start()
    functions.threadKillShiny.join()                 # Wait until the thread terminates  

    if not functions.threadSomeActions.is_alive():
        functions.threadSomeActions = threading.Thread(target=functions.some_actions)
        functions.threadSomeActions.start()
    functions.threadSomeActions.join()               # Wait until the thread terminates
    
    if functions.constant_search_dragon() and config.USE_THREAD_BALL_DRAGON: 
        functions.threadSearchDragon = threading.Thread(target=functions.ball_dragon)
        functions.threadSearchDragon.start()

    sleep(0.5)
    functions.wait_bubble(fishing_position)
    texto_minigame = functions.minigame()
    texto_log_minigame = "{}: {}\n".format(current_time, texto_minigame)

    with open(functions.log, "a") as log_output:
        if texto_minigame != None:
            sleep(1)
            log_output.write(str(texto_log_minigame))
            config.counter += 1

    if config.minigame_repeats == config.counter:    # Logout after the end of minigame_repeats
        sleep(20)
        keyboard.press_and_release("ctrl+q")
        sleep(1)
        keyboard.press_and_release("enter")

if functions.threadSearchDragon is not None and functions.threadSearchDragon.is_alive():
    functions.threadSearchDragon.join()              # Wait until the thread terminates