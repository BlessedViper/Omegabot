# -*- coding:latin1 -*-
from skimage.metrics import structural_similarity
import pyautogui, time, keyring, smtplib, cv2 as cv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Variaveis
clientesAtualizados = []
arquivosInacessiveis = []
destinatario = "EMAIL"
senhaAdmin = input("informe a senha do usuario Admin: ")

# Metodos
def openNavegador():
    user = "omega.bot"
    password = keyring.get_password("CREDENTIAL", user) #Coleta a senha gravada no windows com o nome "CREDENTIAL"

    teste = False
    time.sleep(1)
    pyautogui.hotkey("winleft","r")
    time.sleep(1)
    pyautogui.write("chrome")
    pyautogui.press("enter")

    while teste == False:
        Screenshot(0,0,1364,60,rf'C:\TestApplication\Teste\Geral\navegador.png')
        result = TestImage(rf'C:\TestApplication\Teste\Geral\navegador.png',rf'C:\TestApplication\Produto\Geral\navegador.png')
        if(result == True):
            teste = result
        else:
            time.sleep(0.5)
            continue
    
    MoveMouseClick(179,48,1)
    pyautogui.write("https://autosky02.skyinone.net/admin/")
    pyautogui.press("enter")

    LoadNavegador()
    
    MoveMouseClick(642,385,0.5)
    pyautogui.write(user)
    MoveMouseClick(642,454,0.5)
    pyautogui.write(password)
    MoveMouseClick(816,516,1)

    LoadNavegador()
    MoveMouseClick(448,294,1)
    MoveMouseClick(274,352,1)

def LoadNavegador():
    teste = False
    while teste == False:
        Screenshot(70,40,36,25,rf'C:\TestApplication\Teste\Geral\loadPg.png')

        teste = TestImage('C:\TestApplication\Teste\Geral\loadPg.png','C:\TestApplication\Produto\Geral\loadPg.png')
        time.sleep(0.5)

def openCli(url:str):
    MoveMouseClick(179,48,1)
    pyautogui.write(url)
    pyautogui.press("enter")
    LoadNavegador()

def MoveMouseClick(x:int, y:int,sleep:int):
    pyautogui.moveTo(x=x,y=y)
    pyautogui.sleep(0.5)
    pyautogui.click()
    pyautogui.sleep(sleep)

def MoveMouse(x:int, y:int, sleep:int):
    pyautogui.moveTo(x,y)
    time.sleep(sleep)

def MoveMouseScreenshot(x:int, y:int, xShot:int, yShot:int, diretorio:str):
    MoveMouse(x, y, 0.8)
    x-=15
    y+=10
    sc = pyautogui.screenshot(region=(x,y,xShot,yShot))
    sc.save(diretorio)

def AccessEnvironment():
    directory="C:\TestApplication\Teste\Geral"
    productDirectory="C:\TestApplication\Produto\Geral"
    TesteLogin = False
    TesteMaqPrep = False
    email = "EMAIL"
    password = keyring.get_password("environment", email) #Coleta a senha gravada no windows com o nome "Environment"

    LoadNavegador()

    MoveMouseClick(1090,310,1) # Abre login do teste de abertura

    while TesteLogin == False:
        Screenshot(795,410,173,54,f'{directory}\Login.png')
        img = TestImage(f'{directory}\Login.png',f'{productDirectory}\Login.png')
        if (img == True):
            TesteLogin = img
        else:
            time.sleep(0.5)
            continue
    MoveMouse(623,284,1)
    pyautogui.click(clicks=3) # Clica no campo de usuario do teste
    pyautogui.write(email) # digita o e-mail do Omega Bot
    pyautogui.press('tab')
    pyautogui.write(password) # Digita a senha do Omega Bot
    
    MoveMouseClick(925,436,0) # Clica para logar

    while TesteMaqPrep == False:
        Screenshot(390,380,591,50,f'{directory}\maqPrep.png')

        result1 = TestImage(f'{directory}\maqPrep.png',f'{productDirectory}\html.png')
        result2 = TestImage(f'{directory}\maqPrep.png',f'{productDirectory}\htmlRemote.png')

        if (result1 == True):
            TesteMaqPrep = result1
        elif (result2 == True):
            TesteMaqPrep = result2
        else:
            time.sleep(0.5)
            continue

    MoveMouseClick(445,404,0) # Abre o teste de abertura

