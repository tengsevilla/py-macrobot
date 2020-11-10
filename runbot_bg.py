import time
import pyautogui
import random
pyautogui.FAILSAFE = True

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.

xMin = screenWidth / 2 - ((screenWidth / 2) / 2)
xMax = screenWidth / 2 + ((screenWidth / 2) / 2)

yMin = screenHeight / 2 - ((screenHeight / 2) / 2)
yMax = screenHeight / 2 + ((screenHeight / 2) / 2)

#pyautogui.moveTo(icon, duration=.5)
joining_bg = False

while True:
    bool_bg = check_bg_icon()

    if(bool_bg):
        start_bg()
        time.sleep(5) #Add delay when BG is done
    else:
        if(!joining_bg):
            join_bg()
        #else: Do nothing. Sit down
            
        

def join_bg():
    command('@go 13')
    time.sleep(3)
    command('/sit')
    
    command('@joinbg')
    #TODO: Join bg select option sequence

    joining_bg = True
    time.sleep(.5)

def check_bg_icon():
    ret = False
    icon = pyautogui.locateCenterOnScreen('images/search_icon.PNG')

    if(icon != None): # BG Icon is located
        ret = True

    return ret

def start_bg(): 
    while True:
        randX = random.randint(xMin, xMax)
        randY = random.randint(yMin, yMax)
        #Walk
        pyautogui.click(x=randX, y=randY, clicks=1, interval=1, button='left')
        print(randX, randY)
        #TODO: Skill sequence
        if(!check_bg_icon()):
            joining_bg = False
            break
        time.sleep(1)

#Common function
def command(param1):
    pyautogui.press('enter')
    pyautogui.write(param1, interval=0.03)
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(.5)

