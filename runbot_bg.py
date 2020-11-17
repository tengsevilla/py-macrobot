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
status = 'waiting';
print('START!!!! added 5 sec delay please redirect to your game client\n')
print('Reminder of the following')
print('1. Close all applications, only the client is running')
print('2. Turn off your wireless mouse / unplug it')
print('3. Please dont repeat your mistake that almost got us banned')

time.sleep(6)

def join_bg():
    print('Joining bg...')
    command('/sit')
    
    command('@joinbg')
    #TODO: Join bg select option sequence
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    
    time.sleep(.5)

def check_npc_icon():
    ret = False
    icon = pyautogui.locateCenterOnScreen('images/npc_icon.PNG')
    if(icon != None): # BG Icon is located
        ret = True

    return ret

#Common function
def command(param1):
    pyautogui.press('enter')
    pyautogui.write(param1, interval=0.03)
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(.5)


while True:
    print('Status: ', status)
    npc_exist = check_npc_icon()

    if(status == 'waiting'):
        if(npc_exist == True):
            join_bg()
            status = 'joining'

    if(status == 'joining'):
        if(npc_exist == False):
            status = 'onbg'
           

    if(status == 'onbg'):
        randX = random.randint(xMin, xMax)
        randY = random.randint(yMin, yMax)
        
        #TODO: Skill sequence

        if(npc_exist == True):
            time.sleep(5)
            status = 'waiting'
        else:
            #Walk
            pyautogui.click(x=randX, y=randY, clicks=1, interval=.2, button='left')
            time.sleep(3)
        

    #if(npc_exist == True):
     #   if(joining_bg == False):
    #        join_bg()
    #        joining_bg = True
    #    else:
    #        joining_bg = False
            

    #if(npc_exist == False):
     #   if(joining_bg == True):
            
            
        
        
        
        
            
    #time.sleep(1)
