import random
import pyautogui
from time import sleep

# Set the current system time as seed for the random generator
random.seed()

while(True):
    # Generate the random number
    time = random.random() + random.random() + random.random()
    # Check that the random number is greater than 0.5
    if(time < 0.5):
        time = + 0.5
    # Sleep for the generated random time 0.5...3.0 seconds
    sleep(time)
    print(time)
    # Get the current mouse position
    mouseX, mouseY = pyautogui.position()
    # Click at the current mouse position
    pyautogui.click(mouseX, mouseY)
