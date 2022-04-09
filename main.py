import pyautogui
from os import listdir
from time import sleep, strftime, time
from random import randint, uniform

botName = "BombCryto"
version = "3.1"
Working = False

time_at_screen = 1 #Take screnshot in # hors
time_to_start = 0 #Time started to take screenshot
time_to_end = 0 #Time end to take screenshot

def say(message):
    timeString = strftime("[%H:%M:%S]")
    print('{} {} {}: {}'.format(timeString, botName, version, message))

def click(location, sleepTime=0.1, click= True):
    interval = uniform(0.1, 0.3)
    pyautogui.moveTo(location, duration=interval)
    sleep(interval)
    if click:
        pyautogui.click()
        sleep(interval)
    sleep(sleepTime)

def getTarget(name, confidence = 0.9, grayscale=False):
    for file in listdir('target'):
        if file.endswith(".png"):
            split = file.split('.')
            if split[0] == name:
                return pyautogui.locateCenterOnScreen('target/'+file, confidence=confidence, grayscale=grayscale)

def screenshot():
    global time_to_end
    global time_to_start

    if time_to_start == 0:
        time_to_start = time()
        time_to_end = time_at_screen * 60 * 60
        say('Start {:.0f} - End {}'.format(time_to_start - time(), time_to_end))
    
    if time() - time_to_start >= time_to_end and time_to_start != 0:
        chest = getTarget('chest')
        if chest:
            click(chest)
            sleep(0.5)
            pyautogui.screenshot('screenshots/{}-{}.png'.format(botName, strftime("%H-%M-%S")))
            say('Saving screenshot')
            chestClose = getTarget('chestClose')
            if chestClose:
                click(chestClose)
                time_to_start = 0
                sleep(0.5)

say("Press Enter to start")
input()
while True:

    ErroScreen = getTarget('ErroScreen')
    if ErroScreen:
        say("Erro...")
        click(ErroScreen, sleepTime=1)
        pyautogui.hold('ctrl')
        pyautogui.press('f5')

    #Login
    LoginScreen = getTarget('LoginScreen')
    if LoginScreen:
        Connect = getTarget('Connect')
        if Connect:
            say("Connecting...")
            click(Connect, sleepTime=5)
        
    MetaConnect = getTarget('MetaConnect')
    if MetaConnect:
        say("Connecting MetaMask...")
        click(MetaConnect, sleepTime=5)
        
    AssinarMeta = getTarget('AssinarMeta')
    if AssinarMeta:
        say("Assinando MetaMask...")
        click(AssinarMeta, sleepTime=5)
    #END Login

    screenshot()

    TeasureHunt = getTarget('TeasureHunt')
    if TeasureHunt and Working:
        say("Starting TeasureHunt...")
        click(TeasureHunt, sleepTime=5)

    Heroes = getTarget('Heroes')
    if Heroes:
        say("Menu Heroes...")
        click(Heroes, sleepTime=uniform(2,3))
    
    InGameBack = getTarget('InGameBack')
    if InGameBack and Working:
        sleepTime = randint(180,300)
        sleep_Text = str("{0:.2f}".format(sleepTime/60)).split('.')
        say("Waiting [00:0{}:{}]".format(int(sleep_Text[0]), int(sleep_Text[1])))
        sleep(sleepTime)
        say("Returning to menu to save progress...")
        Working = False
        click(InGameBack, sleepTime=1)
    elif InGameBack and not Working:
        Working = False
        say("Returning to menu...")
        click(InGameBack, sleepTime=1)
    
    HeroMenu = getTarget('HeroMenu')
    if HeroMenu:
        StaminaFull = getTarget('StaminaFull')
        WorkOn = getTarget('WorkOn', confidence=0.99)

        if not StaminaFull and not WorkOn:
            sleep_Time = uniform(30,60)
            say("Waiting {:.1f} sec for Stamina or WorkOn...".format(sleep_Time))
            sleep(sleep_Time)    
            StaminaFull = getTarget('StaminaFull')
            WorkOn = getTarget('WorkOn')

            HeroMenuClose = getTarget('HeroMenuClose')
            if HeroMenuClose:
                click(HeroMenuClose, sleepTime=1)
                continue

            if StaminaFull or WorkOn:
                continue

        elif WorkOn:
            say("Hero(s) in 'WorkON' ")
            Working = True
            HeroMenuClose = getTarget('HeroMenuClose')
            if HeroMenuClose:
                click(HeroMenuClose, sleepTime=1)
                continue

        elif StaminaFull:
            say("Stamina is full...")
            workAll = getTarget('workAll')
            if workAll:
                click(workAll, sleepTime=1)
                continue
