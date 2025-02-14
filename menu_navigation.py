import sys
from sys import platform
from pynput.keyboard import Key, Listener
import os
import logging
from constants import get_logo


# TODO: implement menu navigation using nodes
# sample menu
MENU = ["One", "Two", "Three", "Four", "Five"]
PLATFORM = ""
selected = 0

def main():
     # init logging module; TODO: add date suffix
    #logging.basicConfig(filename="logs/logs_navigation.txt", filemode="a", format="%(asctime)s,%(msecs)03d %(name)s %(levelname)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S", level=logging.DEBUG)

    global PLATFORM

    # TODO: log platform
    if platform == "linux":
        PLATFORM = "LINUX"
        print(PLATFORM)
    elif platform == "win32":
        PLATFORM = "WINDOWS"
        print(PLATFORM)
    elif platform == "unix":
        PLATFORM = "UNIX"
        print(PLATFORM)
    
    init()
     
def init():
    # TODO: test screen refresh on linux/unix

    init_list()

    # Keystroke listener
    # while True:
    #     ...
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


def init_list():
    border_draw()
    # TODO: Log platform info
    platform_clear(PLATFORM)

    print(get_logo())

    print("Press ▲(Up) or ▼(Down) to navigate")

    for i in range(len(MENU)):
        print(MENU[i], end="")
        if i == selected:
            print(" ◄")
        else:
            print()

def platform_clear(PLATFORM):
    match PLATFORM:
        case "LINUX":
            os.system("printf \033c")
            
        case "UNIX":
            os.system("printf \'\\033c\'")
            
        case "WINDOWS":
            os.system("cls")
            
        case default:
            print("Platform undetected")
            # throw error (Custom/Platform error)

def border_draw():
    w, h = os.get_terminal_size()

    for i in range(w):
        print("=", end="")
    

def on_press(key):
    ...
    #logging.info("Pressed " + key)
    #print("Pressed ", key)

def on_release(key):
    global selected
    #logging.info("Released " + key)
    #print("Released ", key)
    match(key):
        case Key.esc:
            print("Quitting")
            return False
        case Key.enter:
            print("Selected: " + MENU[selected])
        case Key.down:
            selected = selected + 1
            if selected > len(MENU) - 1:
                selected = 0
            platform_clear(PLATFORM)
            init_list()
        case Key.up:
            selected = selected - 1
            if selected == -1:
                selected = len(MENU) - 1
            platform_clear(PLATFORM)
            init_list()
    #elif key == 
        
    #elif key == 
        
    # elif key == Key.Up:
    #     selected = selected - 1
    #     if selected == 0:
    #         selected = len(MENU) - 1
    #     platform_clear(PLATFORM)
    #     #os.system("cls")
    #     init_list()

if __name__ == "__main__":
     main()