def AccessService(x:int,y:int):
    TesteLogin = False
    sleeped = 0
    # 323,182 - notificaÃ§Ã£o\n da agenda
    pyautogui.doubleClick(x = x,y = y) # Abre o Service
    
    while TesteLogin == False:
        Screenshot(685,415,208,58,'C:\TestApplication\Teste\Geral\loadService.png')

        result = TestImage('C:\TestApplication\Teste\Geral\loadService.png','C:\TestApplication\Produto\Geral\loadService.png')
        if (result == True):
            TesteLogin = result
        if(sleeped >= 3):
            VerifyTaskBar()
            sleeped = 0
        else:
            time.sleep(0.5)
            sleeped += 0.5
            continue

    MoveMouseClick(772,431,1) # Clica no campo de Login do Service

    pyautogui.write('admin')
    MoveMouseClick(833,458,1)

    pyautogui.write(senhaAdmin)
    pyautogui.hotkey('alt','O')
    time.sleep(4)
    MoveMouseClick(1029,194,0)
    MoveMouseClick(1180,81,0)

def CloseService():
    MoveMouseClick(1339,76,1)
    pyautogui.press("enter")
    pyautogui.sleep(1)
    
def CloseSession():
    MoveMouseClick(1339,112,1)
    pyautogui.press("enter")
    MoveMouseClick(473,19,1)

def TestAplication(img:str,imgEnviromentProd:str,imgEnviromentTest:str):
    i = 0
    xShot = 20
    yShot = 134
    x:int
    y:int
    scoreOld = 0
    teste = False
    sleeped = 0

    while teste == False:
        Screenshot(0,79,1363,649,imgEnviromentTest)
        result = TestImage(imgEnviromentTest,imgEnviromentProd)
        if(result == True):
            teste = result
        if(sleeped >= 3):
            VerifyTaskBar()
            sleeped = 0
        else:
            time.sleep(0.5)
            sleeped += 0.5
            continue

    while i <= 5:
        sc = pyautogui.screenshot(region=(xShot,yShot,75,75))
        sc.save(rf'C:\TestApplication\Teste\Geral\Teste.png')

        J = cv.imread(img)
        J = cv.cvtColor(J,cv.COLOR_BGR2GRAY)

        I = cv.imread('C:\TestApplication\Teste\Geral\Teste.png')
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

def TestArchive(x:int,y:int,cliente:str):
    directory = 'C:\TestApplication\Teste'
    productDirectory = 'C:\TestApplication\Produto'
    test = False

    MoveMouseClick(x,y,1)
    pyautogui.doubleClick()
        
    while test != True:
        Screenshot(1120,110,130,34,rf'{directory}\Geral\arquivosAberto.png')
        result = TestImage(rf'{directory}\Geral\arquivosAberto.png',rf'{productDirectory}\Geral\arquivosAberto.png')
        if(result == True):
            test = result
        else:
            time.sleep(0.5)
            continue
        
    Screenshot(200,275,741,23,rf'{directory}\{cliente}\arquivos.png') 
    
    result = TestImage(rf'{directory}\{cliente}\arquivos.png',rf'{productDirectory}\{cliente}\arquivos.png')
    
    if(result == False):
        arquivosInacessiveis.append(cliente)

