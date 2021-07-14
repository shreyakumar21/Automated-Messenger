import pyautogui
import time

while True:
    time.sleep(5)
    pyautogui.typewrite('Hello!')
    time.sleep(5)
    pyautogui.press('Enter')