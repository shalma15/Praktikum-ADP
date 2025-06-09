import os
import time
from termcolor import colored


os.system('cls')

def tampilkan_logo():
    logo = [
        "  ..\\\_^_//..   ",
        " ... /\\_/\\ ...  ",
        "  ..( ^.^ ) ..  ",
        "  .. > ^ < ..   ",
        "     ~SHA~      ",
    ]
    for line in logo:
        print(colored(line,'black','on_light_green'))

def loading():
    for i in range(3):
        print(colored("   Loading" + "." * (i+1), 'black'))
        time.sleep(2)
        os.system('cls')
        tampilkan_logo()
    print(colored("\n   ..START..    \n", 'light_green'))
    time.sleep(1)


os.system('cls')
tampilkan_logo()
loading()

# if __name__ == "__main__":
#     main()