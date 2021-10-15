import pyautogui as py
from time import sleep

#Abrir Chrome
py.press('winleft')
py.write('Google Chrome')
sleep(0.5)
py.press('enter')
sleep(5)

#Abrir Gmail
acessarSite('https://accounts.google.com/b/0/AddMailService')

#Abrir Linkedin em uma nova aba
novaAbaChrome()
acessarSite('https://www.linkedin.com/')

#Abrir video do no Youtube de ondas bineurais para estudar
novaAbaChrome()
acessarSite('https://youtu.be/-AfuOtlMcII')
sleep(3)

#Voltar para a aba do Gmail e maximar janela
navegarAba(1)
maximizarChrome()
