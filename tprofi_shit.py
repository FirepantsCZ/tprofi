import pyautogui
import keyboard
import time
import random
import string

screenWidth, screenHeight = pyautogui.size()

while True:
    
    pyautogui.click(720, 620)
    em_name = ''.join(random.choices(string.ascii_letters + string.digits, k = 10))
    em_domain = ''.join(random.choices(string.ascii_letters + string.digits, k = 5))
    keyboard.write(f"{em_name}@{em_domain}.cz")
    time.sleep(0.5)
    pyautogui.click(720, 650)
    for _ in range(2):
        keyboard.press_and_release("page_down")
    time.sleep(0.8)
    pyautogui.click(720, 550)
    keyboard.press_and_release("page_down")
    time.sleep(0.5)
    pyautogui.click(670, 850)
    time.sleep(1)

    waiting = True
    while waiting:
        butloc = pyautogui.locateCenterOnScreen("buster.png")
        if butloc:
            print(f"found captcha at {butloc}")
            pyautogui.click(butloc)
            time.sleep(5)
        else:
            waiting = False
        time.sleep(0.1)

    pyautogui.click(730, 510)
    time.sleep(1)