from pyautogui import *
import pyautogui 
import time 
import random

working = False
mapcount = 0

def click(x,y):
        pyautogui.moveTo(x,y, random.uniform(0.5,1))
        pyautogui.mouseDown()
        time.sleep(random.uniform(0.1,0.3))
        pyautogui.mouseUp()


time.sleep(3)

while 1:

        #Verifica se apareceu a tela de erro. Se sim clica em OK
        if pyautogui.locateOnScreen('./src/ErroScreen.png', grayscale=True, confidence=0.8 ) != None or pyautogui.locateOnScreen('./src/connectionError.png', grayscale=True, confidence=0.8 ) != None:
                okButton = pyautogui.locateOnScreen('./src/OkErroScreen.png', grayscale=True, confidence=0.8 )
                x,y = pyautogui.center(okButton)
                print(' > Saindo da Tela de Erro')
                click(x,y)
                time.sleep(random.uniform(10,15))

        #Verifica se tem um botão pra conectar no jogo
        if pyautogui.locateOnScreen('./src/ConnectButton.png', grayscale=True, confidence=0.8 ) != None:
                herobutton = pyautogui.locateOnScreen('./src/ConnectButton.png', grayscale=True, confidence=0.8 )
                x,y = pyautogui.center(herobutton)
                print(' > Entrando na tela do jogo.')
                click(x,y)
                time.sleep(random.uniform(10,15))

                #Verifica se tem o botão da metamesk para se clica em conectar no jogo
                if pyautogui.locateOnScreen('./src/AssinarBtn.png', grayscale=True, confidence=0.8 ) != None:
                        herobutton = pyautogui.locateOnScreen('./src/AssinarBtn.png', grayscale=True, confidence=0.8 )
                        x,y = pyautogui.center(herobutton)
                        print(' > Assinando MetaMesk')
                        click(x,y)
                        time.sleep(random.uniform(15,20))

                if pyautogui.locateOnScreen('./src/UserNotLogged.png', grayscale=True, confidence=0.8 ) != None:
                        okButton = pyautogui.locateOnScreen('./src/OkErroScreen.png', grayscale=True, confidence=0.8 )
                        x,y = pyautogui.center(okButton)
                        print(' > Saindo da User is not logged in')
                        click(x,y)
                        time.sleep(random.uniform(15,20))
                        break
        
        #Vai ate a aba de Herois
        if pyautogui.locateOnScreen('./src/herobutton.png', grayscale=True, confidence=0.8 ) != None:
                herobutton = pyautogui.locateOnScreen('./src/herobutton.png', grayscale=True, confidence=0.8 )
                x,y = pyautogui.center(herobutton)
                print(' > Entrando na area de heroes')
                click(x,y)
                time.sleep(random.uniform(3,5))

                #Procura a barra de Stamina e verifica se esta com energia maxima
                if pyautogui.locateOnScreen('./src/MaxEnergy.png') != None and working == False:
                        print(' > Heroi(s) com energia maxima foi encontrado.')
                        while working == False:
                                if pyautogui.locateOnScreen('./src/WorkOFF.png') != None:
                                        work = pyautogui.locateOnScreen('./src/WorkOFF.png')
                                        x,y = pyautogui.center(work)
                                        click(x,y)
                                        time.sleep(random.uniform(0.1, 0.3))
                                else:
                                        working = True
                                        time.sleep(random.uniform(1,2))
                else:
                        print(' < Nenhum Heroi com energia maxima foi encontrado.')
                        time.sleep(random.uniform(0.1,0.3))
                        if pyautogui.locateOnScreen('./src/workOn.png') != None:
                                working = True
                                print('Heroi(s) em Work encontrado. Voltando para Teasure Hunt')
                        else:
                                working = False
                                counter = 0
                                time_duration = random.uniform(240,300) #Tempo em que a janela de heroi vai fica aberta para procurar o botão de work
                                time_start = time.time()

                                while time.time() - time_start < time_duration:
                                        print('Verificando se há Heroi(s) com energia maxima')
                                        if pyautogui.locateOnScreen('./src/MaxEnergy.png') != None:
                                                print(' > Heroi(s) com energia maxima foi encontrado.')
                                                break
                                        time.sleep(30)

                #Vai fecha o menu de Herois
                if pyautogui.locateOnScreen('./src/xButton.png', grayscale=True, confidence=0.8 ) != None:
                        xButton = pyautogui.locateOnScreen('./src/xButton.png', grayscale=True, confidence=0.8 )
                        x,y = pyautogui.center(xButton)
                        print(' > Saindo da area de Heroes')
                        click(x,y)
                        time.sleep(random.uniform(1,2))

                
        #Vai para a tela de Teasure Hunt
        if pyautogui.locateOnScreen('./src/teasurehunt.png', grayscale=True, confidence=0.8 ) != None and working == True:
                teasurehunt = pyautogui.locateOnScreen('./src/teasurehunt.png', grayscale=True, confidence=0.8 )
                x,y = pyautogui.center(teasurehunt)
                print(' > Entrando no Teasure Hunt')
                click(x,y)
                time.sleep(random.uniform(5,10))

                counter = 0
                time_duration = random.uniform(300,360) # Aguarda de 5 a 6 Minutos
                time_start = time.time()

                while time.time() <  time_start + time_duration:
                        print(' > Verificando se finalizou o mapa')
                        if pyautogui.locateOnScreen('./src/newMap.png') != None:
                                mapcount += 1
                                print(' > Mais um mapa completo. Total de mapas concluidos: ' + str(mapcount))
                                newMapbtn = pyautogui.locateOnScreen('./src/newMap.png')
                                x,y = pyautogui.center(newMapbtn)
                                click(x,y)
                                time.sleep(random.uniform(25,30))
                        time.sleep(60)

                #Apos um tempo retona para a tela principal e começa é recomeça o processo.
                xButton = pyautogui.locateOnScreen('./src/backButton.png', grayscale=True, confidence=0.8 )
                x,y = pyautogui.center(xButton)
                print(' > Saindo do Teasure Hunt')
                click(x,y)
                time.sleep(random.uniform(3,8))

print("===============================================")
        
