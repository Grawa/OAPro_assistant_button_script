from gpiozero import Button
from time import sleep
import keyboard

pulsante = Button(26,pull_up=True)

while True:
    if pulsante.is_pressed:
        keyboard.press("m")
        print("google assistant triggered!")
        sleep(0.30)
        keyboard.release("shift+m")