def TestService(cliente:str):
    reloadMenu = False
    directory = 'C:\TestApplication\Teste\{}'.format(cliente)
    productDirectory = 'C:\TestApplication\Produto\{}'.format(cliente)

    MoveMouseClick(32,107,0.5) # Abre o Menu Cadastro

    reloadMenu = TestMenus(32,107,176,48,rf'{directory}\cadastro.png',rf'{productDirectory}\cadastro.png', reloadMenu, cliente) # Menu Cadastro
    reloadMenu = TestMenus(99,107,390,470,rf'{directory}\compra.png',rf'{productDirectory}\compra.png', reloadMenu, cliente) #Menu Compra
    reloadMenu = TestMenus(168,107,318,273,rf'{directory}\monitoramento.png',rf'{productDirectory}\monitoramento.png', reloadMenu, cliente) # menu Monitoramento
    reloadMenu = TestMenus(253,105,265,165,rf'{directory}\operacional.png',rf'{productDirectory}\operacional.png', reloadMenu, cliente) # Abre o menu Operacional/Vendas
    reloadMenu = TestMenus(381,107,285,353,rf'{directory}\estoque.png',rf'{productDirectory}\estoque.png', reloadMenu, cliente) # Abre o menu Estoque
    reloadMenu = TestMenus(449,107,220,348,rf'{directory}\financeiro.png',rf'{productDirectory}\financeiro.png', reloadMenu, cliente) # Abre o menu Financeiro
    reloadMenu = TestMenus(513,107,200,124,rf'{directory}\relatorios.png',rf'{productDirectory}\relatorios.png', reloadMenu, cliente) # Abre o menu Relatorios
    reloadMenu = TestMenus(572,107,160,88,rf'{directory}\gerencial.png',rf'{productDirectory}\gerencial.png', reloadMenu, cliente) # Abre o menu Gerencial
    reloadMenu = TestMenus(622,107,232,283,rf'{directory}\suporte.png',rf'{productDirectory}\suporte.png', reloadMenu, cliente) # Abre o menu Suporte        

def TestMenus(x:int, y:int,xShot:int,yShot:int,directory:str, productDirectory:str,menuAtualizado:bool, cliente:str):
    if (menuAtualizado == False):
        Screenshot(x,y,xShot,yShot,directory)

        test = TestImage(directory,productDirectory)
      
        if(test == True):
            return menuAtualizado
        else:
            MoveMouseClick(688,105,5)
            clientesAtualizados.append(cliente)
            menuAtualizado = True
    else:
        return menuAtualizado

def UpdateStructure(x:int, y:int):
    finished = False
    Screenshot(490,349,393,145,rf'C:\TestApplication\Teste\Geral\estruturas.png')

    test = TestImage('C:\TestApplication\Teste\Geral\estruturas.png','C:\TestApplication\Produto\Geral\estruturas.png')

    if(test == True):
        MoveMouseClick(744,471,0)

        while finished == False:
            finished = FinishUpdateStructure()
            time.sleep(1)
        MoveMouseClick(767,511,0)
        AccessService(x,y)

def FinishUpdateStructure():
    Screenshot(500,348,370,148,rf'C:\TestApplication\Teste\Geral\estruturas2.png')

    test = TestImage('C:\TestApplication\Teste\Geral\estruturas2.png','C:\TestApplication\Produto\Geral\estruturas2.png')

    if(test == True):
        MoveMouseClick(822,471,0)
        return True
    else:
        return False

def TestImage(test:str, product:str):
    J = cv.imread(test)
    J = cv.cvtColor(J,cv.COLOR_BGR2GRAY)

    I = cv.imread(product)
    I = cv.cvtColor(I,cv.COLOR_BGR2GRAY)

    score,diff = structural_similarity(J, I, full=True)
    score = score*100
    print(score)
    if(score >= 98):
        return True
    else:
        return False

def Screenshot(x:int, y:int, xShot:int, yShot:int, diretorio:str):
    sc = pyautogui.screenshot(region=(x,y,xShot,yShot))
    sc.save(diretorio)

def VerifyTaskBar():
    directory = rf'C:\TestApplication\Teste\Geral\taskbar.png'
    ProductDirectory = rf'C:\TestApplication\Produto\Geral\taskbar.png'
    Screenshot(485,347,404,145,directory)

    test = TestImage(directory, ProductDirectory)

    if (test == True):
        MoveMouseClick(839,470,0.5)

