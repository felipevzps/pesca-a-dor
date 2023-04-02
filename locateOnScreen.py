import pyautogui
import my_keyboard

#IMG PATH
bubble_img='bubble_1024x768_vermilion.PNG'
bar_img='bar_1024x768.PNG'
fish_img='fish_1024x768.PNG'

#POSITIONS
#vermilion
FISHING_POSITIONS = (272, 299)
IMG_BUBBLE_SIZE = (39,40)
MINIGAME_REGION_BAR = (189,555,15,38)
MINIGAME_REGION_FISH = (236,178,14,14)

#pyautogui.PAUSE = 0.1 # default
pyautogui.PAUSE = 0.01 

while True:
    bubble = pyautogui.locateOnScreen(bubble_igm, confidence=0.7)#, region=FISHING_POSITIONS+IMG_BUBBLE_SIZE)
    bar = pyautogui.locateOnScreen(bar_img, confidence=0.7)#, region=MINIGAME_REGION_BAR)
    fish = pyautogui.locateOnScreen(fish_img, confidence=0.7, grayscale=True)#, region=MINIGAME_REGION_FISH)
    print("bubble",bubble)
    print("bar",bar)
    print("fish",fish)
    if bar != None and fish != None:
        if bar.top > fish.top:
            print('pressing space')
        else:
            print('realising space')
