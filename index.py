from os import error
from pyautogui import *
import pyautogui
import time
import random

bot = False

workOn = False
mapCount = 0

config = {
    # Configurações do bot.

    # Configuração: Tela Ingame (TeasureHunt)
    # Tempo maximo em minutos para retornar ao menu principal para "Salvar" o jogo.
    "returnMenuMax": 10,
    # Tempo minimo em minutos para retornar ao menu principal para "Salvar" o jogo.
    "returnMenuMin": 5,

    # Configuração: Tela de Hero (Tempo de Recuperação de Stamina)
    # A cada quantos segundos vai verificar novamente se a stamina esta full com limite de -> "timeMinToVerifyStamina~timeMaxToVerifyStamina"
    "timeToVerifyStaminaFull": 30,
    # Tempo em minutos para verificar se a stamina está cheia. e retorna ao menu principal para evitar Idle
    "timeMaxToVerifyStamina": 5,
    # Tempo em minutos para verificar se a stamina está cheia. e retorna ao menu principal para evitar Idle
    "timeMinToVerifyStamina": 4

}

# Gera o log de forma mais organizada.
timeString = "[%H:%M:%S]"
def botSay(text):
    """
    Função de log para o bot personalizada.
    """
    print(' {} - [Bombot] > {}'.format(time.strftime(timeString), text))

# Move o Mouse e clica

def click(x, y):
    """
    Função para clicar em um local específico.
    """
    pyautogui.moveTo(x, y, random.uniform(0.5, 1))
    pyautogui.mouseDown()
    time.sleep(random.uniform(0.1, 0.3))
    pyautogui.mouseUp()

# retorna o valor em segundos quando recebido em minutos.

def returnSeconds(min):
    """
    Retorna um valor em segundos a partir de um valor em minutos. Ex: 1 minuto = 60 segundos.
    """
    seconds = min*60
    return seconds

# Retorna Bom Dia ou Boa Tarde ou Boa Noite
def returnGreeting():
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

# Inicia o bot com uma mensagem de boas vindas.
botSay(returnGreeting() + ' Estou Iniciando...')
time.sleep(5)  # Espera 5 segundos para iniciar o bot.
bot = True

