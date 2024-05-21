import pyautogui
import time

def acessar_google():
    PAUSE = 1.5

    pyautogui.alert('EXECUTANDO PROGRAMA!!!')
    time.sleep(2.0)
    pyautogui.click(x=1307, y=18)
    pyautogui.press('win')
    time.sleep(2.0)
    pyautogui.click(x=1298, y=83)
    time.sleep(2.0)
    pyautogui.write("Google", interval=0.1)
    pyautogui.press('enter')

def acessar_URL_prateleira():
    time.sleep(2.0)
    pyautogui.write("dpsp-prateleira-infinita.dpsp.io", interval=0.2)
    pyautogui.press('enter')

def acesso_VD():
    time.sleep(2.0)
    
    pyautogui.click(x=464, y=379)
    time.sleep(2.0)
   
    pyautogui.hotkey('ctrl', 'a', interval=0.2)  
    pyautogui.press('backspace') 
    time.sleep(2.0)

    pyautogui.alert('DIGITE O VD!!!')
    time.sleep(2.0)
    pyautogui.typewrite("****")
    pyautogui.press('tab')
    time.sleep(2.0)

    pyautogui.write('*****', interval=0.1)
    pyautogui.press('enter')
    time.sleep(2.0)

def validacao_CPF():
    time.sleep(2.0)
    pyautogui.alert('DIGITE SEU CPF!!!')
    pyautogui.typewrite("***********")
    time.sleep(2.0)
    pyautogui.press('enter')

def main():
    acessar_google()
    acessar_URL_prateleira()
    acesso_VD()
    validacao_CPF()

if __name__ == "__main__":
    main()
