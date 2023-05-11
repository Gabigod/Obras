import pyautogui as pg
import time

import pyperclip

pg.alert('Cuidado, Não mexer no computador') ## Aviso para o usuário
pg.PAUSE = 0.4       ## Tempo de espera entre comandos

pg.press('winleft')  ## Abrindo o sistema
pg.write('obras')
pg.press('enter')
time.sleep(5)

pg.press('left')  ## Efetuando o login
pg.press('enter')
time.sleep(15)
pg.write('Login')           ## Alterar login
pg.press('tab')
pg.write('senha')           ## Alterar a senha
pg.press('enter')
time.sleep(5)

pg.moveTo(629, 390) ## Atualizando o sistema
time.sleep(10)
pg.mouseDown()
pg.mouseUp()
pg.moveTo(1351, 804)
pg.mouseDown()
pg.mouseUp()
pg.alert('Acaabou') ## Aviso do fim da execução do programa
