import time
import pyautogui
pyautogui.FAILSAFE = True

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.

town = False

def npc_conversation():
    time.sleep(.5)
    pyautogui.press('enter')
    
    
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
# 00 Modify to your liking
ALOOTID_ITEM_ID = '12034'
AFK_AFTER_SKILL_COUNT = 650   # After N' times casted, go back in desired town
AFK_IN_TOWN_DURATION = 60 # In seconds
ALT_M_WARP_KEY = '3'
STORM_GUST_KEY = 'e'
# 00 Until here 

print('START!!!! added 5 sec delay please redirect to your game client\n')
print('Reminder of the following')
print('1. Close all applications, only the client is running')
print('2. Turn off your wireless mouse / unplug it')
print('3. Please dont repeat your mistake that almost got us banned')

time.sleep(5)
command('@alootid '+ ALOOTID_ITEM_ID)
while True:
    if(tick >= AFK_AFTER_SKILL_COUNT):
        if(town == False):
            # 01 AFK in town actions. Modify from here
            warp('@warp new_1-1 44 103')
            command('/sit')
            storeall()
            # 01 Until here
            town = True;
            tick_merge = AFK_IN_TOWN_DURATION + AFK_AFTER_SKILL_COUNT
        if(tick >= tick_merge):
            tick = 0
            town = False;

        #Normalize sleep
        time.sleep(1)
            
    else:
        
        pyautogui.keyDown('altleft')
        pyautogui.press(ALT_M_WARP_KEY)
        pyautogui.keyUp('altleft')
        time.sleep(.2)
        pyautogui.press(STORM_GUST_KEY)
        pyautogui.click()
        
        
    tick = tick + 1
    print(tick)
    


        
