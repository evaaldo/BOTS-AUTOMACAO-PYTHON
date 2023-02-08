import pyautogui as bot

#click para paginas com scroll
def clickWithScroll():
    #desce até o fim da página
    bot.press('pagedown', 1000)
    bot.sleep(1)
    #avança para a próxima página
    bot.click(x=1228, y=511)

    #intervalo entre páginas
    bot.sleep(60)

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

def clickRestartLoopWithScroll():
    #intervalo para clicar nas seções do curso
    bot.sleep(5)

    #avança para as seções do curso
    bot.click(x=174, y=203)
    bot.sleep(1)

    #avança para o encontro 17
    bot.press('pagedown', 2)
    bot.sleep(1)
    bot.click(x=178, y=498)

    #intervalo para carregar o encontro 17
    bot.sleep(5)

    #clica no check-in da semana 17
    bot.press('pagedown', 1)
    bot.sleep(2)
    bot.click(x=475, y=419)

    #carregando atividades
    bot.sleep(10)

def clickStrangePage():
    #desce até o fim da página
    bot.press('pagedown', 1000)
    bot.sleep(1)
    #avança para a próxima página
    bot.click(x=945, y=540)

    #intervalo entre páginas
    bot.sleep(8)

while(True):
    bot.sleep(3)

    for i in range(10):
        clickWithScroll()

    clickStrangePage()
    clickWithScroll()
    clickStrangePage()

    for i in range(6):
        clickWithScroll()

    clickRestartLoopWithScroll()

