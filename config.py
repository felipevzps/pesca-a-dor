IMG_BUBBLE_SIZE = (25,28)

# *** 1024x768 ***

RESOLUTION='1024x768'

#FISHING_POSITIONS = (280, 266)      #pewter bridge
#FISHING_POSITIONS = (748, 71)       #pewter paras/diglett
#FISHING_POSITIONS = (319, 110)      #hamlin Guru (fish on map)
#FISHING_POSITIONS = (397, 421)      #shamouti south

#MINIGAME_REGION = (160,150,100,400)
#HUNGRY_POSITION = (982,236,17,20)
#POKEBALL_POSITION = (838, 237)
#POKE_POSITION = (410, 242)

# *** 1920x1080 ***

FISHING_POSITIONS = (1646, 243)      #pewter paras/diglett HD
MINIGAME_REGION = (991,253,268,455)  #HD
HUNGRY_POSITION = (1877,244,17,20)   #HD
POKEBALL_POSITION = (1730, 246)      #HD
POKE_POSITION = (1337, 404)          #HD

#IMG PATH
bubble_img='images/{}/bubble.PNG'.format(RESOLUTION)
bar_img='images/{}/bar.PNG'.format(RESOLUTION)
fish_img='images/{}/fish_bin.PNG'.format(RESOLUTION)
shiny_img='images/{}/shiny.PNG'.format(RESOLUTION)
krabby_img='images/{}/krabby.PNG'.format(RESOLUTION)
tentacool_img='images/{}/tentacool.PNG'.format(RESOLUTION)
hungry_img='images/{}/hungry.PNG'.format(RESOLUTION)
hook_img='images/{}/hook.PNG'.format(RESOLUTION)

# Set the number of minigame_repeats
# A minigame appears for every 4 minutes on average
# minigame_repeats = 100 -> AFK fishing for ~6.5 hours

minigame_repeats = 100   
counter = 0