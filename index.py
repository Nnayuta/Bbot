from pyautogui import *
import pyautogui
import time
import random

workOn = False
mapCount = 0

timeString = " [%H:%M:%S]"
def botSay(text):
    """
    Função de log para o bot personalizada.
    """
    print(time.strftime(timeString) + ' - [Bombot] > ' + text)

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
            botSay('Verificando o status do servidor...')
            if pyautogui.locateOnScreen('./src/statusOnline.png') != None:
                botSay('Servidor online!')
                return True
            else:
                if pyautogui.locateOnScreen('./src/statusMaintenace.png', confidence=0.9) != None:
                    botSay('Servidor em manutenção!')
                elif pyautogui.locateOnScreen('./src/statusOnline.png', confidence=0.9) != None:
                    botSay('Servidor offline!')
                time.sleep(returnSeconds(2)) #Verifica a cada 2 minutos.

    elif pyautogui.locateOnScreen('./src/statusOnline.png', confidence=0.9) != None:
        botSay('Servidor online!')
        return True
    else:
        botSay('Não consigo ver o jogo. Ele precisa esta em primeiro plano.')
        time.sleep(10)


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
        botSay('Conectando ao jogo...')
        click(x,y)
        time.sleep(random.uniform(10,15))
        #Verifica se tem o botão da metamesk para se clica em conectar no jogo
        if pyautogui.locateOnScreen('./src/MetamasLogin.png', grayscale=True, confidence=0.8 ) != None:
            herobutton = pyautogui.locateOnScreen('./src/MetamasLogin.png', grayscale=True, confidence=0.8 )
            x,y = pyautogui.center(herobutton)
            botSay('Assinando a metamask')
            click(x,y)
            time.sleep(random.uniform(15,20))
        if pyautogui.locateOnScreen('./src/UserNotLogged.png', grayscale=True, confidence=0.8 ) != None:
            okButton = pyautogui.locateOnScreen('./src/ErrOK.png', grayscale=True, confidence=0.8 )
            x,y = pyautogui.center(okButton)
            botSay('Falha ao logar no jogo. Tentando novamente...')
            click(x,y)
            time.sleep(random.uniform(15,20))
            break

    #Apos logar no jogo vai ate a tela de Herois a procura de herois com stamina full
    if pyautogui.locateOnScreen('./src/herobutton.png', grayscale=True, confidence=0.8) != None or pyautogui.locateOnScreen('./src/workOn.png') != None or pyautogui.locateOnScreen('./src/maxStamina.png') != None or pyautogui.locateOnScreen('./src/HeroScreen.png') != None:

        if pyautogui.locateOnScreen('./src/herobutton.png', grayscale=True, confidence=0.8) != None:
            heroBtn = pyautogui.locateOnScreen('./src/herobutton.png', grayscale=True, confidence=0.8 )
            x,y = pyautogui.center(heroBtn)
            botSay('Indo para o menu de herois.')
            click(x,y)
            time.sleep(random.uniform(2,3))

        #Procurar 1 heroi com stamina full é coloca todos os herois para trabalhar
        if pyautogui.locateOnScreen('./src/maxStamina.png') != None:
            workAll = pyautogui.locateOnScreen('./src/workAll.png', grayscale=True, confidence=0.8)
            x,y = pyautogui.center(workAll)
            botSay('Colocando todos os herois para trabalhar.')
            click(x,y)
            workOn = True
            time.sleep(random.uniform(2,3))
        else:
            botSay('Não tem herois com stamina full.')
            time.sleep(random.uniform(1,2))
            if pyautogui.locateOnScreen('./src/workOn.png') != None:
                workOn = True
                botSay('Encontrei heroi(s) em Work.')
            else:
                workOn = False
                time_duration = random.uniform(returnSeconds(4),returnSeconds(5)) #Tempo em minutos que a janela vai fica aguardando um heroi fica full. apos isso feche e abra novamente.
                time_start = time.time()

                while time.time() - time_start < time_duration:
                    botSay('Aguardando heroi ficar com Stamina full. ou algum heroi em Work.')

                    if pyautogui.locateOnScreen('./src/workOn.png') != None:
                        botSay('Encontrei um heroi em Work.')
                        break
                    
                    if pyautogui.locateOnScreen('./src/maxStamina.png') != None:
                        botSay('Um heroi ou mais acabou de carregar stamina.')
                        break
                    time.sleep(30)
            
        xBtn = pyautogui.locateOnScreen('./src/xBtn.png', grayscale=True, confidence=0.8)
        x,y = pyautogui.center(xBtn)
        botSay('Fechando janela de herois.')
        click(x,y)
        time.sleep(random.uniform(2,3))

    if pyautogui.locateOnScreen('./src/inGame.png') != None and workOn == False:
        backBtn = pyautogui.locateOnScreen('./src/backButton.png', grayscale=True, confidence=0.8)
        x,y = pyautogui.center(backBtn)
        botSay('Você me iniciou no modo Teasure Hunt. \n Vou voltar para o menu principal é começar novamente.')
        click(x,y)
        time.sleep(random.uniform(2,3))

    #Vai para a TeasureHunt e aguarda o heroi trabalhar.
    if pyautogui.locateOnScreen('./src/teasureHunt.png', grayscale=True, confidence=0.8) != None and workOn == True:
        teasureHunt = pyautogui.locateOnScreen('./src/teasureHunt.png', grayscale=True, confidence=0.8)
        x,y = pyautogui.center(teasureHunt)
        botSay('Indo para a TeasureHunt.')
        click(x,y)
        time.sleep(random.uniform(5,10))

        #Aguarda os Herois trabalharem por 5~10 minutos.
        time_duration = random.uniform(returnSeconds(5),returnSeconds(10))
        time_start = time.time()

        while time.time() - time_start < time_duration:
            botSay('Aguardando Herois Trabalhar.')
            if pyautogui.locateOnScreen('./src/newMap.png') != None:
                botSay('Mapa Completo! Aguardando nova TeasureHunt. Total de Mapas Completos: ' + str(mapCount))
                mapCount += 1
                time.sleep(random.uniform(12,15))
            time.sleep(60)
        
        #Volta para o menu principal para "salvar" o progresso.
        backBtn = pyautogui.locateOnScreen('./src/backButton.png', grayscale=True, confidence=0.8)
        x,y = pyautogui.center(backBtn)
        botSay('Voltando para o menu principal.')
        click(x,y)
        time.sleep(random.uniform(2,3))

    print("========================== "+time.strftime(timeString)+" ==========================")
    print('             Total de Mapas Concluidos: ' + str(mapCount))
    print('===============================================================')
    