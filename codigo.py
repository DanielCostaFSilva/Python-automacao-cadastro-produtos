import pyautogui
import time
import  pandas as pd


# LER O ARQUIVO CSV
tabela = pd.read_csv("produtos.csv")

# DAR UMA PAUSA DE 1 SEGUNDA DE UMA INSTRUÇAO PYOUTOGUI PARA A OUTRA
pyautogui.PAUSE = 1
# HOTKEY USADO PRA CRIAR TECLA DE ATALHOS
# ABRE LAUNCHPAD DO MAC EM CASO DE WINDOWS USARIA A TECLA WIN
pyautogui.hotkey("Command", "a", interval=0.25)
# DIGITANDO O APLICATIVO QUE VAI ABRIR NESSE CASO O SAFARI
pyautogui.write("safari")
pyautogui.press("enter")
# DIGITANDO O ENDEREÇO PARA QUAL IR
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)
# USA O CLICK COM AS CORDENADAS DO PRIMEIRO INPUT 
# PARA PEGAR A CORDENADA DO INPUT RODAR O ARQUIVO AUXILIAR E DEIXAR O MOUSE PARADO NA POSIÇAO DESEJADA
pyautogui.click(x=651, y=321)
# DEPOIS DE TER PEGO A POSIÇÃO DO INPUT, AGORA FAZ O LOGIN
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("1234")

# POSIÇÃO DO BOTAO DE LOGAR
pyautogui.click(x=725, y=449)

# PERCORRER TODO ARQUIVO CSV
for linha in tabela.index: 
    # BUSCAR POSIÇÃO DO PRIMEIRO INPUT
    pyautogui.click(x=636, y=222)

    # INSERIR OS PRODUTOS ATE O FIM DO ARQUIVO
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    if not pd.isna(tabela.loc[linha, "obs"]):
         pyautogui.write(str(tabela.loc[linha, "obs"]))

    pyautogui.click(x=642, y=743)

    pyautogui.scroll(500)





