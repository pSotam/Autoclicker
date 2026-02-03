import pyautogui as pa
from pynput import keyboard
from pynput.keyboard import GlobalHotKeys
from time import sleep
import threading

autoOn = False
speedManager = 0.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001



def autoclick():
    while autoOn:
        pa.click()
        sleep(speedManager)
def toggle_autoclick():
    global autoOn
    autoOn = not autoOn
    print('Autoclick:', 'ON' if autoOn else 'OFF')

    if autoOn:
        threading.Thread(target=autoclick, daemon=True).start()

def negative_speed():
    global speedManager
    while speedManager < 0:
        print('Autoclick speed cant equal or be below 0')
        speedManager = 0.1
    if(speedManager > 0):
        print('Autoclick speed increased by 0.1')

def max_speed():
    global speedManager
    speedManager -= 0.1
    negative_speed()
def min_speed():
    global speedManager
    speedManager += 0.5
    print('Autoclick speed decreased by 0.5')


with GlobalHotKeys({
        '<f7>': toggle_autoclick,
        '<alt>+=': max_speed,
        '<alt>+-': min_speed
        }) as h:
    h.join()