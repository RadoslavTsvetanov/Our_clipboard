import keyboard
import time


def perform_action():
    print("Ctrl+C pressed! Exiting...")
    # Add any additional cleanup or exit logic here


# Define the key combination (Ctrl+C)
ctrl_key = 'ctrl'
c_key = 'c'

while True:
    # Check if Ctrl+C is pressed
    if keyboard.is_pressed(ctrl_key) and keyboard.is_pressed(c_key):
        perform_action()
        time.sleep(1)