def Relatorio(menus:str, arquivos:str):
    email = "EMAIL"
    password = keyring.get_password("outlook", email) #Coleta a senha gravada no windows com o nome "outlook"
    host = "smtp.office365.com"
    port = 587

    server = smtplib.SMTP(host,port)
    server.connect(host,port)
    server.starttls()
    server.ehlo()
    server.login(email,password)

    html = StrToHtml(menus,arquivos)

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Relatório dos testes"
    msg['From'] = email
    msg['To'] = destinatario

    message = MIMEText(html,'html')
    msg.attach(message)

    server.sendmail(email,destinatario,msg.as_string())
    server.quit

def ListToStr(list:list):
    i = 0
    str = ''
    if (list.count == 0):
        return
    for x in list:
        if(i == 0):
            str = x
        else:
            str = f"{str}, {x}"
        i+=1
    return str

def StrToHtml(menus:str, arquivos:str):
    if (menus != '' and arquivos != ''):
        return f"""\
                <html>
                <body>
                    <p> Olá time, tudo certo? <br><br>
                        Finalizei os testes dos clientes, segue abaixo o relatório dos testes: <br><br>
                        Clientes tive que atualizar os menus:<br>
                        {menus}<br><br>
                        Clientes que não consegui acesso as pastas: <br>
                        {arquivos}<br><br>
                        att, <br>
                        Omega Bot.
                </body>
                """
    if(menus == '' and arquivos != ''):
        return f"""\
                <html>
                <body>
                    <p> Olá time, tudo certo? <br><br>
                        Finalizei os testes dos clientes, segue abaixo o relatório dos testes: <br><br>
                        Não houve necessidade de atualizar os menus de nenhum cliente.<br><br>
                        Clientes que não  consegui acesso as pastas: <br>
                        {arquivos}<br><br>
                        att, <br>
                        Omega Bot.
                </body>
                """
    if(menus != '' and arquivos == ''):
        return f"""\
                <html>
                <body>
                    <p> Olá time, tudo certo? <br><br>
                        Finalizei os testes dos clientes, segue abaixo o relatório dos testes: <br><br>
                        Clientes tive que atualizar os menus:<br>
                        {menus}<br><br>
                        Consegui acessar todas as pastas.<br>
                        att, <br>
                        Omega Bot.
                </body>
                """
    else:
        return f"""\
                <html>
                <body>
                    <p> Olá time, tudo certo? <br><br>
                        Finalizei os testes dos clientes, segue abaixo o relatório dos testes: <br><br>
                        Não houve necessidade de atualizar os menus de nenhum cliente.<br<br>
                        Consegui acessar todas as pastas.<br>
                        att, <br>
                        Omega Bot.
                </body>
                """

with open('C:\TestApplication\clientList.txt') as f:
    clientList = f.readlines()

# Abertura do navegador
openNavegador()

for x in clientList:
    xy:str

    teste = x[0:len(x)-1]

    splitString = teste.split(" ")
    cliente = splitString[0]
    url = splitString[1]

    diretorio = 'C:\TestApplication\Teste\{}'.format(cliente)
    diretorioProduto = 'C:\TestApplication\Produto\{}'.format(cliente)

    # Abertura do teste do cliente
    openCli(url)

    AccessEnvironment()

    xy = TestAplication('C:\TestApplication\Produto\Geral\Service.png', rf'{diretorioProduto}\ambiente.png', rf'{diretorio}\ambiente.png')

    splitString = xy.split(",")
    x = int(splitString[0])
    y = int(splitString[1])
    
    AccessService(x,y)

    UpdateStructure(x,y)
    
    TestService(cliente)

    CloseService()

    xy = TestAplication('C:\TestApplication\Produto\Geral\Arquivos.png', rf'{diretorioProduto}\ambiente.png', rf'{diretorio}\ambiente.png')

    splitString = xy.split(",")
    x = int(splitString[0])
    y = int(splitString[1])

    TestArchive(x,y,cliente)
    
    CloseSession()

menus = ListToStr(clientesAtualizados)
arquivos = ListToStr(arquivosInacessiveis)
Relatorio(menus, arquivos)