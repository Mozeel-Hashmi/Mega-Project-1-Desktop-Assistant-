import pyautogui as pt
import time as t
def ch():
    pt.moveTo(698, 766, duration=1)
    t.sleep(1)
    pt.click(704, 749, button="left")
    pt.moveTo(504, 457, duration=1)
    pt.click(button="left")
def ref():
    pt.FAILSAFE = False
    pt.moveTo(1365, 767, duration=2)
    pt.click(button="left")
    pt.moveTo(635, 377, duration=1)
    pt.click(button="right")
    pt.moveTo(684, 435, duration=1)
    pt.click(button="left")
op = {
    "chrome": ch,
    "refresh": ref
}