from skimage.metrics import structural_similarity
import pyautogui, time, cv2 as cv

# Variaveis
email='omega.bot@insidesistemas.com.br'
senha='0m3g4b0t@1'
xy:str

senhaAdmin = input("informe a senha do usuario Admin: ")

# Metodos
def openNavegador():
    time.sleep(1)
    pyautogui.hotkey("winleft","r")
    time.sleep(1)
    pyautogui.write("chrome", interval=0.05)
    pyautogui.press("enter")
    time.sleep(5)

    MoveMouseClick(179,48,1)
    pyautogui.write("https://autosky02.skyinone.net/admin/", interval=0.05)
    pyautogui.press("enter")
    time.sleep(5)
    MoveMouseClick(820,520,1)
    time.sleep(3)
    MoveMouseClick(448,294,1)
    MoveMouseClick(448,380,1)

def openCli(url:str):
    MoveMouseClick(179,48,1)
    pyautogui.write(url, interval=0.05)
    pyautogui.press("enter")
    time.sleep(5)

def MoveMouseClick(x:int, y:int,sleep:int):
    pyautogui.moveTo(x=x,y=y)
    pyautogui.click()
    pyautogui.sleep(sleep)

def MoveMouse(x:int, y:int, sleep:int):
    pyautogui.moveTo(x,y)
    time.sleep(sleep)

def MoveMouseScreenshot(x:int, y:int, xShot:int, yShot:int, diretorio:str):
    MoveMouse(x, y, 0.5)
    x-=15
    y+=10
    sc = pyautogui.screenshot(region=(x,y,xShot,yShot))
    sc.save(diretorio)

def AccessEnvironment():
    MoveMouseClick(1090,310,5) # Abre login do teste de abertura
    MoveMouse(623,284,1)

    pyautogui.click(clicks=3) # Clica no campo de usuario do teste
    pyautogui.write(email) # digita o e-mail do Omega Bot
    pyautogui.press('tab')
    pyautogui.write(senha) # Digita a senha do Omega Bot

    MoveMouseClick(925,436,15) # Clica para logar
    MoveMouseClick(445,404,15) # Abre o teste de abertura

def AccessService(x:int,y:int):
    
    pyautogui.doubleClick(x = x,y = y) # Abre o Service
    time.sleep(15)

    MoveMouseClick(772,431,1) # Clica no campo de Login do Service

    pyautogui.write('admin', interval=0.05)
    MoveMouseClick(833,458,1)

    pyautogui.write(senhaAdmin)
    pyautogui.hotkey('alt','O')
    time.sleep(3)
    MoveMouseClick(1029,194,1)
    MoveMouseClick(1180,81,1)

def CloseService():
    MoveMouseClick(1339,76,1)
    pyautogui.press("enter")
    pyautogui.sleep(1)
    
def CloseSession():
    MoveMouseClick(1339,112,1)
    pyautogui.press("enter")
    MoveMouseClick(473,19,1)

def TestAplication(img:str):
    i = 0
    xShot = 20
    yShot = 134
    x:int
    y:int
    scoreOld = 0

    while i <= 5:
        sc = pyautogui.screenshot(region=(xShot,yShot,75,75))
        sc.save(rf'C:\TestApplication\Teste\Aplicativos\Teste.png')

        J = cv.imread(img)
        J = cv.cvtColor(J,cv.COLOR_BGR2GRAY)

        I = cv.imread('C:\TestApplication\Teste\Aplicativos\Teste.png')
        I = cv.cvtColor(I,cv.COLOR_BGR2GRAY)

        score,diff = structural_similarity(J, I, full=True)
        score = score*100

        if(scoreOld == 0):
            scoreOld = score

        if (score >= scoreOld): 
            x = xShot + 38
            y = yShot + 26
            scoreOld = score

        if(i == 2):
            xShot += 70
        elif(i == 3):
            xShot += 75
        else:
            xShot += 78

        i += 1

    return f"{x},{y}"

def TestArchive(x:int,y:int,caminho:str):
    MoveMouseClick(x,y,1)
    pyautogui.doubleClick()
    MoveMouseClick(189,346,1)
    # MoveMouseClick(65,163,3)
    MoveMouseClick(205,348,2)
    sc = pyautogui.screenshot(region=(286,391,260,62))
    sc.save(caminho)

# Abertura do navegador
openNavegador()




# Entrada do usuario
userInput = input("Digite o cliente que sera gerado o produto para teste: ")
diretorio = 'C:\\Teste\\TestePy\\{}'.format(userInput)

userInput = input("Insira a URL de teste de aplicacoes do cliente: ")
url = userInput

userInput = input("Insira a senha do usuario Admin: ")
senhaAdmin = userInput

# Abertura do teste do cliente
openCli(url)

AccessEnvironment()

xy = TestAplication('C:\TestApplication\Produto\Aplicativos\Service.png')

splitString = xy.split(",")
x = int(splitString[0])
y = int(splitString[1])

AccessService(x,y)


MoveMouseClick(32,107,1) # Abre o Menu Cadastro
MoveMouseScreenshot(32,107,176,48,rf'{diretorio}\cadastro.png') # Menu Cadastro
MoveMouseScreenshot(99,107,390,470,rf'{diretorio}\compra.png') #Menu Compra
MoveMouseScreenshot(168,107,318,273,rf'{diretorio}\monitoramento.png') # menu Monitoramento
MoveMouseScreenshot(253,105,265,165,rf'{diretorio}\operacional.png') # Abre o menu Operacional/Vendas
MoveMouseScreenshot(381,107,285,353,rf'{diretorio}\estoque.png') # Abre o menu Estoque
MoveMouseScreenshot(449,107,220,348,rf'{diretorio}\financeiro.png') # Abre o menu Financeiro
MoveMouseScreenshot(513,107,200,124,rf'{diretorio}\relatorios.png') # Abre o menu Relatorios
MoveMouseScreenshot(572,107,160,88,rf'{diretorio}\gerencial.png') # Abre o menu Gerencial
MoveMouseScreenshot(622,107,232,283,rf'{diretorio}\suporte.png') # Abre o menu Suporte

CloseService()

xy = TestAplication('C:\TestApplication\Produto\Aplicativos\Arquivos.png')
splitString = xy.split(",")
x = int(splitString[0])
y = int(splitString[1])
TestArchive(x,y,rf'{diretorio}\arquivos.png')

CloseSession()
pyautogui.hotkey('alt','O')