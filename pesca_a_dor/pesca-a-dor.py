from pyautogui import *
import keyboard
import config
import threading
import functions

print(">>> Press 'P' to start <<<")
keyboard.wait('p')

functions.log_message("Started fishing")

while config.counter < config.minigame_repeats:
    
    fishing_position = functions.set_fishing_rod()

    functions.start_and_join_thread(functions.threadKillShiny, functions.kill_shiny, (config.KILL_POKEMON_LIST,))
    functions.start_and_join_thread(functions.threadSomeActions, functions.some_actions)

    if functions.constant_search_dragon() and config.USE_THREAD_BALL_DRAGON:
        functions.threadSearchDragon = threading.Thread(target=functions.ball_dragon)
        functions.threadSearchDragon.start()

    functions.wait_bubble(fishing_position)
    config.counter = functions.minigame(config.counter)

    if functions.find_elixir() and config.FISH_MAGIKARP:
        functions.apply_elixir_mode()

    functions.logout(config.counter)
    
functions.join_thread_if_alive(functions.threadSearchDragon)    