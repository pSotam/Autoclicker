import ctypes
import threading
import sys
from pynput.keyboard import GlobalHotKeys

autoOn = False

# ===== WIN32 STRUCTS =====
PUL = ctypes.POINTER(ctypes.c_ulong)

class MouseInput(ctypes.Structure):
    _fields_ = [
        ("dx", ctypes.c_long),
        ("dy", ctypes.c_long),
        ("mouseData", ctypes.c_ulong),
        ("dwFlags", ctypes.c_ulong),
        ("time", ctypes.c_ulong),
        ("dwExtraInfo", PUL)
    ]

class Input_I(ctypes.Union):
    _fields_ = [("mi", MouseInput)]

class Input(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_ulong),
        ("ii", Input_I)
    ]

# ===== CONSTANTS =====
INPUT_MOUSE = 0
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP   = 0x0004

SendInput = ctypes.windll.user32.SendInput

# ===== CLICK MAIS RÁPIDO POSSÍVEL =====
def click():
    extra = ctypes.c_ulong(0)
    down = Input(
        type=INPUT_MOUSE,
        ii=Input_I(
            mi=MouseInput(0, 0, 0, MOUSEEVENTF_LEFTDOWN, 0, ctypes.pointer(extra))
        )
    )
    up = Input(
        type=INPUT_MOUSE,
        ii=Input_I(
            mi=MouseInput(0, 0, 0, MOUSEEVENTF_LEFTUP, 0, ctypes.pointer(extra))
        )
    )
    SendInput(2, ctypes.byref((Input * 2)(down, up)), ctypes.sizeof(Input))

def autoclick():
    while autoOn:
        click()

def toggle():
    global autoOn
    autoOn = not autoOn
    print('AUTOCLICK:', 'ON' if autoOn else 'OFF')

    if autoOn:
        threading.Thread(target=autoclick, daemon=True).start()

def sair():
    print('SAINDO')
    sys.exit()

with GlobalHotKeys({
        '<f7>': toggle,
        '<esc>': sair
    }) as h:
    h.join()
