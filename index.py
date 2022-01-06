from pyautogui import *
import pyautogui
import time
import random

workOn = False
mapCount = 0

def click(x,y):
    """
    Função para clicar em um local específico.
    """
    pyautogui.moveTo(x,y, random.uniform(0.5,1))
    pyautogui.mouseDown()
    time.sleep(random.uniform(0.1,0.3))
    pyautogui.mouseUp()

#retorna o valor em segundos quando recebido em minutos.
def returnSeconds(min):
    """
    Retorna um valor em segundos a partir de um valor em minutos. Ex: 1 minuto = 60 segundos.
    """
    seconds = min*60
    return seconds


#verifica o status do servidor
def checkServerStatus():
    """
    Verifica o status do servidor. Se estiver online, retorna True.
    """
    if pyautogui.locateOnScreen('./src/statusMaintenace.png', confidence=0.9) != None or pyautogui.locateOnScreen('./src/statusOffline.png', confidence=0.9) != None:
        while True:
            print(time.strftime(" %H:%M:%S") + ' - [Bombot] > Verificando o status do servidor...')
            if pyautogui.locateOnScreen('./src/statusOnline.png') != None:
                print(time.strftime(" %H:%M:%S") + ' - [Bombot] > Servidor voltou ao normal.')
                return True
            else:
                if pyautogui.locateOnScreen('./src/statusMaintenace.png', confidence=0.9) != None:
                    print(time.strftime(" %H:%M:%S") + ' - [Bombot] > Servidor em manutenção.')
                elif pyautogui.locateOnScreen('./src/statusOnline.png', confidence=0.9) != None:
                    print(time.strftime(" %H:%M:%S") + ' - [Bombot] > Servidor offline.')
                time.sleep(returnSeconds(2)) #Verifica a cada 2 minutos.

    elif pyautogui.locateOnScreen('./src/statusOnline.png', confidence=0.9) != None:
        print(time.strftime(" %H:%M:%S") + ' - [Bombot] > Servidor online.')
        return True

