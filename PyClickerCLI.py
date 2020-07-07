import random
import pyautogui
import time
from time import sleep
# Set the current system time as seed for the random generator
random.seed()

print("Clicking type selection:")
print("1 = Time in seconds")
print("2 = Ammount of clicks")
selection = input("Input selection:")


def random_sleep():
    # Generate the random number
    sleep_time = random.random() + random.random() + random.random()
    # Check that the random number is greater than 0.5
    if(sleep_time < 0.5):
        sleep_time = + 0.5
    # Sleep for the generated random time 0.5...3.0 seconds
    sleep(sleep_time)

    print("Slept for " + str(sleep_time) + " seconds. Clicking...")


def mouse_click():
    # Get the current mouse position
    mouseX, mouseY = pyautogui.position()
    # Click at the current mouse position
    pyautogui.click(mouseX, mouseY)


def timed_loop():
    clicking_time = input("Clicking time: ")
    current_time = time.time()

    try:
        stopping_time = int(clicking_time) + time.time()
    except ValueError:
        print("Give the clicking time as an integer!")
        print("Exiting...")
        exit()

    while current_time <= stopping_time:

        random_sleep()
        mouse_click()

        print(str(int(stopping_time) - int(current_time))
            + " seconds of clicking time remaining.")

        # Update the current time
        current_time = time.time()


def counted_loop():
    click_count = input("Number of clicks: ")
    clicked = 0

    try:
        click_count_int = int(click_count)
    except ValueError:
        print("Give the click count as an integer!")
        print("Exiting...")
        exit()

    while clicked <= click_count_int:

        random_sleep()
        mouse_click()
        # Increment the ammount of clicked

        print(str(click_count_int - clicked) + " clicks remaining.")
        clicked = clicked + 1


try:
    if int(selection) == 1:
        timed_loop()
    if int(selection) == 2:
        counted_loop()

except ValueError:
    print("Give the selection as an integer!")
    print("Exiting..")
