import msvcrt
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_key():
    key = msvcrt.getch()
    return key.decode('utf-8').lower()

print("Press WASD to move (Press 'q' to quit):")
while True:
    # clear()
    key = get_key()
    if key == 'w':
        print("Moving UP")
    elif key == 'a':
        print("Moving LEFT")
    elif key == 's':
        print("Moving DOWN")
    elif key == 'd':
        print("Moving RIGHT")
    elif key == 'q':
        break
    else:
        print("Invalid key")

print("Game over")
