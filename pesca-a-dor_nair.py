from pyautogui import *
import pyautogui
from time import sleep
import time
import keyboard
import threading
import config
import functions

pyautogui.PAUSE = 0.01 #default = 0.1

# *** START ***

texto = "{}: Started fishing\n".format(functions.current_time)
with open(functions.log, "a") as log_output:
    log_output.write(texto)

print(functions.current_time, ": Started fishing")

keyboard.wait('p')

while config.counter < config.minigame_repeats:
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    with open(functions.log, "a") as log_output:
        texto_repetido = "{}: ...\n".format(current_time)
        log_output.write(texto_repetido)

    print(current_time,": ...")

    fishing_position = functions.set_fishing_rod()

    if not functions.threadSomeActions.is_alive():
        functions.threadSomeActions = threading.Thread(target=functions.some_actions)
        functions.threadSomeActions.start()

    #Wait until the thread terminates    
    functions.threadSomeActions.join()
    
    sleep(0.5)
    functions.wait_bubble(fishing_position)
    texto_minigame = functions.minigame()
    texto_log_minigame = "{}: {}\n".format(current_time, texto_minigame)

    with open(functions.log, "a") as log_output:
        if texto_minigame != None:
            sleep(1)
            log_output.write(str(texto_log_minigame))
            config.counter += 1

    #Logout after the end of minigame_repeats
    if config.minigame_repeats == config.counter:
        sleep(20)
        keyboard.press_and_release("ctrl+q")
        sleep(1)
        keyboard.press_and_release("enter")

# *** END ***