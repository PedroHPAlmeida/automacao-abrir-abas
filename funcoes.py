import pyautogui as py
from time import sleep

def acessarSite(url):
    py.write(url)
    py.press('enter')
    sleep(2)


def novaAbaChrome():
    py.hotkey('ctrl', 't')


def maximizarChrome():
    py.hotkey('ctrl', 'space', 'x')


def navegarAba(numeroAba):
    py.hotkey('ctrl', str(numeroAba))
