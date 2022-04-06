from ast import Break
from cv2 import repeat
import pyautogui
from pyautogui import *
from time import sleep  
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
