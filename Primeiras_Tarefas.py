import pyautogui as py
from time import sleep
import funcoes as func

#Abrir Chrome
py.press('winleft')
py.write('Google Chrome')
sleep(0.5)
py.press('enter')
sleep(5)

#Abrir Gmail
func.acessarSite('https://accounts.google.com/b/0/AddMailService')

#Abrir Linkedin em uma nova aba
func.novaAbaChrome()
func.acessarSite('https://www.linkedin.com/')

#Abrir video do no Youtube de ondas bineurais para estudar
func.novaAbaChrome()
func.acessarSite('https://youtu.be/-AfuOtlMcII')
sleep(3)

#Voltar para a aba do Gmail e maximar janela
func.navegarAba(1)
func.maximizarChrome()
