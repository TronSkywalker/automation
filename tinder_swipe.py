import pyautogui
import keyboard

i=0
while True: 
    pyautogui.dragRel(200, 0,duration=0.2)
    pyautogui.moveRel(-200, 0)
    i+=1
    try:
        if keyboard.is_pressed('q'):
            break
        else:
            pass
    finally:
        pass