try:

    # Loop principal do bot
    while bot:
    ########################################################################################################################

        # Verifica se existe algum erro na tela e pressiona Ok
        if pyautogui.locateOnScreen('./src/ErrOK.png', grayscale=True, confidence=0.8) != None:
            botSay('Encontrei um erro...')
            pyautogui.hold('ctrl')
            pyautogui.press('f5')
            time.sleep(random.uniform(15, 20))

        if pyautogui.locateOnScreen('./src/Status.png', grayscale=True, confidence=0.8) != None:
            botSay("Servidor Online.")
            time.sleep(random.uniform(1, 2))
        else:
            botSay("Servidor Offline.")
            time.sleep(random.uniform(60, 120))
            pyautogui.hold('ctrl')
            pyautogui.press('f5')
            time.sleep(random.uniform(1, 3))
            break


    ########################################################################################################################

        # Apos passa na verificação de erros se conecta ao jogo.
        if pyautogui.locateOnScreen('./src/ConnectButton.png', grayscale=True, confidence=0.8) != None:
            herobutton = pyautogui.locateOnScreen('./src/ConnectButton.png', grayscale=True, confidence=0.8)
            x, y = pyautogui.center(herobutton)
            botSay('Conectando ao jogo...')
            click(x, y)
            time.sleep(random.uniform(10, 15))

            # Verifica se tem o botão da metamesk para se clica em conectar no jogo
            if pyautogui.locateOnScreen('./src/MetamasLogin.png', grayscale=True, confidence=0.8) != None:
                herobutton = pyautogui.locateOnScreen('./src/MetamasLogin.png', grayscale=True, confidence=0.8)
                x, y = pyautogui.center(herobutton)
                botSay('Assinando a metamask')
                click(x, y)
                time.sleep(random.uniform(15, 20))


            if pyautogui.locateOnScreen('./src/ErrOK.png', grayscale=True, confidence=0.8) != None:
                pyautogui.hold('ctrl')
                pyautogui.press('f5')
                botSay('Falha ao logar no jogo. Tentando novamente...')
                time.sleep(random.uniform(15, 20))
                break

    ########################################################################################################################

        # Apos logar no jogo vai ate a tela de Herois a procura de herois com stamina full
        if pyautogui.locateOnScreen('./src/heroScreen.png', grayscale=True, confidence=0.8) != None or pyautogui.locateOnScreen('./src/herobutton.png', grayscale=True, confidence=0.8) != None or pyautogui.locateOnScreen('./src/maxStamina.png', grayscale=True, confidence=0.8) != None or pyautogui.locateOnScreen('./src/workOn.png', grayscale=True, confidence=0.8) != None:
            
            if pyautogui.locateOnScreen('./src/herobutton.png', grayscale=True, confidence=0.8) != None:
                heroBtn = pyautogui.locateOnScreen('./src/herobutton.png', grayscale=True, confidence=0.8)
                x, y = pyautogui.center(heroBtn)
                botSay('Indo para o menu de herois.')
                click(x, y)
                time.sleep(random.uniform(2, 3))

            # Procurar 1 heroi com stamina full é coloca todos os herois para trabalhar
            if pyautogui.locateOnScreen('./src/maxStamina.png') != None:
                if pyautogui.locateOnScreen('./src/workOn.png') != None:
                    workOn = True
                    botSay('Encontrei heroi(s) em Work. é com stamina full.')
                else :
                    workAll = pyautogui.locateOnScreen('./src/workAll.png', confidence=0.8)
                    x, y = pyautogui.center(workAll)
                    botSay('Colocando todos os herois para trabalhar.')
                    click(x, y)
                    workOn = True
                    time.sleep(random.uniform(2, 3))
            else:
                botSay('Não tem herois com stamina full.')
                time.sleep(random.uniform(1, 2))
                if pyautogui.locateOnScreen('./src/workOn.png') != None:
                    workOn = True
                    botSay('Encontrei heroi(s) em Work.')
                else:
                    workOn = False
                    # Tempo em minutos que a janela vai fica aguardando um heroi fica full. apos isso feche e abra novamente.
                    time_duration = random.uniform(returnSeconds(config['timeMinToVerifyStamina']), returnSeconds(config['timeMaxToVerifyStamina']))
                    time_start = time.time()
                    timeSendMsg = 0

                    while time.time() - time_start < time_duration:
                        if timeSendMsg == 0 or timeSendMsg == 60:
                            botSay('Aguardando heroi ficar com Stamina full. ou algum heroi em Work.')
                            timeSendMsg = 0

                        if pyautogui.locateOnScreen('./src/workOn.png') != None:
                            botSay('Encontrei um heroi em Work.')
                            break

                        if pyautogui.locateOnScreen('./src/maxStamina.png') != None:
                            botSay('Um heroi ou mais acabou de carregar stamina.')
                            break
                        timeSendMsg += (config['timeToVerifyStaminaFull']/2)
                        time.sleep(config['timeToVerifyStaminaFull'])

            xBtn = pyautogui.locateOnScreen('./src/xBtn.png', grayscale=True, confidence=0.8)
            x, y = pyautogui.center(xBtn)
            botSay('Fechando janela de herois.')
            click(x, y)
            time.sleep(random.uniform(2, 3))

        if pyautogui.locateOnScreen('./src/inGame.png') != None and workOn == False:
            backBtn = pyautogui.locateOnScreen('./src/backButton.png', grayscale=True, confidence=0.8)
            x, y = pyautogui.center(backBtn)
            botSay('Você me iniciou no modo Teasure Hunt. \n Vou voltar para o menu principal é começar novamente.')
            click(x, y)
            time.sleep(random.uniform(2, 3))

    ########################################################################################################################

        # Vai para a TeasureHunt e aguarda o heroi trabalhar.
        if pyautogui.locateOnScreen('./src/teasureHunt.png', grayscale=True, confidence=0.8) != None and workOn == True:
            teasureHunt = pyautogui.locateOnScreen('./src/teasureHunt.png', grayscale=True, confidence=0.8)
            x, y = pyautogui.center(teasureHunt)
            botSay('Indo para a TeasureHunt.')
            click(x, y)
            time.sleep(random.uniform(5, 10))

            # Aguarda os Herois trabalharem por 5~10 minutos.
            time_duration = random.uniform(returnSeconds(config['returnMenuMin']), returnSeconds(config['returnMenuMax']))
            time_start = time.time()
            sendmsg = 0

            while time.time() - time_start < time_duration:
                if sendmsg == 60 or sendmsg == 0: 
                    botSay('Aguardando herois trabalharem ou um mapa ser concluido.')
                    sendmsg = 0

                if pyautogui.locateOnScreen('./src/newMap.png') != None:
                    mapCount += 1
                    botSay('Mapa Completo! Aguardando nova TeasureHunt. Total de Mapas concluidos: ' + str(mapCount))
                    time.sleep(random.uniform(12, 15))
                    break
                sendmsg += 5
                time.sleep(5)

            # Volta para o menu principal para "salvar" o progresso.
            backBtn = pyautogui.locateOnScreen('./src/backButton.png', grayscale=True, confidence=0.8)
            x, y = pyautogui.center(backBtn)
            botSay('Voltando para o menu principal.')
            click(x, y)
            time.sleep(random.uniform(2, 3))

        print('{:=^50}'.format(time.strftime(' [%H:%M:%S] ')))
        print('{:=^50}'.format(' Total de mapas concluidos: {} '.format(str(mapCount))))
        print('='*50)

except Exception as erro:
    print("Isso não deveria acontecer... mas aconteceu!: " + erro)
    time.sleep(10)