import sys

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
    while True:
        ...


def init_list():
    for i in range(len(MENU)):
        print(MENU[i], end="")
        if i == selected:
            print(" ◄")
        else:
            print()

if __name__ == "__main__":
     main()