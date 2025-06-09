import os
import time
from termcolor import colored

def clear_screen():
    os.system('cls')

def tampilkan_logo_sr():
    logo = [
        "  ..\\\_^_//..   ",
        " ... /\\_/\\ ...  ",
        "  ..( ^.^ ) ..  ",
        "  .. > ^ < ..   ",
        "     ~SHA~      ",
    ]
    for line in logo:
        print(colored(line,'black','on_light_green'))

def animasi_loading():
    for i in range(3):
        print(colored("   Loading" + "." * (i+1), 'black'))
        time.sleep(2)
        clear_screen()
        tampilkan_logo_sr()
    print(colored("\n   ..START..    \n", 'light_green'))
    time.sleep(1)

def main():
    clear_screen()
    tampilkan_logo_sr()
    animasi_loading()

if __name__ == "__main__":
    main()
