import time
import pyautogui
pyautogui.FAILSAFE = True

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.

town = False
    
def warp(yourwarp):
    pyautogui.press('enter')
    pyautogui.write(yourwarp, interval=0.03)
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(3)

def command(param1):
    pyautogui.press('enter')
    pyautogui.write(param1, interval=0.03)
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
warp_seq = 1
# 00 Modify to your liking
ALOOTID_ITEM_ID = '12034 678 12114 12115 12116 12117 607 608 969 7444'
ALTM_WARP_UPTO_KEY_NUM = 4      # Sequence should be incremental. Alt 1, Alt 2, Alt 3
AFK_AFTER_SKILL_COUNT = 500     # After N' times casted, go back in desired town
AFK_IN_TOWN_DURATION = 5        # In seconds
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
#command('@autoloot 10 ')
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
            warp_seq = warp_seq + 1;
            #print('Bop tick')
            print(str(warp_seq))

        #Normalize sleep
        time.sleep(1)
            
    else:
        if(warp_seq > ALTM_WARP_UPTO_KEY_NUM):
            warp_seq = 1 #Reset
            
        pyautogui.keyDown('altleft')
        pyautogui.press(str(warp_seq)) 
        pyautogui.keyUp('altleft')
        time.sleep(.2)
        pyautogui.press(STORM_GUST_KEY)
        pyautogui.click()

        # If need to cast LOV in the map, please add the alt M here.
        if(warp_seq == 0):
            time.sleep(.7)
            pyautogui.press(VERMILLION_KEY)
            pyautogui.click()
        
        
    tick = tick + 1
    #print(tick)
    
    


        
