import sys
from pynput.keyboard import Key, Listener

# TODO: implement menu navigation using nodes
# sample menu
MENU = ["One", "Two", "Three", "Four", "Five"]
selected = 0

def main():
     init()
     
def init():
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
    print("Pressed ", key)

def on_release(key):
    global selected
    print("Released ", key)
    if key == Key.esc:
        print("Quitting")
        return False
    if key == Key.down:
        selected = selected + 1
        if selected > len(MENU) - 1:
            selected = 0
        init_list()

if __name__ == "__main__":
     main()