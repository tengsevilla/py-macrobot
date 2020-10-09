import time
import pyautogui
pyautogui.FAILSAFE = True

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.

town = False
    
def warp(yourwarp):
    pyautogui.press('enter')
    pyautogui.write(yourwarp, interval=0.05)
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(3)

def command(param1):
    pyautogui.press('enter')
    pyautogui.write(param1, interval=0.1)
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(.5)

def pub(pubwarp, pubname):
    warp(pubwarp)
    pyautogui.keyDown('altleft')
    pyautogui.press('c')
    pyautogui.keyUp('altleft')
    time.sleep(.5)
    pyautogui.write(pubname, interval=0.05)
    pyautogui.press('enter')
    pyautogui.keyDown('altleft')
    pyautogui.press('1')
    pyautogui.keyUp('altleft')

def storeall():
    for item in ALOOTID_ITEM_ID.split():
        command('@storeall id '+ item)
        
tick = 0
bop_tick = 0
bop_is_full = 36
# 00 Modify to your liking
ALOOTID_ITEM_ID = '12034 1015 969 985 984 7321 7312 604' #963 12053 971 1053 631 Clam Soup
AFK_AFTER_SKILL_COUNT = 600   # After N' times casted, go back in desired town
AFK_IN_TOWN_DURATION = 10 # In seconds
ALT_M_WARP_KEY_1 = '2'
ALT_M_WARP_KEY_2 = '3'
STORM_GUST_KEY = 'e'
VERMILLION_KEY = 'w'
# 00 Until here 

print('START!!!! added 5 sec delay please redirect to your game client\n')
print('Reminder of the following')
print('1. Close all applications, only the client is running')
print('2. Turn off your wireless mouse / unplug it')
print('3. Please dont repeat your mistake that almost got us banned')

time.sleep(6)
command('@alootid '+ ALOOTID_ITEM_ID)
command('@autoloot 10 ')
while True:
    if(tick >= AFK_AFTER_SKILL_COUNT):
        if(town == False):
            # 01 AFK in town actions. Modify from here
            warp('@warp manuk 273 144')
            time.sleep(3)
            pyautogui.click()
            warp('@go 31')
            command('/sit')
            storeall()
            # 01 Until here
            town = True;
            tick_merge = AFK_IN_TOWN_DURATION + AFK_AFTER_SKILL_COUNT
        if(tick >= tick_merge):
            tick = 0
            town = False;
            bop_tick = bop_tick + 1;
            print('Bop tick')
            print(str(bop_tick))

        #Normalize sleep
        time.sleep(1)
            
    else:
        modulo = bop_tick % 2

        if(modulo == 0):
            pyautogui.keyDown('altleft')
            pyautogui.press(ALT_M_WARP_KEY_1)
            pyautogui.keyUp('altleft')
            time.sleep(.1)
            pyautogui.press(STORM_GUST_KEY)
        else:
            pyautogui.keyDown('altleft')
            pyautogui.press(ALT_M_WARP_KEY_2) #Second warp 
            pyautogui.keyUp('altleft')
            time.sleep(.1)
            pyautogui.press(STORM_GUST_KEY)
        
        pyautogui.click()
        
        
    tick = tick + 1
    print(tick)
    


        
