import pyautogui

pyautogui.FAILSAFE = False

task_view_opened = False
desktop_returned = False

while True:
    x, y = pyautogui.position()
    if x <= 10 and y >= pyautogui.size().height - 10 and not task_view_opened:
        pyautogui.keyDown("win")
        pyautogui.keyDown("tab")
        pyautogui.keyUp("tab")
        pyautogui.keyUp("win")
        task_view_opened = True
    elif task_view_opened and not (x <= 10 and y >= pyautogui.size().height - 10):
        task_view_opened = False
    if x >= pyautogui.size().width - 10 and y >= pyautogui.size().height - 10 and not desktop_returned:
        pyautogui.keyDown("win")
        pyautogui.keyDown("d")
        pyautogui.keyUp("d")
        pyautogui.keyUp("win")
        desktop_returned = True
    elif desktop_returned and (x < pyautogui.size().width - 10 or y < pyautogui.size().height - 10):
        desktop_returned = False
    pyautogui.sleep(0.1)
