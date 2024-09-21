from pyautogui import *
import keyboard
import config
import threading
import functions
import json

print(">>> Press 'P' to start <<<")
keyboard.wait('p')

functions.log_message("Started fishing")

with open("pesca_a_dor/infos.json", "r") as file:
    config_json = json.load(file)

while config.counter < config.minigame_repeats: 

    fishing_position = functions.set_fishing_rod()

    functions.start_and_join_thread(functions.threadKillShiny,functions.kill_shiny,(config.KILL_POKEMON_LIST, config_json["USE_THREAD_KILL_SHINY"]))
    functions.start_and_join_thread(functions.threadSomeActions,functions.some_actions,(config_json["USE_THREAD_KILL_SHINY"],))

    if functions.constant_search_dragon () and config_json["USE_THREAD_BALL_DRAGON"]:

        functions.threadSearchDragon = threading.Thread(target=functions.ball_dragon)
        functions.threadSearchDragon.start()
        
    # To catch normal dratini / dragonair
    #if config_json["USE_THREAD_BALL_DRAGON"]:
        #unctions.threadSearchNormal = threading.Thread(target=functions.ball_normal)
        #functions.threadSearchNormal.start()

    functions.wait_bubble(fishing_position)
    config.counter = functions.minigame(config.counter)

    if functions.find_elixir() and config_json["FISH_MAGIKARP"]:
        config_json["USE_THREAD_KILL_SHINY"] = functions.apply_elixir_mode(config_json["USE_THREAD_KILL_SHINY"])

    functions.logout(config.counter)

functions.join_thread_if_alive(functions.threadSearchDragon)
    