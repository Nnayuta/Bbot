from pyautogui import *
import pyautogui
import time
import random

workStatus = False
mapCount = 0

def botSay(text):
    """
    Função de log para o bot.
    """
    timeString = "[%H:%M:%S]"
    print(' {} - [Bombot 2.0] > {}'.format(time.strftime(timeString), text))

#Função pra fazer o bot clicar com pyautogui com delay de alguns segundos
def botClick(x, y):
    """
    Função de bot para clicar com delay.
    """
    pyautogui.moveTo(x, y, random.uniform(0.5, 1))
    pyautogui.mouseDown()
    time.sleep(random.uniform(0.1, 0.3))
    pyautogui.mouseUp()

#Função que retorna o valor em segundos recebendo em minutos
def minToSec(min):
    """
    Função para converter minutos para segundos.
    """
    return min * 60

#Função que pega a hora atual e retorna uma Saudações
def getGreeting():
    """
    Retorna Bom Dia ou Boa Tarde ou Boa Noite
    """
    hour = int(time.strftime("%H"))
    if hour >= 0 and hour < 12:
        return 'Bom dia!'
    elif hour >= 12 and hour < 18:
        return 'Boa tarde!'
    else:
        return 'Boa noite!'

botSay(getGreeting() + ", Estou Iniciando...")
time.sleep(2)
while True:

    try:
        connectButton = pyautogui.locateOnScreen('src/ConnectButton.png')
        if connectButton:
            x, y = pyautogui.center(connectButton)
            botClick(x, y)
            botSay("Se conectando ao jogo...")

            time.sleep(random.uniform(10, 15))
        
            metamaskLogin = pyautogui.locateOnScreen('src/MetamasLogin.png')
            if metamaskLogin:
                #Assina a metamask para autorizar o login
                x, y = pyautogui.center(metamaskLogin)
                botClick(x, y)
                botSay("Logando no Metamask...")
                time.sleep(random.uniform(10, 15))

            ErrOK = pyautogui.locateOnScreen('src/ErrOK.png')
            if ErrOK:
                #Reincia o cache do navegador é começa novamente o loop
                pyautogui.hold('ctrl')
                pyautogui.press('f5')
                botSay("Erro na conexão, reiniciando o jogo...")
                time.sleep(random.uniform(10, 15))
                continue
    except:
        pass

    #Menu Principal, Tenta procurar o botão de seleção de Heroi ou stamina maxima ou work on
    try:
        #Verifica se tem algum Error na tela
        ErrOK = pyautogui.locateOnScreen('src/ErrOK.png')
        if ErrOK:
            #Reincia o cache do navegador é começa novamente o loop
            pyautogui.hold('ctrl')
            pyautogui.press('f5')
            botSay("Erro na conexão, reiniciando o jogo...")
            time.sleep(random.uniform(15, 20))
            continue

        try:
            herobutton = pyautogui.locateOnScreen('src/herobutton.png')
            if herobutton and workStatus == False:
                #Tela de seleção de heroi
                x, y = pyautogui.center(herobutton)
                botClick(x, y)
                botSay("Abrindo tela de seleção de Herois...")
                time.sleep(random.uniform(2, 3))    
        except:
            pass

        try:
            heroScreen = pyautogui.locateOnScreen('src/heroScreen.png')
            if heroScreen and workStatus == False:
                try:
                    maxStamina = pyautogui.locateOnScreen('src/maxStamina.png')
                    workOn = pyautogui.locateOnScreen('src/workOn.png')
                    if maxStamina == None and workOn == None:

                        time_duration = minToSec(random.randint(5, 10))
                        time_start = time.time()
                        sendMsg = 0

                        while time.time() - time_start < time_duration:
                            #Verifica Erros na tela
                            ErrOK = pyautogui.locateOnScreen('src/ErrOK.png')
                            if ErrOK:
                                #Reincia o cache do navegador é começa novamente o loop
                                pyautogui.hold('ctrl')
                                pyautogui.press('f5')
                                botSay("Erro na conexão, reiniciando o jogo...")
                                time.sleep(random.uniform(15, 20))
                                break

                            #Verifica se o tem algum Heroi com Stamina Maxima
                            maxStamina = pyautogui.locateOnScreen('src/maxStamina.png')
                            if maxStamina:
                                botSay("Heroi(s) com Stamina Maxima")
                                break

                            workOn = pyautogui.locateOnScreen('src/workOn.png')
                            if workOn:
                                botSay("Heroi(s) com Work On")
                                break

                            if sendMsg == 0 or sendMsg == 60:
                                botSay("Aguardando heroi(s) ficar full...")
                                sendMsg = 0
                            sendMsg += 5
                            time.sleep(5)
                        
                        xBtn = pyautogui.locateOnScreen('src/xBtn.png')
                        if xBtn:
                            x, y = pyautogui.center(xBtn)
                            botClick(x, y)
                            botSay("Fechando tela de seleção de Herois...")
                            time.sleep(random.uniform(2, 3))
                except:
                    pass
        except:
            pass

        try:
            maxStamina = pyautogui.locateOnScreen('src/maxStamina.png')
            if maxStamina and workStatus == False:
                botSay("Heroi(s) com Stamina Maxima encontrado(s)!")
                try:
                    #Tenta procura o botão de WorkAll é clica
                    workAll = pyautogui.locateOnScreen('src/workAll.png')
                    if workAll:
                        x, y = pyautogui.center(workAll)
                        botClick(x, y)
                        botSay("Work All...")
                        time.sleep(random.uniform(2, 3))
                except:
                    pass
        except:
            pass

        try:
            workOn = pyautogui.locateOnScreen('src/workOn.png')
            if workOn and workStatus == False:
                botSay("Encontrei Heroi em Work...")
                #Personagem em Work contrado indo para TeasureHunt
                try:
                    #Tenta encontra o "xBtn" para fechar o menu de Work
                    xBtn = pyautogui.locateOnScreen('src/xBtn.png')
                    if xBtn:
                        x, y = pyautogui.center(xBtn)
                        botClick(x, y)
                        botSay("Fechando o menu para ir para o TeasureHunt...")
                        time.sleep(random.uniform(2, 3))
                        workStatus = True
                except:
                    pass
        except:
            pass

        try:
            inGame = pyautogui.locateOnScreen('src/backButton.png')
            if inGame and workStatus == False:
                #Volta pro menu principal procurando o botão de voltar "backButton".
                backButton = pyautogui.locateOnScreen('src/backButton.png')
                if backButton:
                    x, y = pyautogui.center(backButton)
                    botClick(x, y)
                    botSay("Voltando para o menu principal para verificar os herois...")
                    time.sleep(random.uniform(2, 3))
        except:
            pass

        #Tenta encontrar o botão de TreasureHunt
        try:
            treasureHunt = pyautogui.locateOnScreen('src/teasureHunt.png')
            if treasureHunt and workStatus == True:
                #Tenta encontra o botão de TreasureHunt
                x, y = pyautogui.center(treasureHunt)
                botClick(x, y)
                botSay("Indo para TreasureHunt...")
                time.sleep(random.uniform(5, 10))

                time_duration = minToSec(random.randint(5, 8))
                time_start = time.time()
                sendMsg = 0
                while time.time() - time_start < time_duration:
                    #Verifica a todo momento se apareceu algum erro na tela

                    try:
                        ErrOK = pyautogui.locateOnScreen('src/ErrOK.png')
                        if ErrOK:
                            #Reincia o cache do navegador é começa novamente o loop
                            pyautogui.hold('ctrl')
                            pyautogui.press('f5')
                            botSay("Erro na conexão, reiniciando o jogo...")
                            time.sleep(random.uniform(15, 20))
                            break
                    except:
                        pass
                    try:
                        if sendMsg == 60 or sendMsg == 0:
                            botSay("TeasureHunt em andamento...")
                            sendMsg = 0 
                    except:
                        pass
                    try:
                        newMap = pyautogui.locateOnScreen('src/newMap.png')
                        if newMap:
                            mapCount += 1
                            botSay("Mapa finalizado... aguardando o proximo mapa...")
                            time.sleep(random.uniform(12, 15))
                            break
                    except:
                        pass
                    sendMsg += 5
                    time.sleep(5)

                try:
                    #Volta pro menu principal para "salvar progresso"
                    backButton = pyautogui.locateOnScreen('src/backButton.png')
                    if backButton:
                        x, y = pyautogui.center(backButton)
                        botClick(x, y)
                        botSay("Voltando para o menu principal para salvar progresso...")
                        workStatus = False
                        time.sleep(random.uniform(2, 3))
                except:
                    pass

        except:
            pass

    except:
        pass
    
    print('{:=^50}'.format(time.strftime(' [%H:%M:%S] ')))
    print('{:=^50}'.format(' Total de mapas concluidos: {} '.format(str(mapCount))))
    print('='*50)