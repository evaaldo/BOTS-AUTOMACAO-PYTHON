import pyautogui as bot

#click para paginas com scroll
def clickWithScroll():
    #desce até o fim da página
    bot.press('pagedown', 1000)
    bot.sleep(1)
    #avança para a próxima página
    bot.click(x=1228, y=511)

    #intervalo entre páginas
    bot.sleep(10)

#click para páginas sem scroll
def clickWithoutScroll():
    #avança para a próxima página
    bot.click(x=1275, y=525)

    #intervalo entre páginas
    bot.sleep(10)

#click para reiniciar o loop
def clickRestartLoop():
    #intervalo para clicar nas seções do curso
    bot.sleep(5)

    #avança para as seções do curso
    bot.click(x=174, y=203)
    bot.sleep(1)

    #avança para o encontro 11
    bot.press('pagedown', 1)
    bot.sleep(1)
    bot.click(x=174, y=542)

    #intervalo para carregar o encontro 11
    bot.sleep(5)

    #desce a página
    bot.press('pagedown', 1)
    bot.sleep(1)

    #clica na semana 11
    bot.click(x=616, y=400)

    #carregando atividades
    bot.sleep(5)

def clickRestartLoopWithoutScroll():
    #intervalo para clicar nas seções do curso
    bot.sleep(5)

    #avança para as seções do curso
    bot.click(x=174, y=203)
    bot.sleep(1)

    #avança para o encontro 15
    bot.press('pagedown', 2)
    bot.sleep(1)
    bot.click(x=164, y=303)

    #intervalo para carregar o encontro 15
    bot.sleep(5)

    #clica na semana 14
    bot.press('pagedown', 1)
    bot.sleep(2)
    bot.click(x=485, y=412)

    #carregando atividades
    bot.sleep(5)

def clickStrangePage():
    #desce até o fim da página
    bot.press('pagedown', 1000)
    bot.sleep(1)
    #avança para a próxima página
    bot.click(x=1236, y=544)

    #intervalo entre páginas
    bot.sleep(120)

while(True):
    bot.sleep(3)

    for i in range(25):
        clickWithScroll()

    clickRestartLoopWithoutScroll()

