import pyautogui
from os import listdir
from time import sleep, strftime
from random import randint, uniform

timeString = strftime("[%H:%M:%S]")
botName = "BombCryto"
version = "3.1"
Working = False

def say(message):
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

input('{} {} {}: {}'.format(timeString, botName, version, 'Press Enter to start'))
say("Starting...")
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
            say("Waiting for Stamina or WorkOn...")
            sleep(uniform(30,60))    
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
