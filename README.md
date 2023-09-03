# pesca-a-dor

This document describes the operation and use of [pesca-a-dor](https://github.com/felipevzps/pesca-a-dor), developed to automate the fishing process in the [PxG](https://www.pokexgames.com/). This bot has been developed to `fish`, `cast spells on shiny Pokémon`, `capture shiny Pokémon`, `collect loot`, and `solve the periodic fishing challenge` that appears on the screen every 5 minutes, allowing uninterrupted fishing.

![](images/desafio_de_pesca.gif)

## Requirements

```bash
pip install pyautogui
pip install keyboard
pip install Pillow
pip install opencv-python
```

## Usage

Before proceeding, reduce your monitor resolution to `1024x768`. This step is essential for accurately obtaining screen coordinates for specific variables within the software. These variables include:

```python
FISHING_POSITIONS = (280, 382)    # The location where the bait will be cast
IMG_BUBBLE_SIZE = (25, 28)        # The size of the bubble image
POKEBALL_POSITION = (838, 237)    # The position of the Pokémon's Pokéball
POKE_POSITION = (410, 242)        # The position where the Pokémon will remain stationary
```

Please note the following:

To acquire the coordinates for each of these positions, you must execute [locateOnScreen.py](https://github.com/felipevzps/pesca-a-dor/blob/main/locateOnScreen.py) within vscode and hover your mouse over the desired locations while the script is running. For instance, to obtain the coordinates for `POKEBALL_POSITION`, position your mouse cursor over the Pokémon pokéball and retrieve the coordinates from the first print statement generated by the script (e.g., `print(pyautogui.position())`).

Ensuring that your mouse is positioned accurately during this process is crucial for obtaining precise left and top coordinates for your defined screen positions.

After getting and adding the coordinates in the code of [pesca-a-dor.py](https://github.com/felipevzps/pesca-a-dor/blob/main/pesca-a-dor.py), run the bot inside vscode, minimize the vscode and press `P` ingame to start fishing.

![](https://github.com/felipevzps/pesca-a-dor/blob/main/images/positions.PNG)

## Achievements

```
27/04/2023 - 1st night 100% AFK
04:08 You caught a Pokémon! (Krabby).
04:08 You've wasted: 144 Ultra Balls and 407 Net Balls to catch it.
```

```
23:26 You caught a Pokémon! (Krabby).
23:26 You've wasted: 200 Net Balls to catch it.
```

```
05:47 You caught a Pokémon! (Krabby).
05:47 You've wasted: 20 Net Balls to catch it.
```

```
00:06 You caught a Pokémon! (Krabby).
00:06 You've wasted: 499 Net Balls to catch it.
```
