import pyautogui as pt
import time as t
def op(arg):
    if arg == "chrome":
        pt.moveTo(698, 766, duration=1)
        t.sleep(1)
        pt.click(704, 749, button="left")
        pt.moveTo(504, 457, duration=1)
        pt.click(button="left")