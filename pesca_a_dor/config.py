# *** GLOBAL VARIABLES ***

USE_THREAD_KILL_SHINY = False        # Set as True/False if do/dont want to use threadKillShiny on main loop
USE_THREAD_BALL_DRAGON = True        # Set as True/False if do/dont want to project dragonair on main loop
FISH_MAGIKARP = True                 # Set as True to activate elixir mode 

#IMG_BUBBLE_SIZE = (25,28)           # bubble.PNG  (1024x768)
IMG_BUBBLE_SIZE = (26,28)            # bubble1.PNG (1920x1080)
IMG_HOOK_SIZE = (30, 30)

# *** 1024x768 ***

#FISHING_POSITIONS = (280, 266)      # pewter bridge
#FISHING_POSITIONS = (748, 71)       # pewter paras/diglett
#FISHING_POSITIONS = (319, 110)      # hamlin Guru (fish on map)
#FISHING_POSITIONS = (397, 421)      # shamouti south

#MINIGAME_REGION = (160,150,100,400)
#HUNGRY_POSITION = (982,236,17,20)
#POKEBALL_POSITION = (838, 237)
#POKE_POSITION = (410, 242)

# *** 1920x1080 ***

#FISHING_POSITIONS = (1646, 243)        # pewter paras/diglett
#FISHING_POSITIONS = (1574, 393)        # pewter-cerulean road (dragonair)
#FISHING_POSITIONS = (1391, 284)        # pewter-cerulean road (magikarp)

FISHING_POSITIONS = (1062, 284)        # vermilion west (dragonair)
#FISHING_POSITIONS = (1208, 321)        # hamlin lake

#FISHING_POSITIONS = (1464, 430)        # cerulean CP 
#FISHING_POSITIONS = (1537, 430)        # hamlin east 

MINIGAME_REGION = (991,253,268,455)  
HUNGRY_POSITION = (1877,244,17,20)   
POKEBALL_POSITION = (1730, 246)      
#POKE_POSITION = (1337, 404)            # north     
POKE_POSITION = (1292, 435)            # left 
# *** IMG PATH ***

RESOLUTION='1024x768'

bubble_img='images/{}/bubble1.PNG'.format(RESOLUTION)
bar_img='images/{}/bar.PNG'.format(RESOLUTION)
fish_img='images/{}/fish_bin.PNG'.format(RESOLUTION)
shiny_img='images/{}/shiny.PNG'.format(RESOLUTION)
krabby_img='images/{}/krabby.PNG'.format(RESOLUTION)
tentacool_img='images/{}/tentacool.PNG'.format(RESOLUTION)
dratini_img='images/{}/dratini.PNG'.format(RESOLUTION)
dragonair_img='images/{}/dragonair.PNG'.format(RESOLUTION)
giant_karp_img='images/{}/giant_karp.PNG'.format(RESOLUTION)
shiny_giant_karp_img='images/{}/shiny_giant_karp3.PNG'.format(RESOLUTION)
magikarp_img='images/{}/magikarp.PNG'.format(RESOLUTION)
shiny_karp_img='images/{}/shiny_karp.PNG'.format(RESOLUTION)
feebas_img='images/{}/feebas.PNG'.format(RESOLUTION)
hungry_img='images/{}/hungry.PNG'.format(RESOLUTION)
hook_img='images/{}/hook.PNG'.format(RESOLUTION)
elixir_img='images/{}/elixir.PNG'.format(RESOLUTION)
combat_img='images/{}/combat.PNG'.format(RESOLUTION)
electabuzz_img='images/{}/electabuzz.PNG'.format(RESOLUTION)
shedinja_img='images/{}/shedinja.PNG'.format(RESOLUTION)

# List of tuples containing pokemons to kill_shiny
KILL_POKEMON_LIST = [
    ("pokémon", shiny_img, 0.9),
    ("Feebas", feebas_img, 0.9),
    ("Giant Magikarp", giant_karp_img, 0.9),
]

# *** MINIGAME REPEATS ***
''' Set the number of minigame_repeats
    A minigame appears for every 4 minutes on average
    minigame_repeats = 100 -> AFK fishing for ~6.5 hours '''

minigame_repeats = 100   # 100
counter = 0