import pyautogui
from pyautogui import *
from time import sleep  
from random import randint
from random import uniform

Working = False

def say(message):
    timeString = time.strftime("[%H:%M:%S]")
    botName = "BombCryto"
    version = "3.0"
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
    for file in os.listdir('target'):
        if file.endswith(".png"):
            split = file.split('.')
            if split[0] == name:
                return pyautogui.locateCenterOnScreen('target/'+file, confidence=confidence, grayscale=grayscale)

say("Starting...")
while True:

    ErroScreen = getTarget('ErroScreen')
    if ErroScreen:
        say("Erro...")
        click(ErroScreen, sleepTime=1)
        pyautogui.hold('ctrl')
        pyautogui.press('f5')

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

    TeasureHunt = getTarget('TeasureHunt')
    if TeasureHunt and Working:
        say("Starting TeasureHunt...")
        click(TeasureHunt, sleepTime=5)

    Heroes = getTarget('Heroes')
    if Heroes:
        say("Menu Heroes...")
        click(Heroes, sleepTime=1)

    
    InGameBack = getTarget('InGameBack')
    if InGameBack and Working:
        sleepTime = uniform(180,300)
        say("Waiting {} minutes...".format(sleepTime/60))
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

        WorkOn = getTarget('WorkOn', grayscale=False, confidence=0.98)
        WorkOff = getTarget('WorkOff', grayscale=False, confidence=0.98)
        StaminaFull = getTarget('StaminaFull')

        if WorkOn:
            say("Heroes in WorkOn...")
            Working = True
            HeroMenuClose = getTarget('HeroMenuClose')
            if HeroMenuClose:
                click(HeroMenuClose, sleepTime=1)

        elif WorkOff:
            say("Heroes in WorkOff...")
            Working = False
            StaminaFull = getTarget('StaminaFull')
            if StaminaFull:
                say("Stamina Full...")
                workAll = getTarget('workAll')
                if workAll:
                    say("Working All...")
                    click(workAll, sleepTime=1)

        elif not StaminaFull:
            say("Waiting for Stamina...")
            Working = False
            sleep(uniform(60, 120))
            HeroMenuClose = getTarget('HeroMenuClose')
            if HeroMenuClose:
                click(HeroMenuClose, sleepTime=1)
             
        

        