import pyautogui
import time
import  pandas as pd


tabela = pd.read_csv("produtos.csv")

pyautogui.PAUSE = 1.5
pyautogui.hotkey("Command", "a", interval=0.25)
pyautogui.write("safari")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

pyautogui.click(x=651, y=321)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("1234")
pyautogui.click(x=725, y=449)

for linha in tabela.index: 
    pyautogui.click(x=636, y=222)
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