while checkServerStatus():

    #Verifica se existe algum erro na tela e pressiona Ok
    errList = {
        'SocketError': 'SocketError',
        'idle': 'idle',
        'wrongVersion': 'wrongVersion', #Lembra de fazer um atualização na função para desativar o bot
        'unstable': 'unstable', #Lembra de fazer um atualização na função para desativar o bot
    }
    for err in errList:
        if pyautogui.locateOnScreen('./src/' + err + '.png', grayscale=True, confidence=0.8 ) != None:
            OkBtn = pyautogui.locateOnScreen('./src/ErrOK.png', grayscale=True, confidence=0.8 )
            x,y = pyautogui.center(OkBtn)
            click(x,y)
            time.sleep(random.uniform(10,15))

    #Apos passa na verificação de erros se conecta ao jogo.
    if pyautogui.locateOnScreen('./src/ConnectButton.png', grayscale=True, confidence=0.8 ) != None:
        herobutton = pyautogui.locateOnScreen('./src/ConnectButton.png', grayscale=True, confidence=0.8 )
        x,y = pyautogui.center(herobutton)
        print(time.strftime(" %H:%M:%S") + ' - [Bombot] > Fazendo login no jogo.')
        click(x,y)
        time.sleep(random.uniform(10,15))
        #Verifica se tem o botão da metamesk para se clica em conectar no jogo
        if pyautogui.locateOnScreen('./src/MetamasLogin.png', grayscale=True, confidence=0.8 ) != None:
            herobutton = pyautogui.locateOnScreen('./src/MetamasLogin.png', grayscale=True, confidence=0.8 )
            x,y = pyautogui.center(herobutton)
            print(time.strftime(" %H:%M:%S") + ' - [Bombot] > Assinando MetaMesk')
            click(x,y)
            time.sleep(random.uniform(15,20))
        if pyautogui.locateOnScreen('./src/UserNotLogged.png', grayscale=True, confidence=0.8 ) != None:
            okButton = pyautogui.locateOnScreen('./src/ErrOK.png', grayscale=True, confidence=0.8 )
            x,y = pyautogui.center(okButton)
            print(time.strftime(" %H:%M:%S") + ' - [Bombot] > Falha ao logar no jogo. Tentando novamente.')
            click(x,y)
            time.sleep(random.uniform(15,20))
            break

    #Apos logar no jogo vai ate a tela de Herois a procura de herois com stamina full
    if pyautogui.locateOnScreen('./src/herobutton.png', grayscale=True, confidence=0.8) != None or pyautogui.locateOnScreen('./src/workOn.png') != None or pyautogui.locateOnScreen('./src/maxStamina.png') != None or pyautogui.locateOnScreen('./src/HeroScreen.png') != None:

        if pyautogui.locateOnScreen('./src/herobutton.png', grayscale=True, confidence=0.8) != None:
            heroBtn = pyautogui.locateOnScreen('./src/herobutton.png', grayscale=True, confidence=0.8 )
            x,y = pyautogui.center(heroBtn)
            print(time.strftime(" %H:%M:%S") + ' - [Bombot] > Indo para o menu de herois.')
            click(x,y)
            time.sleep(random.uniform(2,3))

        #Procurar 1 heroi com stamina full é coloca todos os herois para trabalhar
        if pyautogui.locateOnScreen('./src/maxStamina.png') != None:
            workAll = pyautogui.locateOnScreen('./src/workAll.png', grayscale=True, confidence=0.8)
            x,y = pyautogui.center(workAll)
            print(time.strftime(" %H:%M:%S") + ' - [Bombot] > Heroi(s) com stamina full. Colocando todos os herois para trabalhar.')
            click(x,y)
            workOn = True
            time.sleep(random.uniform(2,3))
        else:
            print(time.strftime(" %H:%M:%S") + ' - [Bombot] > Não tem heroi com stamina full.')
            time.sleep(random.uniform(1,2))
            if pyautogui.locateOnScreen('./src/workOn.png') != None:
                workOn = True
                print(time.strftime(" %H:%M:%S") + ' - [Bombot] > Encontrei heroi(s) em Work.')
            else:
                workOn = False
                time_duration = random.uniform(returnSeconds(4),returnSeconds(5)) #Tempo em minutos que a janela vai fica aguardando um heroi fica full. apos isso feche e abra novamente.
                time_start = time.time()

                while time.time() - time_start < time_duration:
                    print(time.strftime(" %H:%M:%S") + ' - [Bombot] > Aguardando heroi ficar com Stamina full. ou algum heroi em Work.')

                    if pyautogui.locateOnScreen('./src/workOn.png') != None:
                        print(time.strftime(" %H:%M:%S") + ' - [Bombot] > Encontrei um heroi em Work.')
                        break
                    
                    if pyautogui.locateOnScreen('./src/maxStamina.png') != None:
                        print(time.strftime(" %H:%M:%S") + ' - [Bombot] > Um heroi ou mais acabou de carregar stamina.')
                        break
                    time.sleep(30)
            
        xBtn = pyautogui.locateOnScreen('./src/xBtn.png', grayscale=True, confidence=0.8)
        x,y = pyautogui.center(xBtn)
        print(time.strftime(" %H:%M:%S") + ' - [Bombot] > Fechando janela de herois.')
        click(x,y)
        time.sleep(random.uniform(2,3))

    if pyautogui.locateOnScreen('./src/inGame.png') != None and workOn == False:
        backBtn = pyautogui.locateOnScreen('./src/backButton.png', grayscale=True, confidence=0.8)
        x,y = pyautogui.center(backBtn)
        print(time.strftime(" %H:%M:%S") + ' - [Bombot] > Você me iniciou no modo Teasure Hunt. \n Vou voltar para o menu principal é começar novamente.')
        click(x,y)
        time.sleep(random.uniform(2,3))

    #Vai para a TeasureHunt e aguarda o heroi trabalhar.
    if pyautogui.locateOnScreen('./src/teasureHunt.png', grayscale=True, confidence=0.8) != None and workOn == True:
        teasureHunt = pyautogui.locateOnScreen('./src/teasureHunt.png', grayscale=True, confidence=0.8)
        x,y = pyautogui.center(teasureHunt)
        print(time.strftime(" %H:%M:%S") + ' - [Bombot] > Indo para a TeasureHunt.')
        click(x,y)
        time.sleep(random.uniform(5,10))

        #Aguarda os Herois trabalharem por 5~10 minutos.
        time_duration = random.uniform(returnSeconds(5),returnSeconds(10))
        time_start = time.time()

        while time.time() - time_start < time_duration:
            print(time.strftime(" %H:%M:%S") + ' - [Bombot] > Aguardando Herois Trabalhar.')
            if pyautogui.locateOnScreen('./src/newMap.png') != None:
                print(time.strftime(" %H:%M:%S") + ' - [Bombot] > Mapa Completo! Aguardando nova TeasureHunt. Total de Mapas Completos: ' + str(mapCount))
                mapCount += 1
                time.sleep(random.uniform(12,15))
            time.sleep(60)
        
        #Volta para o menu principal para "salvar" o progresso.
        backBtn = pyautogui.locateOnScreen('./src/backButton.png', grayscale=True, confidence=0.8)
        x,y = pyautogui.center(backBtn)
        print(time.strftime(" %H:%M:%S") + ' - [Bombot] > Voltando para o menu principal.')
        click(x,y)
        time.sleep(random.uniform(2,3))

    print("========================== "+time.strftime(" %H:%M:%S")+" ==========================")
    print('             Total de Mapas Concluidos: ' + str(mapCount))
    print('===============================================================')
