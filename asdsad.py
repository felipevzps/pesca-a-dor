import pyautogui
import my_keyboard

#while True:
#    region = pyautogui.locateOnScreen('bar.PNG', confidence=0.6)
#    print(region.top)

#vermilion
FISHING_POSITIONS = (272, 299)
IMG_BUBBLE_SIZE = (39,40)
MINIGAME_REGION_BAR = (189,555,15,38)
MINIGAME_REGION_FISH = (236,178,14,14)

#pyautogui.PAUSE = 0.1 # default
pyautogui.PAUSE = 0.01 # tentando rodar mais rapdo

#fish = True
#while fish != None:
while True:
    bubble = pyautogui.locateOnScreen('bubble_1024_vermilion.PNG', confidence=0.7)#, region=FISHING_POSITIONS+IMG_BUBBLE_SIZE)
    #infos = pyautogui.locateOnScreen('infos2.PNG', confidence=0.7, region=MINIGAME_REGION_BAR)
    bar = pyautogui.locateOnScreen('bar_1024.PNG', confidence=0.7)#, region=MINIGAME_REGION_BAR)
    fish = pyautogui.locateOnScreen('fish_1024.PNG', confidence=0.7, grayscale=True)#, region=MINIGAME_REGION_FISH)
    print("bubble",bubble)
    #print("infos",infos)
    print("bar",bar)
    print("fish",fish)
    if bar != None and fish != None:
        if bar.top > fish.top:
            print('pressing space')
            #my_keyboard.key_down(0x39)
        else:
            print('realising space')
            #my_keyboard.release_key(0x39)
    #else:
        #my_keyboard.key_down(0x39)
        #my_keyboard.release_key(0x39)