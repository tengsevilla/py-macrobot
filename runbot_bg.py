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

def perform_action():
    randA = random.randint(1, 9)
    randB = random.randint(1, 9)

    if(randA == randB):
        #Cast a skill
        print('Cast a skill:', randA)
        pyautogui.press(randA)
        pyautogui.click()
        
    ans = randA - randB
    if(ans == 0):
        #Send emote
        print('Send emote')
        command('/heh')

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
        time.sleep(3)
        randX = random.randint(xMin, xMax)
        randY = random.randint(yMin, yMax)
        rand_click = random.randint(1, 4)
        #TODO: Skill sequence

        if(check_npc_icon() == True):
            status = 'waiting'
            time.sleep(5)
        else:
            perform_action()
            #Walk
            pyautogui.click(x=randX, y=randY, clicks=rand_click, interval=.2, button='left')
            
        
            
        
        
        
        
            
    #time.sleep(1)
