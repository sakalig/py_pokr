import sys
from pynput.keyboard import Key, Listener
import os
import logging

# TODO: implement menu navigation using nodes
# sample menu
MENU = ["One", "Two", "Three", "Four", "Five"]
selected = 0

def main():
     # init logging module; TODO: add date suffix
    logging.basicConfig(filename="logs_navigation", filemode="a", format="%(asctime)s,%(msecs)03d %(name)s %(levelname)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S", level=logging.DEBUG)

    init()
     
def init():
    # screen refresh .. works on windows; TODO: test on linux/unix
    os.system("cls")

    print("Press ▲(Up) or ▼(Down) to navigate")

    #current_list = MENU
    #print(current_list)

    init_list()

    # Keystroke listener
    # while True:
    #     ...
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


def init_list():
    for i in range(len(MENU)):
        print(MENU[i], end="")
        if i == selected:
            print(" ◄")
        else:
            print()

def on_press(key):
    ...
    #logging.info("Pressed " + key)
    #print("Pressed ", key)

def on_release(key):
    global selected
    #logging.info("Released " + key)
    #print("Released ", key)
    if key == Key.esc:
        print("Quitting")
        return False
    if key == Key.enter:
        print("Selected: " + MENU[selected])
    if key == Key.down:
        selected = selected + 1
        if selected > len(MENU) - 1:
            selected = 0
        os.system("cls")
        init_list()

if __name__ == "__main__":
     main()